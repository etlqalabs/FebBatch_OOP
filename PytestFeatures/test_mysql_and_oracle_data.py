import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import pytest

# if you want to skip the test cases run then use skip
@pytest.mark.skip
def test_department_data_sourceAsOracle_and_targetAsmySQL_skip(connect_to_oracledb,connect_to_mysqldb):
    print("Test begin....")
    df_expected  = pd.read_sql("""select * from department""",connect_to_oracledb)
    print("expected data is ",df_expected)
    df_actual= pd.read_sql("""select * from department""", connect_to_mysqldb)
    print("actual data is ", df_actual)
    assert df_actual.equals(df_expected),"department data between source and target not matching"

# if you want to run the test cases but don't want that to be captire in your report
@pytest.mark.xfail
def test_department_data_sourceAsOracle_and_targetAsmySQL_xfail(connect_to_oracledb,connect_to_mysqldb):
    print("Test begin....")
    df_expected  = pd.read_sql("""select * from department""",connect_to_oracledb)
    print("expected data is ",df_expected)
    df_actual= pd.read_sql("""select * from department""", connect_to_mysqldb)
    print("actual data is ", df_actual)
    assert df_actual.equals(df_expected),"department data between source and target not matching"