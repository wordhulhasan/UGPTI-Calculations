import pandas as pd
from janitor import clean_names
def step3():
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
            df.loc[index, 'vrh_ar'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @ar and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @ar and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_ar'] = val1 + val2
            else:
                df.loc[index, 'vrh_ar'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_cb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_cb'] = val1 + val2
            else:
                df.loc[index, 'vrh_cb'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cc and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_cc'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cc and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cc and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_cc'] = val1 + val2
            else:
                df.loc[index, 'vrh_cc'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_cr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_cr'] = val1 + val2
            else:
                df.loc[index, 'vrh_cr'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @dr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_dr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @dr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @dr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_dr'] = val1 + val2
            else:
                df.loc[index, 'vrh_dr'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @dt and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_dt'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @dt and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @dt and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_dt'] = val1 + val2
            else:
                df.loc[index, 'vrh_dt'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @fb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_fb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @fb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @fb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_fb'] = val1 + val2
            else:
                df.loc[index, 'vrh_fb'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @hr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_hr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @hr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @hr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_hr'] = val1 + val2
            else:
                df.loc[index, 'vrh_hr'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @ip and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_ip'] = 0
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @ip and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @ip and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_ip'] = val1 + val2
            else:
                df.loc[index, 'vrh_ip'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @jt and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_jt'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @jt and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @jt and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_jt'] = val1 + val2
            else:
                df.loc[index, 'vrh_jt'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @lr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_lr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @lr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @lr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_lr'] = val1 + val2
            else:
                df.loc[index, 'vrh_lr'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @mb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_mb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @mb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @mb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_mb'] = val1 + val2
            else:
                df.loc[index, 'vrh_mb'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @mg and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_mg'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @mg and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @mg and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_mg'] = val1 + val2
            else:
                df.loc[index, 'vrh_mg'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_or'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_or'] = val1 + val2
            else:
                df.loc[index, 'vrh_or'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @pb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_pb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @pb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @pb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_pb'] = val1 + val2
            else:
                df.loc[index, 'vrh_pb'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @rb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_rb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @rb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @rb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_rb'] = val1 + val2
            else:
                df.loc[index, 'vrh_rb'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @sr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_sr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @sr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @sr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_sr'] = val1 + val2
            else:
                df.loc[index, 'vrh_sr'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @tb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_tb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @tb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @tb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_tb'] = val1 + val2
            else:
                df.loc[index, 'vrh_tb'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @tr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_tr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @tr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @tr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_tr'] = val1 + val2
            else:
                df.loc[index, 'vrh_tr'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @vp and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_vp'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @vp and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @vp and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_vp'] = val1 + val2
            else:
                df.loc[index, 'vrh_vp'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @yr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrh_yr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @yr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @yr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrh_yr'] = val1 + val2
            else:
                df.loc[index, 'vrh_yr'] = tdf['actual_vehicle_passenger_car_revenue_hours'].to_string(index=False)

    df.to_csv('version2.csv')

if __name__ == '__main__':

    step3()
    print("Step 3 complete")
