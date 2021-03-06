import pandas as pd
from janitor import clean_names


def step6():
    df = pd.read_csv('Output/step5_opex.csv', dtype='str')
    df_2 = pd.read_csv('Output/step5_opex.csv', dtype='str')
    df = clean_names(df)
    # df = df.head(5)
    df = df.set_index('ntd_id')
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
        df = totalOpexCalculationbyTrip(df, df_2, index, ar, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, cb, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, cc, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, cr, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, dr, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, dt, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, fb, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, hr, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, ip, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, jt, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, lr, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, mb, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, mg, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, or_, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, pb, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, rb, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, sr, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, tb, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, tr, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, vp, 0)
        df = totalOpexCalculationbyTrip(df, df_2,index, yr, 1)

        opexPerTripTotalCalculation(df, df_2, index)
    df.to_csv('Output/step6_opex_by_upt.csv')


def opexPerTripTotalCalculation(df, df_2, index):
    tdf = df_2.query("ntd_id== @index")
    valOpexTotal = float(
        tdf['opex_total'].to_string(index=False).replace(',', '').replace('$', '').replace(' ', ''))
    valUptTotal = float(
        tdf['upt_total'].to_string(index=False).replace(',', '').replace('$', '').replace(' ', ''))
    if valUptTotal == 0:
        df.loc[index, 'opex_per_trip_total'] = 0
    else:
        df.loc[index, 'opex_per_trip_total'] = "{:.2f}".format(valOpexTotal / valUptTotal)


def totalOpexCalculationbyTrip(df, df_2, index, mode, flag):
    if mode == "IP":
        return df
    tdf = df_2.query("ntd_id== @index")
    valOpex = float(tdf['opex_'+mode.lower()].to_string(index=False).replace(',', '').replace('$', '').replace(' ', ''))
    valUpt = float(tdf['upt_'+mode.lower()].to_string(index=False).replace(',', '').replace('$', '').replace(' ', ''))
    if valUpt == 0:
        df.loc[index, 'opex_' + mode.lower() + '_per_trip'] = 0
    else:
        df.loc[index, 'opex_' + mode.lower()+'_per_trip'] = "{:.2f}".format(valOpex / valUpt)
    return df


if __name__ == '__main__':
    step6()
    print("Step 6 complete")
