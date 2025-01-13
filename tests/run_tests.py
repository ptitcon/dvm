import pytest

from tests.config import TMP_PATH, MAX_FAIL


def main():
    args = [
        f"--basetemp={TMP_PATH}",
        "-v",
        "-s",
        f"--maxfail={MAX_FAIL}",
        "--disable-warnings",
    ]
    pytest.main(args)


def run_in_ci():
    args = [
        f"--basetemp={TMP_PATH}",
        "--maxfail=1",
        "--disable-warnings",
        "--tb=short",
    ]
    pytest.main(args)
