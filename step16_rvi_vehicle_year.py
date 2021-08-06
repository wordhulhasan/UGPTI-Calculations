import pandas as pd
from janitor import clean_names


def step16():
    df = pd.read_csv('Output/step15_rvi_ada_vehicle_type.csv', dtype='str')
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
    df.to_csv('Output/step16_rvi_vehicle_year.csv')


def totalCalculation(df):
    for index2, row2, in df.iterrows():
        total = 0
        tdf2 = df.query("ntd_id== @index2")
        total = float(str(row2['number_fleet_year_Bus'])) \
                + float(str(row2['number_fleet_year_Cutaway'])) \
                + float(str(row2['number_fleet_year_Van'])) \
                + float(str(row2['number_fleet_year_Minivan'])) \
                + float(str(row2['number_fleet_year_Automobile'])) \
                + float(str(row2['number_fleet_year_School Bus'])) \
                + float(str(row2['number_fleet_year_Over-the-road Bus'])) \
                + float(str(row2['number_fleet_year_Sports Utility Vehicle'])) \
                + float(str(row2['number_fleet_year_Aerial Tramway'])) \
                + float(str(row2['number_fleet_year_Articulated Bus'])) \
                + float(str(row2['number_fleet_year_Ferryboat'])) \
                + float(str(row2['number_fleet_year_Streetcar Rail'])) \
                + float(str(row2['number_fleet_year_Trolleybus'])) \
                + float(str(row2['number_fleet_year_Light Rail Vehicle'])) \
                + float(str(row2['number_fleet_year_Commuter Rail Self-Propelled Passenger Car'])) \
                + float(str(row2['number_fleet_year_Commuter Rail Passenger Coach'])) \
                + float(str(row2['number_fleet_year_Monorail Vehicle'])) \
                + float(str(row2['number_fleet_year_Double Decker Bus'])) \
                + float(str(row2['number_fleet_year_Commuter Rail Locomotive'])) \
                + float(str(row2['number_fleet_year_Heavy Rail Passenger Car'])) \
                + float(str(row2['number_fleet_year_Vintage Trolley'])) \
                + float(str(row2['number_fleet_year_Inclined Plain Vehicle'])) \
                + float(str(row2['number_fleet_year_Automated Guideway Vehicle'])) \
                + float(str(row2['number_fleet_year_Cable Car'])) \
                + float(str(row2['number_fleet_year_Other']))
        df.loc[index2, 'number_fleet_year_total'] = total


def vehicle_calculation(df, df_rev_inventory, vehicletype):
    for index, row in df.iterrows():
        total = 0
        tdf = df_rev_inventory.query("ntd_id== @index and vehicle_type == @vehicletype")
        for openIndex, row in tdf.iterrows():
            if str(row['manufacture_year']).replace(',', '') == "nan":
                row['manufacture_year'] = "0"
            serviceYear = 2019 - int(str(row['manufacture_year']).replace(',', ''))
            if str(row['active_fleet_vehicles']) == 'nan':
                row['active_fleet_vehicles'] = '0'
            total = total + (serviceYear * int(str(row['active_fleet_vehicles']).replace(',', '')))
        df.loc[index, 'number_fleet_year_' + vehicletype] = total


if __name__ == '__main__':
    step16()
    print("Step 16 complete")
