import pandas as pd
import pytest

@pytest.mark.order(3)
@pytest.mark.regression
def test_compare_employee_src_and_tgt_using_pytest_1(expected_data_setup,actual_data_setup):
    print("Orderb # 3.....")
    print("Test case 1 started.....")
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"
    print("Test case 1 completed.....")

@pytest.mark.order(5)
@pytest.mark.regression
@pytest.mark.smoke
def test_compare_employee_src_and_tgt_using_pytest_2(expected_data_setup,actual_data_setup):
    print("Orderb # 5.....")
    print("Test case 2 started.....")
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"
    print("Test case 2 completed.....")


@pytest.mark.smoke
def test_compare_employee_src_and_tgt_using_pytest_3(expected_data_setup,actual_data_setup):
    print("Test case 3 started.....")
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"
    print("Test case 2 completed.....")


# execute the test cases in proper order
@pytest.mark.order(1)
@pytest.mark.smoke
def test_compare_customer_src_and_tgt_using_pytest_1(expected_data_setup,actual_data_setup):
    print("Orderb # 1.....")
    print("Test case 1 started.....")
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"
    print("Test case 1 completed.....")

@pytest.mark.order(2)
@pytest.mark.smoke
def test_compare_customer_src_and_tgt_using_pytest_2(expected_data_setup,actual_data_setup):
    print("Orderb # 2.....")
    print("Test case 2 started.....")
    assert actual_data_setup.equals(expected_data_setup),"source data of employees doen not match with target employees data"
    print("Test case 2 completed.....")