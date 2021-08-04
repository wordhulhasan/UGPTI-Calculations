import pandas as pd
from janitor import clean_names
def step5():
    df = pd.read_csv('../UGPTI-Calculations/Output/step4_upt.csv', dtype ='str')
    df = clean_names(df)
    df = df.head(5)
    df = df.set_index('ntd_id')
    df_opex = pd.read_csv('../UGPTI-Calculations/NTD_Files/2019 Operating Expenses.csv')
    df_opex = clean_names(df_opex)
    ar = "AR"
    cb = "CB"
    cc = "CC"
    cr = "CR"
    dr = "DR"
    dt = "DT"
    fb = "FB"
    hr = "HR"
    ip = "IP"
    jt = "JT"
    lr = "LR"
    mb = "MB"
    mg = "MG"
    or_ = "OR"
    pb = "PB"
    rb = "RB"
    sr = "SR"
    tb = "TB"
    tr = "TR"
    vp = "VP"
    yr = "YR"
    for index, row in df.iterrows():
        df = totalOpexCalculation(df, df_opex, index, ar,0)
        df = totalOpexCalculation(df, df_opex, index, cb,0)
        df = totalOpexCalculation(df, df_opex, index, cc,0)
        df = totalOpexCalculation(df, df_opex, index, cr,0)
        df = totalOpexCalculation(df, df_opex, index, dr,0)
        df = totalOpexCalculation(df, df_opex, index, dt,0)
        df = totalOpexCalculation(df, df_opex, index, fb,0)
        df = totalOpexCalculation(df, df_opex, index, hr,0)
        df = totalOpexCalculation(df, df_opex, index, ip,0)
        df = totalOpexCalculation(df, df_opex, index, jt,0)
        df = totalOpexCalculation(df, df_opex, index, lr,0)
        df = totalOpexCalculation(df, df_opex, index, mb,0)
        df = totalOpexCalculation(df, df_opex, index, mg,0)
        df = totalOpexCalculation(df, df_opex, index, or_,0)
        df = totalOpexCalculation(df, df_opex, index, pb,0)
        df = totalOpexCalculation(df, df_opex, index, rb,0)
        df = totalOpexCalculation(df, df_opex, index, sr,0)
        df = totalOpexCalculation(df, df_opex, index, tb,0)
        df = totalOpexCalculation(df, df_opex, index, tr,0)
        df = totalOpexCalculation(df, df_opex, index, vp,0)
        df = totalOpexCalculation(df, df_opex, index, yr,1)

    df.to_csv('../UGPTI-Calculations/Output/step5_opex.csv')
def totalOpexCalculation(df, df_opex, index, mode,flag):
    pt = "PT"
    do = "DO"
    total = "Total"
    sum = 0
    tdf = df_opex.query("ntd_id== @index and mode== @mode and operating_expense_type== @total")
    if tdf.empty:
        df.loc[index, 'opex_'+mode.lower()] = 0
    else:
        if tdf.shape[0] > 1:
            tdf1 = tdf.query("tos == @pt")
            tdf2 = tdf.query("tos == @do")
            val1 = int(tdf1['total_operating_expenses'].to_string(index=False).replace(',', '').replace('$', ''))
            val2 = int(tdf2['total_operating_expenses'].to_string(index=False).replace(',', '').replace('$', ''))
            df.loc[index, 'opex_'+mode.lower()] = val1 + val2
        else:
            df.loc[index, 'opex_'+mode.lower()] = tdf['total_operating_expenses'].to_string(index=False).replace('$', '')
    if flag ==1:
        tdf_total = df_opex.query("ntd_id== @index and operating_expense_type== @total")
        for openIndex, row in tdf_total.iterrows():
            sum = sum + int(row['total_operating_expenses'].replace(',', '').replace('$', ''))
        df.loc[index,'opex_total'] = sum
    return df

if __name__ == '__main__':


    step5()
    print("Step 5 complete")