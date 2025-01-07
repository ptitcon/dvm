from config import set_up_root_logger


class Dotfiles:
    _instance = None

    def __new__(cls):
        if cls._instance is not None:
            raise RuntimeError("An instance of Dotfiles already exists!")
        cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        Dotfiles._instance = self
        self._logger = set_up_root_logger()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise RuntimeError("Dotfiles has not been initialized!")
        return cls._instance
