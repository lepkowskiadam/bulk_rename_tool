import pytest


def test_init(matcher):
    assert matcher


def test_match(matcher, tmp_path, temp_files):
    pattern = '1'
    result = matcher.match(tmp_path, pattern)
    expected = ['my_file1.txt']
    assert result == expected


def test_match_multiple(matcher, tmp_path, multiple_patts):
    patterns = {'ś': 's', 'ą': 'a', 'ę': 'e'}
    expected = [(f'file_ąśę{i}.txt', ['ś', 'ą', 'ę']) for i in range(10)]
    result = matcher.match_multiple(tmp_path, **patterns)
    assert sorted(result) == sorted(expected)
