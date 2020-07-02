from snapshot import Snapshot
import pytest


def test_init(snapshot):
    assert snapshot


def test_save_state(snapshot):
    snapshot.save_state('test/path', 'test_pattern', 'test_new_pattern')
    assert len(snapshot.states) == 1


def test_return_state(snapshot):
    snapshot.save_state('test/path', 'test_pattern', 'test_new_pattern')
    result = snapshot.return_state()
    assert type(result) == tuple
    assert len(result) == 3


def test_undo(snapshot):
    test_path_1 = 'test/path'
    test_pattern_1 = 'test_pattern'
    test_new_pattern_1 = 'test_new_pattern'
    test_path_2 = 'test/path'
    test_pattern_2 = 'test_pattern_2'
    test_new_pattern_2 = 'test_new_pattern_2'
    snapshot.save_state(test_path_1, test_pattern_1, test_new_pattern_1)
    snapshot.save_state(test_path_2, test_pattern_2, test_new_pattern_2)
    result = snapshot.return_state()
    path, old, new = result
    assert path == test_path_2
    assert old == test_pattern_2
    assert new == test_new_pattern_2
    snapshot.undo()
    result = snapshot.return_state()
    path, old, new = result
    assert path == test_path_1
    assert old == test_pattern_1
    assert new == test_new_pattern_1
    snapshot.undo()
    result = snapshot.return_state()
    path, old, new = result
    assert path == test_path_1
    assert old == test_pattern_1
    assert new == test_new_pattern_1
