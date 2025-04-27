import pandas as pd
import pytest

@pytest.fixture()
def expected_data_setup():
    print("expected data setup is being done")
    df_emp_expected = pd.read_csv("../TestData/emp_src.csv")
    return df_emp_expected

@pytest.fixture()
def actual_data_setup():
    print("actual data setup is being done")
    df_emp_actual = pd.read_csv("../TestData/emp_tgt.csv")
    return df_emp_actual



def test_compare_cemployee_src_and_tgt_using_pytest_1(expected_data_setup,actual_data_setup):
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"

def test_compare_cemployee_src_and_tgt_using_pytest_2(expected_data_setup,actual_data_setup):
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"

def test_compare_cemployee_src_and_tgt_using_pytest_3(expected_data_setup,actual_data_setup):
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"
