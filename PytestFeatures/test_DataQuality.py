import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import pytest


@pytest.mark.skip
def test_duplicate_check_row_level(connect_to_oracledb):
    print("Duplicate check test started.....")
    df = pd.read_sql("""select * from department""",connect_to_oracledb)
    print("data is the database: ",df)
    count_dupes = df.duplicated().sum()
    print("count of duplicated rows ",count_dupes)
    assert count_dupes == 0,"There are duplicates - please"
    print("Duplicate check test started.....")

def test_count_check_row_level(connect_to_oracledb):
    print("Count check test started.....")
    df = pd.read_sql("""select count(*) from department""",connect_to_oracledb)
    print("data is the database: ",df)
    count_rows = df.iloc[0,0]
    print("count of rows ",count_rows)
    assert count_rows != 0,"There are zero records"
    print("Duplicate check test started.....")