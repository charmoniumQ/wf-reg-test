from typing import Iterable, Any, Optional

import matplotlib  # type: ignore
import numpy
import numpy.typing

from .util import functional_shuffle


Color = Any


_ten_colors = functional_shuffle(list(matplotlib.colormaps["tab10"].colors))
def rand_color(idx: int, total: int) -> Color:
    if total < 10:
        return _ten_colors[idx]
    else:
        raise NotImplementedError("Not implemented for more than 10 colors")


def plot_kde(
        ax: matplotlib.axes.Axes,
        xs: Iterable[Any],
        dist: numpy.typing.NDArray[Any],
        rug: bool = False,
        label: Optional[str] = None,
        color: Optional[Color] = None,
        linestyle: Optional[str] = None,
) -> None:
    pass
