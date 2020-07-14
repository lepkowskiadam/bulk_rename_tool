from snapshot import Snapshot
import pytest


@pytest.fixture
def path_file_names():
    path = 'test/path'
    old_file_names = [f'old_file_1{x}.txt' for x in range(10)]
    new_file_names = [f'new_file_1{x}.txt' for x in range(10)]
    return path, old_file_names, new_file_names


def test_init(snapshot):
    assert snapshot


def test_save_state(snapshot, path_file_names):
    path, old_file_names, new_file_names = path_file_names
    snapshot.save_state(path, old_file_names, new_file_names)
    assert len(snapshot.states) == 1
    assert snapshot.state == 0


def test_return_state(snapshot, path_file_names):
    path, old_file_names, new_file_names = path_file_names
    snapshot.save_state(path, old_file_names, new_file_names)
    result = snapshot.return_state()
    assert type(result) == tuple
    assert len(result) == 3
    assert result[1] == old_file_names
    assert result[2] == new_file_names


def test_undo(snapshot, path_file_names):
    path, old_file_names, new_file_names = path_file_names
    snapshot.save_state(path, old_file_names, new_file_names)
    assert snapshot.state == 0
    snapshot.undo()
    assert snapshot.state == 0
    snapshot.save_state(path, old_file_names, new_file_names)
    assert snapshot.state == 1
    snapshot.undo()
    assert snapshot.state == 0


def test_redo(snapshot, path_file_names):
    path, old_file_names, new_file_names = path_file_names
    snapshot.save_state(path, old_file_names, new_file_names)
    assert snapshot.state == 0
    snapshot.redo()
    assert snapshot.state == 0
    snapshot.save_state(path, old_file_names, new_file_names)
    assert snapshot.state == 1
    snapshot.undo()
    assert snapshot.state == 0
    snapshot.redo()
    assert snapshot.state == 1
