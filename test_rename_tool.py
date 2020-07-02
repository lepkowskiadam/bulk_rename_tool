import pytest


def test_init(rename):
    assert rename


def test_rename(rename, temp_files, tmp_path):
    pattern = 'my_file'
    new_pattern = 'test_file'
    result = rename.rename(tmp_path, pattern, new_pattern)
    expected = [f'{new_pattern}{i}.txt' for i in range(10)]
    assert sorted(result) == sorted(expected)


def test_undo(rename, temp_files, tmp_path):
    pattern = 'my_file'
    new_pattern = 'test_file'
    rename.rename(tmp_path, pattern, new_pattern)
    result = rename.undo()
    expected = [f'{pattern}{i}.txt' for i in range(10)]
    assert sorted(result) == sorted(expected)