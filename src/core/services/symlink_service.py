import logging

from pathlib import Path
from typing import List

from core.exceptions import PathResolutionError
from core.models import Symlink
from core.services import FileService


class SymlinkService:

    def __init__(self, file_service: FileService):
        self._logger = logging.getLogger(__class__.__name__)
        self._file_service = file_service

    def is_broken_link(self, target: Path) -> bool:
        if not target.is_symlink():
            return False
        try:
            return not target.readlink().exists()
        except OSError:
            return True

    def get_symlink_state(self, target: Path) -> "Symlink.State":
        """
        Get the state of the symlink based on its target's existence.

        :param target: The symlink to check.
        :return: The state of the symlink.
        """
        if not target.exists():
            return Symlink.State.NEW

        return (
            Symlink.State.BROKEN
            if self.is_broken_link(target)
            else Symlink.State.TARGET_EXISTING
        )

    def generate_symlinks(self, src_dir: Path) -> List[Symlink]:
        """
        Generate symlinks for files in the given source directory.

        :param: The source directory to generate symlinks from.
        :return: A list of Symlink objects representing the generated symlinks.
        :raises ValueError: If the source directory is invalid or not inside the
                            'data' directory.
        """
        symlinks = []

        if not src_dir.is_dir():
            raise ValueError("Source must be a directory.")

        if src_dir.parent != self._file_service.data_dir:
            raise ValueError("Source must be inside the 'data' directory.")

        for subfolder in src_dir.iterdir():
            if not subfolder.is_dir():
                continue

            for file in subfolder.iterdir():
                src = file.resolve()
                try:
                    dst = self._file_service.resolve_path(file)
                    symlinks.append(Symlink(src, dst, self.get_symlink_state(dst)))
                except PathResolutionError as e:
                    self._logger.warning(e.message)
                    continue
        return symlinks
