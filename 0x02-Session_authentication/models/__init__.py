#!/usr/bin/env python3
"""Initialize storage engine for the entire project.
Creates a single `FileStorage` instance accessible as `models.storage`."""
from models.engine.file_storage import FileStorage

# Global unique FileStorage instance
storage = FileStorage()
storage.reload()
