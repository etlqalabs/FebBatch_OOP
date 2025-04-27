import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import pytest

print("I am insdie the fixture")
@pytest.fixture()
def expected_data_setup():
    print("expected data setup is being done")
    df_emp_expected = pd.read_csv("TestData/emp_src.csv")
    print("expected data setup is  done")
    yield df_emp_expected
    print("After test check done")

@pytest.fixture()
def actual_data_setup():
    print("actual data setup is being done")
    df_emp_actual = pd.read_csv("TestData/emp_tgt.csv")
    print("actual data setup is  done")
    yield df_emp_actual
    print("After test check done")


@pytest.fixture()
def connect_to_oracledb():
    print("Oracle database connection is being established...")
    engine = create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe")
    connection_oracle = engine.connect()
    print("Oracle database connection has been established...")
    yield connection_oracle
    connection_oracle.close()
    print("Oracle database connection has been closed...")

@pytest.fixture()
def connect_to_mysqldb():
    print("mysql database connection is being established...")
    engine = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/demo")
    connection_mysql = engine.connect()
    print("mysql database connection has been established...")
    yield connection_mysql
    connection_mysql.close()
    print("mysql database connection has been closed...")
