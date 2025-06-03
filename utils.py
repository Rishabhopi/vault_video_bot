import time

cooldowns = {}

def is_on_cooldown(user_id: int, cooldown_sec: int):
    now = time.time()
    if user_id in cooldowns and cooldowns[user_id] > now:
        return True, int(cooldowns[user_id] - now)
    cooldowns[user_id] = now + cooldown_sec
    return False, 0
