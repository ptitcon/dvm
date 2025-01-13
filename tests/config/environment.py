from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class Environment:
    data_dir: Path
    variant: "Environment.Variant"

    @property
    def variant_path(self) -> Path:
        return self.data_dir.joinpath(self.variant.name)

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

    @dataclass
    class Variant:
        name: str
        dotfiles_count: int = field(default=0)

        @classmethod
        def default(cls):
            return cls("default", 6)

        @classmethod
        def personal(cls):
            return cls("personal", 6)

        @classmethod
        def work(cls):
            return cls("work", 6)
