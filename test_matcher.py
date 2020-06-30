from matcher import Matcher
import pytest


@pytest.fixture(name='matcher')
def matcher():
    matcher = Matcher()
    return matcher


@pytest.fixture(name='temp_files')
def temp_files(tmp_path):
    d = tmp_path
    for i in range(10):
        p = d / f'my_file{i}.txt'
        p.write_text(f'{i}')


def test_init(matcher):
    assert matcher


def test_match(matcher, tmp_path, temp_files):
    pattern = '1'
    result = matcher.match(tmp_path, pattern)
    expected = ['my_file1.txt']
    assert result == expected

