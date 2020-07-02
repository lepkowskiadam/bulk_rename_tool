from snapshot import Snapshot
import pytest


def test_init(snapshot):
    assert snapshot


def test_save_state(snapshot, rename, tmp_path, temp_files):
    pattern = 'my_file'
    new_pattern = 'test_file'
    snapshot.save_state(tmp_path, pattern, new_pattern)
    assert len(snapshot.states) == 1

