import pytest


def test_init(rename):
    assert rename


def test_undo(rename, temp_files, tmp_path):
    pattern = 'my_file'
    new_pattern = 'test_file'
    rename.rename(tmp_path, pattern, new_pattern)
    result = rename.undo()
    expected = [f'{pattern}{i}.txt' for i in range(10)]
    assert sorted(result) == sorted(expected)


def test_redo(rename, temp_files, tmp_path):
    pattern = 'my_file'
    new_pattern = 'test_file'
    rename.rename(tmp_path, pattern, new_pattern)
    rename.undo()
    result = rename.redo()
    expected = [f'{new_pattern}{i}.txt' for i in range(10)]
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize('pattern, new_pattern, expected', [
    ('e', 'es', [f'my_files{i}.txt' for i in range(10)]),
    ('my_file', 'test_pattern', [f'test_pattern{i}.txt' for i in range(10)]),
    ('', '', [f'my_file{i}.txt' for i in range(10)]),
    ('.txt', '.doc', [f'my_file{i}.txt' for i in range(10)])
])
def test_rename(rename, temp_files, tmp_path, pattern, new_pattern, expected):
    result = rename.rename(tmp_path, pattern, new_pattern)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize('pattern, new_pattern, expected', [
    ('file', 'new_file', [f'new_file_{i}.txt' for i in range(10)]),
    ('pattern_not_used', 'test', [])
])
def test_rename_full(rename, temp_files, tmp_path, pattern, new_pattern, expected):
    result = rename.rename_full(tmp_path, pattern, new_pattern)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize('patterns, expected', [
    ({'ś': 's', 'ą': 'a', 'ę': 'e'}, [f'file_ase{i}.txt' for i in range(10)]),
])
def test_rename_multiple_patterns(rename, tmp_path, patterns, expected, multiple_patts):
    result = rename.rename_multiple(tmp_path, patterns)
    assert sorted(result) == sorted(expected)
