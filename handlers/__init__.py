# handlers/__init__.py

from .start import start_handler
from .callbacks import callback_handlers
from .admin import admin_handlers
from .uploader import uploader_handler
from .video import video_handler

__all__ = [
    "start_handler",
    "callback_handlers",
    "admin_handlers",
    "uploader_handler",
    "video_handler",
]
