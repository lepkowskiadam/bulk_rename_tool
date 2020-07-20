import pytest


def test_init(matcher):
    assert matcher


def test_match(matcher, tmp_path, multiple_patts):
    patterns = {'ś': 's', 'ą': 'a', 'ę': 'e'}
    expected = [(f'file_ąśę{i}.txt', ['ś', 'ą', 'ę']) for i in range(10)]
    result = matcher.match(tmp_path, **patterns)
    assert sorted(result) == sorted(expected)
