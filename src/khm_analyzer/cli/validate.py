from __future__ import annotations

from typing import TYPE_CHECKING
from warnings import catch_warnings

from click import echo
from readylog.decorators import debug_in

from khm_analyzer.validation import validate_paths

if TYPE_CHECKING:
    from click import File


@debug_in
def validate(paths: tuple[File]) -> None:
    with catch_warnings(record=True) as w:
        validate_paths(paths)
    for warning in w:
        echo(warning.message)
