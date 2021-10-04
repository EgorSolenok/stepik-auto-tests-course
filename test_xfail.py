#!/usr/bin/env python3

import pytest

@pytest.mark.xfail
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False