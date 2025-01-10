# flake8: noqa: E501,

from typing import List, Callable
from pathlib import Path

from core.models import Symlink


def filter_links_by_parent_dir(links: List[Symlink], parent_dir: Path) -> List[Symlink]:
    """
    Filter symlinks whose source parent directory matches the specified directory.

    :param links: List of Symlink objects to filter.
    :param parent_dir: The directory to match.
    :return: List of Symlink objects whose source parent directory matches the specified directory.
    """
    return filter_links(links, lambda sym: sym.source.parent == parent_dir)


def filter_links(
    links: List[Symlink], predicate: Callable[[Symlink], bool]
) -> List[Symlink]:
    """
    Filter symlinks based on a given predicate.

    :param links: List of Symlink objects to filter.
    :param predicate: A callable that takes a Symlink object and returns a boolean.
    :return: List of Symlink objects that match the predicate.
    """
    return list(filter(predicate, links))


def assert_links_count_equal(links: List[Symlink], expected_count: int):
    """
    Assert that the number of symlinks matches the expected count.

    :param links: List of Symlink objects.
    :param expected_count: The expected number of symlinks.
    :raises AssertionError: If the actual number of symlinks does not match the expected count.
    """
    actual_count = len(links)
    assert (
        actual_count == expected_count
    ), f"Expected {expected_count} symlinks, but found {actual_count}."


def assert_all_links_match_expected(links: List[Symlink], expected_files: set[str]):
    """
    Assert that all symlinks match the expected files.

    :param links: List of Symlink objects.
    :param expected_files: Set of expected file names.
    :raises AssertionError: If not all symlinks match the expected files.
    """
    assert_links_not_empty(links)
    assert all(
        sym.source.name in expected_files and sym.target.name in expected_files
        for sym in links
    ), f"Not all symlinks match the expected files. Expected files: {expected_files}, found: {', '.join([f'{sym.source.name} -> {sym.target.name}' for sym in links])}"


def assert_all_links_match_expected_dst(links: List[Symlink], expected_dst: Path):
    """
    Assert that all symlinks have the expected destination directory.

    :param links: List of Symlink objects.
    :param expected_dst: The expected destination directory.
    :raises AssertionError: If not all symlinks have the expected destination directory.
    """
    assert_links_not_empty(links)
    assert all(
        sym.target.parent == expected_dst for sym in links
    ), f"Not all symlinks have the expected destination. Expected destination: {expected_dst}, found: {', '.join([f'{sym.target.parent}' for sym in links])}"


def assert_state_match_expected(actual: Symlink.State, expected: Symlink.State):
    """
    Assert that the actual state matches the expected state.

    :param actual: The actual state.
    :param expected: The expected state.
    :raises AssertionError: If the actual state does not match the expected state.
    """
    assert actual == expected, f"Expected state: {expected}, found: {actual}"


def assert_links_not_empty(links: List[Symlink]):
    """
    Assert that the list of links is not empty.

    :param links: List of Symlink objects.
    :raises AssertionError: If the list of links is empty.
    """
    assert links, "The list of links is empty."
