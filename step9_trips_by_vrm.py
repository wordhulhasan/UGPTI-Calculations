import pandas as pd
from janitor import clean_names


def step9():
    df = pd.read_csv('../UGPTI-Calculations/Output/step8_opex_by_vrh.csv', dtype='str')
    df_2 = pd.read_csv('../UGPTI-Calculations/Output/step8_opex_by_vrh.csv', dtype='str')
    df = clean_names(df)
    df = df.head(5)
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
        df = totalTripsCalculationByVRM(df, df_2, index, ar, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, cb, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, cc, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, cr, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, dr, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, dt, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, fb, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, hr, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, ip, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, jt, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, lr, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, mb, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, mg, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, or_, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, pb, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, rb, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, sr, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, tb, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, tr, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, vp, 0)
        df = totalTripsCalculationByVRM(df, df_2,index, yr, 1)

    df.to_csv('../UGPTI-Calculations/Output/step9_trips_by_vrm.csv')


def totalTripsCalculationByVRM(df, df_2, index, mode, flag):
    if mode == "IP":
        return df
    tdf = df_2.query("ntd_id== @index")
    valTrips = float(tdf['upt_'+mode.lower()].to_string(index=False).replace(',', '').replace('$', '').replace(' ', ''))
    valVrm = float(tdf['vrm_'+mode.lower()].to_string(index=False).replace(',', '').replace('$', '').replace(' ', ''))
    if valVrm == 0:
        df.loc[index, 'upt_' + mode.lower() + '_per_vrm'] = 0
    else:
        df.loc[index, 'upt_' + mode.lower()+'_per_vrm'] = "{:.2f}".format(valTrips / valVrm)
    return df


if __name__ == '__main__':
    step9()
    print("Step 9 complete")