# -*- coding: utf-8 -*-

"""Test code for the dynamic loading functions."""


import pytest
from cbc_binary_sdk.loader import dynamic_load, dynamic_create


class TestClassForLoad:
    """TODO"""
    pass


def test_dynamic_load():
    """TODO"""
    class1 = dynamic_load('test_loader.TestClassForLoad')
    assert class1 == TestClassForLoad
    with pytest.raises(ImportError):
        dynamic_load('bogus_package.bogus_class')


def test_dynamic_create():
    """TODO"""
    obj1 = dynamic_create('test_loader.TestClassForLoad')
    assert isinstance(obj1, TestClassForLoad)
    with pytest.raises(ImportError):
        dynamic_create('bogus_package.bogus_class')