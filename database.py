from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client.vault_video_bot

# Collections
videos_col = db.videos          # stores video message_ids
users_col = db.users            # stores users info and seen videos
sudos_col = db.sudos            # sudo user ids
banned_col = db.banned          # banned user ids
logs_col = db.logs              # logs

# Helper functions for CRUD ops

async def add_video(message_id: int):
    exists = await videos_col.find_one({"message_id": message_id})
    if not exists:
        await videos_col.insert_one({"message_id": message_id})

async def remove_video(message_id: int):
    await videos_col.delete_one({"message_id": message_id})

async def get_all_videos():
    cursor = videos_col.find({})
    return [doc["message_id"] async for doc in cursor]

async def add_sudo(user_id: int):
    exists = await sudos_col.find_one({"user_id": user_id})
    if not exists:
        await sudos_col.insert_one({"user_id": user_id})

async def remove_sudo(user_id: int):
    await sudos_col.delete_one({"user_id": user_id})

async def is_sudo(user_id: int) -> bool:
    doc = await sudos_col.find_one({"user_id": user_id})
    return bool(doc)

async def add_banned(user_id: int):
    exists = await banned_col.find_one({"user_id": user_id})
    if not exists:
        await banned_col.insert_one({"user_id": user_id})

async def remove_banned(user_id: int):
    await banned_col.delete_one({"user_id": user_id})

async def is_banned(user_id: int) -> bool:
    doc = await banned_col.find_one({"user_id": user_id})
    return bool(doc)

async def add_user_seen(user_id: int, message_id: int):
    user = await users_col.find_one({"user_id": user_id})
    if user:
        seen = user.get("seen", [])
        if message_id not in seen:
            seen.append(message_id)
            await users_col.update_one({"user_id": user_id}, {"$set": {"seen": seen}})
    else:
        await users_col.insert_one({"user_id": user_id, "seen": [message_id]})

async def get_user_seen(user_id: int):
    user = await users_col.find_one({"user_id": user_id})
    if user:
        return user.get("seen", [])
    return []

async def reset_user_seen(user_id: int):
    await users_col.update_one({"user_id": user_id}, {"$set": {"seen": []}}, upsert=True)

async def log_event(text: str):
    await logs_col.insert_one({"text": text})

async def get_sudos():
    cursor = sudos_col.find({})
    return [doc["user_id"] async for doc in cursor]
