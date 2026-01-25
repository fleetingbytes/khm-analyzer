from __future__ import annotations

from typing import TYPE_CHECKING

from khm_enums import Edition, Volume

if TYPE_CHECKING:
    from click import Context, Parameter


def to_edition(_ctx: Context, _param: Parameter, number: int) -> Edition:
    return Edition(number)


def to_volume(_ctx: Context, _param: Parameter, number: int) -> Volume:
    return Volume(number)
