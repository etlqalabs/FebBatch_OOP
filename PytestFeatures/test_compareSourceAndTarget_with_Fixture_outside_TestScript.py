import pandas as pd
import pytest

def test_compare_cemployee_src_and_tgt_using_pytest_1(expected_data_setup,actual_data_setup):
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"

def test_compare_cemployee_src_and_tgt_using_pytest_2(expected_data_setup,actual_data_setup):
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"

def test_compare_cemployee_src_and_tgt_using_pytest_3(expected_data_setup,actual_data_setup):
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"
