from rename_tool import RenameTool
from matcher import Matcher
import pytest


@pytest.fixture(name='rename')
def rename():
    matcher = Matcher()
    rename_tool = RenameTool(Matcher())
    return rename_tool


@pytest.fixture(name='temp_files')
def temp_files(tmp_path):
    d = tmp_path
    for i in range(10):
        p = d / f'my_file{i}.txt'
        p.write_text(f'{i}')


def test_init(rename):
    assert rename


def test_rename(rename, temp_files, tmp_path):
    pattern = 'my_file'
    new_pattern = 'test_file'
    result = rename.rename(tmp_path, pattern, new_pattern)
    expected = [f'{new_pattern}{i}.txt' for i in range(10)]
    assert sorted(result) == sorted(expected)
