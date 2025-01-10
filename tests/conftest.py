import shutil
import os
import pytest


def pytest_sessionfinish(session):
    try:
        remove_tmp_dir(session.config.option.basetemp)
    except Exception as e:
        pytest.fail("Failed to remove tmp dir", e)


def remove_tmp_dir(tmp_path):
    if os.path.exists(tmp_path):
        shutil.rmtree(tmp_path)
