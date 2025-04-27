import pandas as pd


def compare_cemployee_src_and_tgt_using_python():
    df_emp_src = pd.read_csv("../TestData/emp_src.csv")
    df_emp_tgt = pd.read_csv("../TestData/emp_tgt.csv")
    if(df_emp_tgt.equals(df_emp_src)):
        print("data matches")
    else:
        print("data between source and target does not match")

compare_cemployee_src_and_tgt_using_python()

