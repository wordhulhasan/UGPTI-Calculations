import pandas as pd
from janitor import clean_names


def step1():
    # Use a breakpoint in the code line below to debug your script.
    df = pd.read_csv('2019_a_info.csv')
    df_service = pd.read_csv('2019service.csv')
    df = df.set_index('NTD_ID')
    print(df.head(5))
    print(df_service.head(5))

    # df = df.head(20)

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

        count = 0

        tdf = df_service.query("NTD_ID== @index and Mode== @ar")
        if tdf.empty:
            df.loc[index, 'mode_ar'] = 0
        else:
            df.loc[index, 'mode_ar'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @cb")
        if tdf.empty:
            df.loc[index, 'mode_cb'] = 0
        else:
            df.loc[index, 'mode_cb'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @cc")
        if tdf.empty:
            df.loc[index, 'mode_cc'] = 0
        else:
            df.loc[index, 'mode_cc'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @cr")
        if tdf.empty:
            df.loc[index, 'mode_cr'] = 0
        else:
            df.loc[index, 'mode_cr'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @dr")
        if tdf.empty:
            df.loc[index, 'mode_dr'] = 0
        else:
            df.loc[index, 'mode_dr'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @dt")
        if tdf.empty:
            df.loc[index, 'mode_dt'] = 0
        else:
            df.loc[index, 'mode_dt'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @fb")
        if tdf.empty:
            df.loc[index, 'mode_fb'] = 0
        else:
            df.loc[index, 'mode_fb'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @hr")
        if tdf.empty:
            df.loc[index, 'mode_hr'] = 0
        else:
            df.loc[index, 'mode_hr'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @ip")
        if tdf.empty:
            df.loc[index, 'mode_ip'] = 0
        else:
            df.loc[index, 'mode_ip'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @jt")
        if tdf.empty:
            df.loc[index, 'mode_jt'] = 0
        else:
            df.loc[index, 'mode_jt'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @lr")
        if tdf.empty:
            df.loc[index, 'mode_lr'] = 0
        else:
            df.loc[index, 'mode_lr'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @mb")
        if tdf.empty:
            df.loc[index, 'mode_mb'] = 0
        else:
            df.loc[index, 'mode_mb'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @mg")
        if tdf.empty:
            df.loc[index, 'mode_mg'] = 0
        else:
            df.loc[index, 'mode_mg'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @or_")
        if tdf.empty:
            df.loc[index, 'mode_or'] = 0
        else:
            df.loc[index, 'mode_or'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @pb")
        if tdf.empty:
            df.loc[index, 'mode_pb'] = 0
        else:
            df.loc[index, 'mode_pb'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @rb")
        if tdf.empty:
            df.loc[index, 'mode_rb'] = 0
        else:
            df.loc[index, 'mode_rb'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @sr")
        if tdf.empty:
            df.loc[index, 'mode_sr'] = 0
        else:
            df.loc[index, 'mode_sr'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @tb")
        if tdf.empty:
            df.loc[index, 'mode_tb'] = 0
        else:
            df.loc[index, 'mode_tb'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @tr")
        if tdf.empty:
            df.loc[index, 'mode_tr'] = 0
        else:
            df.loc[index, 'mode_tr'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @vp")
        if tdf.empty:
            df.loc[index, 'mode_vp'] = 0
        else:
            df.loc[index, 'mode_vp'] = 1
            count = count + 1

        tdf = df_service.query("NTD_ID== @index and Mode== @yr")
        if tdf.empty:
            df.loc[index, 'mode_yr'] = 0
        else:
            df.loc[index, 'mode_yr'] = 1
            count = count + 1

        df.loc[index, 'mode_total'] = count

        # print(tdf)
    print(df.head(10))  # Press Ctrl+F8 to toggle the breakpoint.
    df.to_csv('file_name_modes.csv')
    valid = 1
    nonValid = 0
    # MB DR VP
    for index, row in df.iterrows():

        tdf = df.query("NTD_ID== @index and mode_mb== @valid "
                       "and mode_ar != @valid "
                       "and mode_cb != @valid "
                       "and mode_cc != @valid "
                       "and mode_cr != @valid "
                       "and mode_dr != @valid "
                       "and mode_dt != @valid "
                       "and mode_fb != @valid "
                       "and mode_hr != @valid "
                       "and mode_ip != @valid "
                       "and mode_jt != @valid "
                       "and mode_lr != @valid "
                       "and mode_mg != @valid "
                       "and mode_or != @valid "
                       "and mode_pb != @valid "
                       "and mode_rb != @valid "
                       "and mode_sr != @valid "
                       "and mode_tb != @valid "
                       "and mode_tr != @valid "
                       "and mode_vp != @valid "
                       "and mode_yr != @valid ")
        if tdf.empty:
            df.loc[index, 'mb_only'] = 0
        else:
            df.loc[index, 'mb_only'] = 1

        tdf = df.query("NTD_ID== @index and mode_dr== @valid "
                       "and mode_ar != @valid "
                       "and mode_cb != @valid "
                       "and mode_cc != @valid "
                       "and mode_cr != @valid "
                       "and mode_mb != @valid "
                       "and mode_dt != @valid "
                       "and mode_fb != @valid "
                       "and mode_hr != @valid "
                       "and mode_ip != @valid "
                       "and mode_jt != @valid "
                       "and mode_lr != @valid "
                       "and mode_mg != @valid "
                       "and mode_or != @valid "
                       "and mode_pb != @valid "
                       "and mode_rb != @valid "
                       "and mode_sr != @valid "
                       "and mode_tb != @valid "
                       "and mode_tr != @valid "
                       "and mode_vp != @valid "
                       "and mode_yr != @valid ")
        if tdf.empty:
            df.loc[index, 'dr_only'] = 0
        else:
            df.loc[index, 'dr_only'] = 1

        tdf = df.query("NTD_ID== @index and mode_vp== @valid "
                       "and mode_ar != @valid "
                       "and mode_cb != @valid "
                       "and mode_cc != @valid "
                       "and mode_cr != @valid "
                       "and mode_dr != @valid "
                       "and mode_dt != @valid "
                       "and mode_fb != @valid "
                       "and mode_hr != @valid "
                       "and mode_ip != @valid "
                       "and mode_jt != @valid "
                       "and mode_lr != @valid "
                       "and mode_mg != @valid "
                       "and mode_or != @valid "
                       "and mode_pb != @valid "
                       "and mode_rb != @valid "
                       "and mode_sr != @valid "
                       "and mode_tb != @valid "
                       "and mode_tr != @valid "
                       "and mode_mb != @valid "
                       "and mode_yr != @valid ")
        if tdf.empty:
            df.loc[index, 'vp_only'] = 0
        else:
            df.loc[index, 'vp_only'] = 1

        tdf = df.query("NTD_ID== @index and mode_mb== @valid and mode_dr == @valid ")
        if tdf.empty:
            df.loc[index, 'mb_dr'] = 0
        else:
            df.loc[index, 'mb_dr'] = 1

    df.to_csv('version1.csv')


def step2():
    df = pd.read_csv('version1.csv')
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
                df.loc[index, 'vrm_ip'] = val1 + val2
            else:
                df.loc[index, 'vrm_ip'] = tdf['actual_vehicle_passenger_car_revenue_miles'].to_string(index=False)

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
    print(df.head(3))
    df.to_csv('version2.csv')


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

def step5():
    df = pd.read_csv('version2.csv', dtype ='str')
    df = clean_names(df)
    df = df.head(5)
    df = df.set_index('ntd_id')
    df_service = pd.read_csv('2019 Operating Expenses.csv')
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
    for index, row in df.iterrows():
        df = totalOpexCalculation(df, df_service, index, ar,0)
        df = totalOpexCalculation(df, df_service, index, cb,0)
        df = totalOpexCalculation(df, df_service, index, cc,0)
        df = totalOpexCalculation(df, df_service, index, cr,0)
        df = totalOpexCalculation(df, df_service, index, dr,0)
        df = totalOpexCalculation(df, df_service, index, dt,0)
        df = totalOpexCalculation(df, df_service, index, fb,0)
        df = totalOpexCalculation(df, df_service, index, hr,0)
        df = totalOpexCalculation(df, df_service, index, ip,0)
        df = totalOpexCalculation(df, df_service, index, jt,0)
        df = totalOpexCalculation(df, df_service, index, lr,0)
        df = totalOpexCalculation(df, df_service, index, mb,0)
        df = totalOpexCalculation(df, df_service, index, mg,0)
        df = totalOpexCalculation(df, df_service, index, or_,0)
        df = totalOpexCalculation(df, df_service, index, pb,0)
        df = totalOpexCalculation(df, df_service, index, rb,0)
        df = totalOpexCalculation(df, df_service, index, sr,0)
        df = totalOpexCalculation(df, df_service, index, tb,0)
        df = totalOpexCalculation(df, df_service, index, tr,0)
        df = totalOpexCalculation(df, df_service, index, vp,0)
        df = totalOpexCalculation(df, df_service, index, yr,1)

    df.to_csv('version2.csv')


def totalOpexCalculation(df, df_service, index, mode,flag):
    pt = "PT"
    do = "DO"
    total = "Total"
    sum = 0
    tdf = df_service.query("ntd_id== @index and mode== @mode and operating_expense_type== @total")
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
        tdf_total = df_service.query("ntd_id== @index and operating_expense_type== @total")
        for openIndex, row in tdf_total.iterrows():
            sum = sum + int(row['total_operating_expenses'].replace(',', '').replace('$', ''))
        df.loc[index,'opex_total'] = sum
    return df

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # step1()
    # print("Step 1 complete")
    step2()
    print("Step 2 complete")
    step3()
    print("Step 3 complete")
    step4()
    print("Step 4 complete")
    step5()
    print("Step 5 complete")
