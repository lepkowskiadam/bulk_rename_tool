from rename_tool import RenameTool
import pytest


@pytest.fixture(name='rename')
def fixture_rename():
    rename_tool = RenameTool()
    return rename_tool


def test_init(rename):
    assert rename
