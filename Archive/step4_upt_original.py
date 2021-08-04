import pandas as pd
from janitor import clean_names
def step4():
    df = pd.read_csv('version2.csv', dtype ='str')
    df = clean_names(df)
    df = df.head(5)
    df = df.set_index('ntd_id')
    df_service = pd.read_csv('2019service.csv')
    df_service = clean_names(df_service)

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
    annualTotal = "Annual Total"
    pt = "PT"
    do = "DO"

    for index, row in df.iterrows():
        tdf = df_service.query("ntd_id== @index and mode== @ar and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_ar'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @ar and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @ar and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_ar'] = val1 + val2
            else:
                df.loc[index, 'upt_ar'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_cb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_cb'] = val1 + val2
            else:
                df.loc[index, 'upt_cb'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cc and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_cc'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cc and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cc and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_cc'] = val1 + val2
            else:
                df.loc[index, 'upt_cc'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_cr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_cr'] = val1 + val2
            else:
                df.loc[index, 'upt_cr'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @dr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_dr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @dr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @dr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_dr'] = val1 + val2
            else:
                df.loc[index, 'upt_dr'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @dt and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_dt'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @dt and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @dt and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_dt'] = val1 + val2
            else:
                df.loc[index, 'upt_dt'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @fb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_fb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @fb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @fb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_fb'] = val1 + val2
            else:
                df.loc[index, 'upt_fb'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @hr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_hr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @hr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @hr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_hr'] = val1 + val2
            else:
                df.loc[index, 'upt_hr'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @ip and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_ip'] = 0
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @ip and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @ip and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_ip'] = val1 + val2
            else:
                df.loc[index, 'upt_ip'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @jt and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_jt'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @jt and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @jt and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_jt'] = val1 + val2
            else:
                df.loc[index, 'upt_jt'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @lr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_lr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @lr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @lr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_lr'] = val1 + val2
            else:
                df.loc[index, 'upt_lr'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @mb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_mb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @mb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @mb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_mb'] = val1 + val2
            else:
                df.loc[index, 'upt_mb'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @mg and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_mg'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @mg and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @mg and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_mg'] = val1 + val2
            else:
                df.loc[index, 'upt_mg'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_or'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_or'] = val1 + val2
            else:
                df.loc[index, 'upt_or'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @pb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_pb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @pb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @pb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_pb'] = val1 + val2
            else:
                df.loc[index, 'upt_pb'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @rb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_rb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @rb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @rb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_rb'] = val1 + val2
            else:
                df.loc[index, 'upt_rb'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @sr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_sr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @sr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @sr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_sr'] = val1 + val2
            else:
                df.loc[index, 'upt_sr'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @tb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_tb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @tb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @tb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_tb'] = val1 + val2
            else:
                df.loc[index, 'upt_tb'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @tr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_tr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @tr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @tr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_tr'] = val1 + val2
            else:
                df.loc[index, 'upt_tr'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @vp and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_vp'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @vp and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @vp and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_vp'] = val1 + val2
            else:
                df.loc[index, 'upt_vp'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @yr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'upt_yr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @yr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @yr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['unlinked_passenger_trips_upt_'].to_string(index=False).replace(',', ''))
                df.loc[index, 'upt_yr'] = val1 + val2
            else:
                df.loc[index, 'upt_yr'] = tdf['unlinked_passenger_trips_upt_'].to_string(index=False)

    df.to_csv('version2.csv')

if __name__ == '__main__':
    step4()
    print("Step 4 complete")
