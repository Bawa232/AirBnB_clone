#!/usr/bin/python3
"""Instantiates the fileStorage class which would be used to handle storage"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
