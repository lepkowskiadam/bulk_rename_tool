import pytest


def test_init(rename):
    assert rename


@pytest.mark.parametrize('patterns, expected', [
    ({'file': 'not_file'}, [f'my_file{i}.txt' for i in range(10)])
])
def test_undo(rename, temp_files, tmp_path, patterns, expected):
    rename.replace(tmp_path, **patterns)
    result = rename.undo()
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize('patterns, expected', [
    ({'file': 'not_file'}, [f'my_not_file{i}.txt' for i in range(10)])
])
def test_redo(rename, temp_files, tmp_path, patterns, expected):
    assert type(rename.replace(tmp_path, **patterns)) == list
    rename.undo()
    result = rename.redo()
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize('pattern, new_pattern, expected', [
    ('file', 'new_file', [f'new_file_{i}.txt' for i in range(10)]),
    ('pattern_not_used', 'test', [])
])
def test_rename(rename, temp_files, tmp_path, pattern, new_pattern, expected):
    result = rename.rename(tmp_path, pattern, new_pattern)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize('patterns, expected', [
    ({'file': 'not_file', 'ś': 's', 'ą': 'a', 'ę': 'e'}, [f'not_file_ase{i}.txt' for i in range(10)])
])
def test_replace(rename, tmp_path, patterns, expected, multiple_patts):
    result = rename.replace(tmp_path, **patterns)
    assert sorted(result) == sorted(expected)
