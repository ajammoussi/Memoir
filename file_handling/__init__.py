"""
File Handling Module
Unified file monitoring for local filesystem and cloud sources.

Modules:
- storage_schemas: Data models (FileEvent, EventType, Source, FileType)
- event_queue: Thread-safe event queue with workers
- filesystem_watcher: Local filesystem monitoring with watchdog
- public_cloud_monitor: Public Google Drive and OneDrive monitoring
- server: FastAPI REST API server
"""
from core.storage_schemas import FileEvent, EventType, Source, FileType
from core.event_queue import EventQueue
from watchers.filesystem_watcher import FilesystemMonitor
from watchers.public_cloud_monitor import PublicCloudMonitor
from api.server import app

__all__ = [
    'FileEvent',
    'EventType', 
    'Source',
    'FileType',
    'EventQueue',
    'FilesystemMonitor',
    'PublicCloudMonitor',
    'app'
]
