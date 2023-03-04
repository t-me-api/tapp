from enum import Enum


class Match(Enum):
    """
    Help to match :class:`tapp.routing.route.TRoute` is matches event.
    """

    NONE = 0
    MATCH = 1
