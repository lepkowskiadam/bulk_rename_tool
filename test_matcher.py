import pytest


def test_init(matcher):
    assert matcher


def test_match(matcher, tmp_path, temp_files):
    pattern = '1'
    result = matcher.match(tmp_path, pattern)
    expected = ['my_file1.txt']
    assert result == expected

