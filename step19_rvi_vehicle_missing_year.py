import pandas as pd
from janitor import clean_names


def step19():
    df = pd.read_csv('Output/step18_rvi_vehicle_seats.csv', dtype='str')
    df = clean_names(df)
    # df = df.head(5)
    df = df.set_index('ntd_id')
    df_rev_inventory = pd.read_csv('Output/2019_rev_vehicle_inventory_modified.csv', dtype='str')


    vehicle_calculation(df, df_rev_inventory, "Bus")
    vehicle_calculation(df, df_rev_inventory, "Cutaway")
    vehicle_calculation(df, df_rev_inventory, "Van")
    vehicle_calculation(df, df_rev_inventory, "Minivan")
    vehicle_calculation(df, df_rev_inventory, "Automobile")
    vehicle_calculation(df, df_rev_inventory, "School Bus")
    vehicle_calculation(df, df_rev_inventory, "Over-the-road Bus")
    vehicle_calculation(df, df_rev_inventory, "Sports Utility Vehicle")
    vehicle_calculation(df, df_rev_inventory, "Aerial Tramway")
    vehicle_calculation(df, df_rev_inventory, "Articulated Bus")
    vehicle_calculation(df, df_rev_inventory, "Ferryboat")
    vehicle_calculation(df, df_rev_inventory, "Streetcar Rail")
    vehicle_calculation(df, df_rev_inventory, "Trolleybus")
    vehicle_calculation(df, df_rev_inventory, "Light Rail Vehicle")
    vehicle_calculation(df, df_rev_inventory, "Commuter Rail Self-Propelled Passenger Car")
    vehicle_calculation(df, df_rev_inventory, "Commuter Rail Passenger Coach")
    vehicle_calculation(df, df_rev_inventory, "Monorail Vehicle")
    vehicle_calculation(df, df_rev_inventory, "Double Decker Bus")
    vehicle_calculation(df, df_rev_inventory, "Commuter Rail Locomotive")
    vehicle_calculation(df, df_rev_inventory, "Heavy Rail Passenger Car")
    vehicle_calculation(df, df_rev_inventory, "Vintage Trolley")
    vehicle_calculation(df, df_rev_inventory, "Inclined Plain Vehicle")
    vehicle_calculation(df, df_rev_inventory, "Automated Guideway Vehicle")
    vehicle_calculation(df, df_rev_inventory, "Cable Car")
    vehicle_calculation(df, df_rev_inventory, "Other")

    totalCalculation(df)
    df = clean_names(df)
    df.to_csv('Output/step19_rvi_vehicle_missing_year.csv')


def totalCalculation(df):
    for index2, row2, in df.iterrows():
        total = 0
        tdf2 = df.query("ntd_id== @index2")
        total = float(str(row2['number_of_Bus_missing_year'])) \
                + float(str(row2['number_of_Cutaway_missing_year'])) \
                + float(str(row2['number_of_Van_missing_year'])) \
                + float(str(row2['number_of_Minivan_missing_year'])) \
                + float(str(row2['number_of_Automobile_missing_year'])) \
                + float(str(row2['number_of_School Bus_missing_year'])) \
                + float(str(row2['number_of_Over-the-road Bus_missing_year'])) \
                + float(str(row2['number_of_Sports Utility Vehicle_missing_year'])) \
                + float(str(row2['number_of_Aerial Tramway_missing_year'])) \
                + float(str(row2['number_of_Articulated Bus_missing_year'])) \
                + float(str(row2['number_of_Ferryboat_missing_year'])) \
                + float(str(row2['number_of_Streetcar Rail_missing_year'])) \
                + float(str(row2['number_of_Trolleybus_missing_year'])) \
                + float(str(row2['number_of_Light Rail Vehicle_missing_year'])) \
                + float(str(row2['number_of_Commuter Rail Self-Propelled Passenger Car_missing_year'])) \
                + float(str(row2['number_of_Commuter Rail Passenger Coach_missing_year'])) \
                + float(str(row2['number_of_Monorail Vehicle_missing_year'])) \
                + float(str(row2['number_of_Double Decker Bus_missing_year'])) \
                + float(str(row2['number_of_Commuter Rail Locomotive_missing_year'])) \
                + float(str(row2['number_of_Heavy Rail Passenger Car_missing_year'])) \
                + float(str(row2['number_of_Vintage Trolley_missing_year'])) \
                + float(str(row2['number_of_Inclined Plain Vehicle_missing_year'])) \
                + float(str(row2['number_of_Automated Guideway Vehicle_missing_year'])) \
                + float(str(row2['number_of_Cable Car_missing_year'])) \
                + float(str(row2['number_of_Other_missing_year']))
        df.loc[index2, 'number_vehicle_missing_year_total'] = total


def vehicle_calculation(df, df_rev_inventory, vehicletype):
    for index, row in df.iterrows():
        sum = 0
        tdf = df_rev_inventory.query("ntd_id== @index and vehicle_type == @vehicletype")
        tdf = tdf[tdf['manufacture_year'].isna()]
        for openIndex, row in tdf.iterrows():
            if str(row['active_fleet_vehicles']) == 'nan':
                row['active_fleet_vehicles'] = '0'
            sum = sum + int(str(row['active_fleet_vehicles']).replace(',', ''))
        df.loc[index, 'number_of_' + vehicletype+"_missing_year"] = sum


if __name__ == '__main__':
    step19()
    print("Step 19 complete")
