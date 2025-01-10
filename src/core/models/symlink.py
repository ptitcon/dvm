from dataclasses import dataclass
from enum import Enum
from pathlib import Path


@dataclass(frozen=True)
class Symlink:
    source: Path
    target: Path
    state: "Symlink.State"

    State = Enum("State", "NEW, TARGET_EXISTING, BROKEN")
