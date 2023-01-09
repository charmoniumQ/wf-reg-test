# from typing import Iterable, Any
# from .util import functional_shuffle
# import matplotlib


# Color = Any


# _ten_colors = functional_shuffle(matplotlib.colormaps["tab10"].colors)
# def rand_color(idx: int, total: int) -> Color:
#     if total < 10:
#         return _ten_colors[idx]
#     else:
#         raise NotImplementedError("Not implemented for more than 10 colors")


# def plot_kde(
#         ax: matplotlib.axes.Axes,
#         xs: Iterable[Any],
#         dist: np.NDarray,
#         rug: bool = False,
#         label: Optional[str] = None,
#         color: Optional[Color] = None,
#         linestyle: Optional[str] = None,
# ) -> None:
#     pass


# def plot_kdes(
#         ax: matplotlib.axes.Axes,
#         dists: list[np.NDarray],
#         rug: bool = False,
#         labels: list[str] = None,
#         colors: Optional[list[Color]] = None,
#         linestyles: Optional[str] = None,
# ) -> None:
#     if colors is None:
#         colors = _ten_colors[len(dists)]
#     if linestyles is None:
#         linestyles = [None] * len(dists)
#     for dist, label, color, linestyle in zip(dists, labels, colors, line_styles):
#         plot_kde(
#             ax,
#             dist,
#             rug,
#             label,
#             color,
#             linestyle,
#         )
