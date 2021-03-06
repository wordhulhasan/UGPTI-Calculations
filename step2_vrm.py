import pandas as pd
from janitor import clean_names
def step2():
    df = pd.read_csv('../UGPTI-Calculations/Output/step1_mode.csv')
    df = clean_names(df)
    # df = df.head(5)
    df = df.set_index('ntd_id')
    df_service = pd.read_csv('../UGPTI-Calculations/NTD_Files/2019service.csv')
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

    vrm_total = 0
    for index, row in df.iterrows():
        # print(index)

        tdf = df_service.query("ntd_id== @index and mode== @ar and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_ar'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @ar and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @ar and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_ar'] = val1 + val2

            else:
                df.loc[index, 'vrm_ar'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_cb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_cb'] = val1 + val2
            else:
                df.loc[index, 'vrm_cb'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cc and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_cc'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cc and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cc and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_cc'] = val1 + val2

            else:
                df.loc[index, 'vrm_cc'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @cr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_cr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @cr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @cr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_cr'] = val1 + val2

            else:
                df.loc[index, 'vrm_cr'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @dr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_dr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @dr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @dr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_dr'] = val1 + val2

            else:
                df.loc[index, 'vrm_dr'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @dt and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_dt'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @dt and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @dt and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_dt'] = val1 + val2

            else:
                df.loc[index, 'vrm_dt'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @fb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_fb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @fb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @fb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_fb'] = val1 + val2
            else:
                df.loc[index, 'vrm_fb'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @hr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_hr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @hr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @hr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_hr'] = val1 + val2
            else:
                df.loc[index, 'vrm_hr'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @ip and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_ip'] = 0
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @ip and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @ip and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_ip'] = 0
            else:
                df.loc[index, 'vrm_ip'] = 0

        tdf = df_service.query("ntd_id== @index and mode== @jt and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_jt'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @jt and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @jt and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_jt'] = val1 + val2
            else:
                df.loc[index, 'vrm_jt'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @lr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_lr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @lr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @lr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_lr'] = val1 + val2
            else:
                df.loc[index, 'vrm_lr'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @mb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_mb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @mb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @mb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_mb'] = val1 + val2
            else:
                df.loc[index, 'vrm_mb'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @mg and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_mg'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @mg and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @mg and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_mg'] = val1 + val2
            else:
                df.loc[index, 'vrm_mg'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_or'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @or_ and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_or'] = val1 + val2
            else:
                df.loc[index, 'vrm_or'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @pb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_pb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @pb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @pb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_pb'] = val1 + val2
            else:
                df.loc[index, 'vrm_pb'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @rb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_rb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @rb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @rb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_rb'] = val1 + val2
            else:
                df.loc[index, 'vrm_rb'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @sr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_sr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @sr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @sr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_sr'] = val1 + val2
            else:
                df.loc[index, 'vrm_sr'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @tb and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_tb'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @tb and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @tb and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_tb'] = val1 + val2
            else:
                df.loc[index, 'vrm_tb'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @tr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_tr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @tr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @tr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_tr'] = val1 + val2
            else:
                df.loc[index, 'vrm_tr'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @vp and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_vp'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @vp and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @vp and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_vp'] = val1 + val2
            else:
                df.loc[index, 'vrm_vp'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

        tdf = df_service.query("ntd_id== @index and mode== @yr and time_period == @annualTotal")
        if tdf.empty:
            df.loc[index, 'vrm_yr'] = 0
        else:
            if tdf.shape[0] > 1:
                tdf1 = tdf.query("ntd_id== @index and mode== @yr and time_period == @annualTotal and tos == @pt")
                tdf2 = tdf.query("ntd_id== @index and mode== @yr and time_period == @annualTotal and tos == @do")
                val1 = int(tdf1['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                val2 = int(tdf2['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False).replace(',', ''))
                df.loc[index, 'vrm_yr'] = val1 + val2
            else:
                df.loc[index, 'vrm_yr'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)
        sum =0
        tdf_total = df_service.query("ntd_id== @index and time_period == @annualTotal")
        for openIndex, row in tdf_total.iterrows():
            sum = sum + int(row['actual_vehicle_passenger_car_revenue_miles'].replace(',', '').replace('$', ''))
        df.loc[index, 'vrm_total'] = sum
    df.to_csv('Output/step2_vrm.csv')


if __name__ == '__main__':
    step2()
    print("Step 2 complete")
