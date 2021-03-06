from rename_tool import RenameTool
from matcher import Matcher
from snapshot import Snapshot
import pytest


@pytest.fixture(name='snapshot')
def snapshot():
    snapshot = Snapshot()
    return snapshot


@pytest.fixture(name='matcher')
def matcher():
    matcher = Matcher()
    return matcher


@pytest.fixture(name='rename')
def rename():
    rename_tool = RenameTool()
    return rename_tool


@pytest.fixture(name='temp_files')
def temp_files(tmp_path):
    d = tmp_path
    for i in range(10):
        p = d / f'my_file{i}.txt'
        p.write_text(f'{i}')


@pytest.fixture(name='multiple_patts')
def multiple_patts(tmp_path):
    d = tmp_path
    for i in range(10):
        p = d / f'file_ąśę{i}.txt'
        p.write_text(f'{i}')
