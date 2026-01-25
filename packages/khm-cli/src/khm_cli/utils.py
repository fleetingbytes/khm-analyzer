from __future__ import annotations

from typing import TYPE_CHECKING

from readylog.decorators import debug_in

if TYPE_CHECKING:
    from pathlib import Path


@debug_in
def create_parent_dir_if_not_exists(file_path: Path) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
