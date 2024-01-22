from typing import cast
from ipyfoo import Counter
import anywidget._file_contents

def test_counter():
    counter = Counter()
    counter.value = 10
    assert counter._esm
    assert counter.value == 10
    fc = cast(anywidget._file_contents.FileContents, Counter._esm)
    assert fc._background_thread is not None
    fc.stop_thread()
    assert fc._background_thread is None
