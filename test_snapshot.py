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
