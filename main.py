# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# from janitor import clean_names
import pandas as pd


# df = df.query("state == @state and agency==@agency").reset_index(drop=True)
# df.loc[rowIndex, 'New Column Title'] = "some value"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    df = pd.read_csv('2019_a_info.csv')
    df_service = pd.read_csv('2019service.csv')
    df = df.set_index('NTD_ID')
    print(df.head(5))
    print(df_service.head(5))

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
            count = count+1

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
    df.to_csv('file_name_modes.csv', index=False)
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

        tdf = df.query("NTD_ID== @index and mode_mb== @valid "
                       "and mode_ar != @valid "
                       " and mode_cb != @valid "
                       " and mode_cc != @valid "
                       " and mode_cr != @valid "
                       " and mode_dr == @valid "
                       " and mode_dt != @valid "
                       " and mode_fb != @valid "
                       " and mode_hr != @valid "
                       " and mode_ip != @valid "
                       " and mode_jt != @valid "
                       " and mode_lr != @valid "
                       " and mode_mg != @valid "
                       " and mode_or != @valid "
                       " and mode_pb != @valid "
                       " and mode_rb != @valid "
                       " and mode_sr != @valid "
                       " and mode_tb != @valid "
                       " and mode_tr != @valid "
                       " and mode_vp != @valid "
                       " and mode_yr != @valid ")
        if tdf.empty:
            df.loc[index, 'mb_dr_only'] = 0
        else:
            df.loc[index, 'mb_dr_only'] = 1

    df.to_csv('version1.csv', index=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
