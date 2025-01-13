from dataclasses import dataclass, field
from pathlib import Path
from enum import Enum, auto
from collections import namedtuple


@dataclass(frozen=True)
class Environment:
    data_dir: Path
    variant: "Environment.Variant"

    @property
    def variant_path(self) -> Path:
        return self.data_dir.joinpath(self.variant.name.lower())

    @property
    def home(self) -> Path:
        return Path.home()

    @property
    def bash(self) -> Path:
        return self.variant_path.joinpath("bash")

    @property
    def git(self) -> Path:
        return self.variant_path.joinpath("git")

    @property
    def tmux(self) -> Path:
        return self.variant_path.joinpath("tmux")

    @property
    def vim(self) -> Path:
        return self.variant_path.joinpath("vim")

    # The values represent the number of dotfiles that are expected in each variant.
    Variant = Enum("Variant", [("DEFAULT", 6), ("PERSONAL", 6), ("WORK", 6)])
