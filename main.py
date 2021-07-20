# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from janitor import clean_names
import pandas as pd
from janitor import clean_names


# df = df.query("state == @state and agency==@agency").reset_index(drop=True)
# df.loc[rowIndex, 'New Column Title'] = "some value"

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

    print(df.head(5))
    print(df_service.head(5)['mode'])

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

    df.to_csv('version2.csv')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    step1()
    step2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
