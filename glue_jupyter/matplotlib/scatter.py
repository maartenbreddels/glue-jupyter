from __future__ import absolute_import, division, print_function

from glue.utils import defer_draw, decorate_all_methods
from glue.viewers.scatter.layer_artist import ScatterLayerArtist
from glue.viewers.scatter.state import ScatterViewerState
from glue.viewers.scatter.viewer import MatplotlibScatterMixin

from .base import MatplotlibJupyterViewer

__all__ = ['ScatterJupyterViewer']


@decorate_all_methods(defer_draw)
class ScatterJupyterViewer(MatplotlibScatterMixin, MatplotlibJupyterViewer):

    LABEL = '2D Scatter'

    _state_cls = ScatterViewerState
    _data_artist_cls = ScatterLayerArtist
    _subset_artist_cls = ScatterLayerArtist

    def __init__(self, session, parent=None, state=None):
        super(ScatterJupyterViewer, self).__init__(session, parent=parent, state=state)
        MatplotlibScatterMixin.setup_callbacks(self)
