from config import set_up_root_logger
from core.services import FileService, SymlinkService


class Dvm:
    _instance = None

    @property
    def symlink_service(self) -> SymlinkService:
        return self._symlink_service

    def __new__(cls):
        if cls._instance is not None:
            raise RuntimeError("An instance of Dvm already exists!")
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        Dvm._instance = self
        self._logger = set_up_root_logger()
        self._symlink_service = SymlinkService(FileService())

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise RuntimeError("Dvm has not been initialized!")
        return cls._instance
