#!/usr/bin/env python3
"""Initialize storage engine"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
