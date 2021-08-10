import pandas as pd
from janitor import clean_names
def step24():
    df = pd.read_csv('Output/step23_rvi_vehicle_type_by_funding.csv', dtype ='str')
    df = clean_names(df)
    df = df.head(10)
    df = df.set_index('ntd_id')
    df_fare = pd.read_csv('NTD_Files/2019 Fare Revenue.csv', encoding= 'unicode_escape', dtype ='str')
    df_fare = clean_names(df_fare)
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
        df = totalFareCalculation(df, df_fare, index, ar,0)
        df = totalFareCalculation(df, df_fare, index, cb,0)
        df = totalFareCalculation(df, df_fare, index, cc,0)
        df = totalFareCalculation(df, df_fare, index, cr,0)
        df = totalFareCalculation(df, df_fare, index, dr,0)
        df = totalFareCalculation(df, df_fare, index, dt,0)
        df = totalFareCalculation(df, df_fare, index, fb,0)
        df = totalFareCalculation(df, df_fare, index, hr,0)
        df = totalFareCalculation(df, df_fare, index, ip,0)
        df = totalFareCalculation(df, df_fare, index, jt,0)
        df = totalFareCalculation(df, df_fare, index, lr,0)
        df = totalFareCalculation(df, df_fare, index, mb,0)
        df = totalFareCalculation(df, df_fare, index, mg,0)
        df = totalFareCalculation(df, df_fare, index, or_,0)
        df = totalFareCalculation(df, df_fare, index, pb,0)
        df = totalFareCalculation(df, df_fare, index, rb,0)
        df = totalFareCalculation(df, df_fare, index, sr,0)
        df = totalFareCalculation(df, df_fare, index, tb,0)
        df = totalFareCalculation(df, df_fare, index, tr,0)
        df = totalFareCalculation(df, df_fare, index, vp,0)
        df = totalFareCalculation(df, df_fare, index, yr,1)

    df.to_csv('Output/step25_fare_revenue_by_mode.csv')

def totalFareCalculation(df, df_fare, index, mode,flag):
    if mode == "IP":
        return df
    pt = "PT"
    do = "DO"
    sum = 0
    tdf = df_fare.query("ntd_id== @index and mode== @mode")
    if tdf.empty:
        df.loc[index, 'fare_'+mode.lower()] = 0
    else:
        if tdf.shape[0] > 1:
            tdf1 = tdf.query("tos == @pt")
            tdf2 = tdf.query("tos == @do")
            val1 = int(tdf1['total_fares'].to_string(index=False).replace(',', '').replace('$', ''))
            val2 = int(tdf2['total_fares'].to_string(index=False).replace(',', '').replace('$', ''))
            df.loc[index, 'fare_'+mode.lower()] = val1 + val2
        else:
            df.loc[index, 'fare_'+mode.lower()] = tdf['total_fares'].to_string(index=False).replace('$', '')
    if flag ==1:
        tdf_total = df_fare.query("ntd_id== @index")
        for openIndex, row in tdf_total.iterrows():
            sum = sum + int(row['total_fares'].replace(',', '').replace('$', ''))
        df.loc[index,'fare_revenue_total'] = sum
    return df

if __name__ == '__main__':
    step24()
    print("Step 24 complete")