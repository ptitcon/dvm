import pytest

from pathlib import Path

from core.models import Symlink
from tests.config import (
    EXPECTED_BASH_FILES,
    Environment as Env,
)
from .utils import (
    filter_links_by_parent_dir,
    assert_links_count_equal,
    assert_all_links_match_expected,
    assert_all_links_match_expected_dst,
    assert_state_match_expected,
)


@pytest.mark.parametrize("variant", [Env.Variant.default(), Env.Variant.work()])
def test_bash_names(symlink_service, generate_environment):
    env = generate_environment

    links = symlink_service.generate_symlinks(env.variant_path)

    assert_all_links_match_expected(
        filter_links_by_parent_dir(links, env.bash), EXPECTED_BASH_FILES
    )


@pytest.mark.parametrize("variant", [Env.Variant.personal(), Env.Variant.work()])
def test_git_destination(symlink_service, generate_environment):
    env = generate_environment

    links = symlink_service.generate_symlinks(env.variant_path)

    assert_all_links_match_expected_dst(
        filter_links_by_parent_dir(links, env.bash), env.home
    )


@pytest.mark.parametrize("variant", [Env.Variant.personal(), Env.Variant.work()])
def test_symlinks_count(symlink_service, generate_environment):
    env = generate_environment

    links = symlink_service.generate_symlinks(env.variant_path)

    assert_links_count_equal(links, env.variant.dotfiles_count)


@pytest.mark.parametrize("variant", [Env.Variant.personal(), Env.Variant.work()])
def test_symlink_is_broken(symlink_service, mocker):
    """Test if symlink is broken."""
    src = mocker.MagicMock(spec=Path)
    src.exists.return_value = False

    dst = mocker.MagicMock(spec=Path)
    dst.is_symlink.return_value = True
    dst.readlink.return_value = src

    assert symlink_service.is_broken_link(dst)


@pytest.mark.parametrize("variant", [Env.Variant.personal(), Env.Variant.work()])
def test_symlink_is_not_broken(symlink_service, mocker):
    """Test if symlink is not broken."""
    src = mocker.MagicMock(spec=Path)
    src.exists.return_value = True

    dst = mocker.MagicMock(spec=Path)
    dst.is_symlink.return_value = True
    dst.readlink.return_value = src

    assert not symlink_service.is_broken_link(dst)


@pytest.mark.parametrize("variant", [Env.Variant.personal(), Env.Variant.work()])
def test_symlink_state_new(symlink_service, mocker):
    """Test symlink state is NEW."""
    dst = mocker.MagicMock(spec=Path)
    dst.exists.return_value = False

    assert_state_match_expected(
        symlink_service.get_symlink_state(dst), Symlink.State.NEW
    )


@pytest.mark.parametrize("variant", [Env.Variant.personal(), Env.Variant.work()])
def test_symlink_state_target_existing(symlink_service, mocker):
    """Test symlink state TARGET_EXISTING."""
    dst = mocker.MagicMock(spec=Path)
    dst.exists.return_value = True

    assert_state_match_expected(
        symlink_service.get_symlink_state(dst), Symlink.State.TARGET_EXISTING
    )


@pytest.mark.parametrize("variant", [Env.Variant.personal(), Env.Variant.work()])
def test_symlink_state_target_existing_as_link(symlink_service, mocker):
    """Test symlink state is still TARGET_EXISTING when the target is a symlink."""
    dst = mocker.MagicMock(spec=Path)
    dst.exists.return_value = True
    dst.is_symlink.return_value = True

    assert_state_match_expected(
        symlink_service.get_symlink_state(dst), Symlink.State.TARGET_EXISTING
    )


@pytest.mark.parametrize("variant", [Env.Variant.personal(), Env.Variant.work()])
def test_symlink_state_broken(symlink_service, mocker):
    """Test symlink state is BROKEN."""
    src = mocker.MagicMock(spec=Path)
    src.exists.return_value = False

    dst = mocker.MagicMock(spec=Path)
    dst.is_symlink.return_value = True
    dst.readlink.return_value = src

    assert_state_match_expected(
        symlink_service.get_symlink_state(dst), Symlink.State.BROKEN
    )
