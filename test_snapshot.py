from snapshot import Snapshot
import pytest


def test_init(snapshot):
    assert snapshot


def test_save_state(snapshot):
    snapshot.save_state('test/path', 'test_pattern', 'test_new_pattern', 'test')
    assert len(snapshot.states) == 1


def test_return_state(snapshot):
    snapshot.save_state('test/path', 'test_pattern', 'test_new_pattern', 'test')
    result = snapshot.return_state()
    assert type(result) == tuple
    assert len(result) == 4


def test_undo(snapshot):
    test_path_1 = 'test/path'
    test_pattern_1 = 'test_pattern'
    test_new_pattern_1 = 'test_new_pattern'
    func = 'test'
    test_path_2 = 'test/path'
    test_pattern_2 = 'test_pattern_2'
    test_new_pattern_2 = 'test_new_pattern_2'
    snapshot.save_state(test_path_1, test_pattern_1, test_new_pattern_1, func)
    snapshot.save_state(test_path_2, test_pattern_2, test_new_pattern_2, func)
    result = snapshot.return_state()
    path, old, new, func = result
    assert path == test_path_2
    assert old == test_pattern_2
    assert new == test_new_pattern_2
    snapshot.undo()
    result = snapshot.return_state()
    path, old, new, func = result
    assert path == test_path_1
    assert old == test_pattern_1
    assert new == test_new_pattern_1
    snapshot.undo()
    result = snapshot.return_state()
    path, old, new, func = result
    assert path == test_path_1
    assert old == test_pattern_1
    assert new == test_new_pattern_1


def test_redo(snapshot):
    test_path_1 = 'test/path'
    test_pattern_1 = 'test_pattern'
    test_new_pattern_1 = 'test_new_pattern'
    func = 'test'
    test_path_2 = 'test/path'
    test_pattern_2 = 'test_pattern_2'
    test_new_pattern_2 = 'test_new_pattern_2'
    snapshot.save_state(test_path_1, test_pattern_1, test_new_pattern_1, func)
    snapshot.save_state(test_path_2, test_pattern_2, test_new_pattern_2, func)
    snapshot.undo()
    result = snapshot.return_state()
    path, old, new, func = result
    assert path == test_path_1
    assert old == test_pattern_1
    assert new == test_new_pattern_1
    snapshot.redo()
    result = snapshot.return_state()
    path, old, new, func = result
    assert path == test_path_2
    assert old == test_pattern_2
    assert new == test_new_pattern_2
    snapshot.redo()
    result = snapshot.return_state()
    path, old, new, func = result
    assert path == test_path_2
    assert old == test_pattern_2
    assert new == test_new_pattern_2
