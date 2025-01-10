from pathlib import Path

from config import ROOT_DIR


class PathResolutionError(Exception):
    """Raised when there is an error resolving a path."""

    def __init__(self, file: Path):
        self.file = file
        self.message = f"Failed to resolve path for {file.relative_to(ROOT_DIR)}"
