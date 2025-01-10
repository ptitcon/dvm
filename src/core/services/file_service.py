import json

from pathlib import Path

from config import ROOT_DIR, DATA_DIR
from core.exceptions import PathResolutionError


class FileService:

    @property
    def data_dir(self) -> Path:
        return Path(self._data_dir)

    @property
    def possible_paths(self) -> dict[str, list[str]]:
        """
        Return the dictionary of possible configuration paths loaded from the
        `dotfiles.json` file, where keys are tool names and values are lists of
        potential file paths for those tools.

        :return: A dictionary where keys are tool names (e.g., 'vim', 'tmux') and
        values are lists of paths to dotfiles for those tools.
        """
        return self._possible_paths

    def __init__(self, data_dir: str = DATA_DIR):
        self._data_dir = data_dir
        with open(f"{ROOT_DIR}/dotfiles.json", "r") as f:
            self._possible_paths = json.load(f)

    def resolve_path(self, dotfile: Path):
        """
        Resolve and return the correct file path for the given dotfile
        by looking it up in the predefined paths from `dotfiles.json`.

        If no matching path is found, raise a `PathResolutionError`.

        :param: dotfile: The path to the dotfile to resolve.
        :return: The resolved file path if found.
        :raises PathResolutionError: If no matching path is found in the possible paths.
        """
        for path in self.possible_paths.get(dotfile.parent.name, []):
            expanded_path = Path(path).expanduser()
            if expanded_path.name == dotfile.name:
                return expanded_path
        raise PathResolutionError(dotfile)
