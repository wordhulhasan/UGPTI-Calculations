import pandas as pd
from janitor import clean_names

def step11():
    df = pd.read_csv('Output/step10_trips_by_vrh.csv', dtype ='str')
    df = clean_names(df)
    df = df.head(5)
    df = df.set_index('ntd_id')
    df_rev_source = pd.read_csv('NTD_Files/2019 Revenue Sources.csv', dtype ='str')
    df_rev_source = clean_names(df_rev_source)

    funds_expended_type = "Funds Expended on Operations"
    for index, row in df.iterrows():
        tdf = df_rev_source.query("ntd_id== @index and funds_expended_type == @funds_expended_type")
        for index2, row2 in tdf.iterrows():
            tdf2 = tdf.query("index==@index2")
            val1 = tdf2['funding_category'].to_string(index=False)
            val2 = tdf2['total'].to_string(index=False)
            df.loc[index, val1+"_Operations"] = val2

    df.to_csv('Output/step11_revenue_source.csv')

if __name__ == '__main__':
    step11()
    print("Step 11 complete")