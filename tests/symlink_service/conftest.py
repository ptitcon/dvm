import pytest
import shutil

from typing import Generator
from pathlib import Path

from core.services import SymlinkService, FileService
from config import TEST_DIR
from tests.config import Environment as Env

DATA_DIR = TEST_DIR / "data"


@pytest.fixture(scope="function")
def symlink_service(generate_environment: Env) -> SymlinkService:
    return SymlinkService(FileService(data_dir=generate_environment.data_dir))


@pytest.fixture(scope="function")
def generate_environment(tmp_path, variant: Env.Variant) -> Generator[Env, None, None]:
    try:
        copy_data_to_tmp_dir(tmp_path)
        yield Env(tmp_path, variant)
    except Exception as e:
        pytest.fail("Failed to generate environment", e)


def copy_data_to_tmp_dir(tmp_dir: Path):
    shutil.copytree(DATA_DIR, tmp_dir, dirs_exist_ok=True)
