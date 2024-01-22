from typing import cast
from ipyfoo import Counter
import anywidget._file_contents

def test_counter():
    counter = Counter()
    counter.value = 10
    assert counter._esm
    assert counter.value == 10
    cast(anywidget._file_contents.FileContents, Counter._esm)._background_thread.join()
