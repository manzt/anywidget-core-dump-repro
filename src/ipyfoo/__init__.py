import importlib.metadata
import pathlib

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("ipyfoo")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"


class Counter(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    value = traitlets.Int(0).tag(sync=True)
