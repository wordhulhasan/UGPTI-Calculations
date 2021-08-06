import pandas as pd
from janitor import clean_names


def step13():
    df = pd.read_csv('Output/step12_revenue_source_capital.csv', dtype='str')
    df = clean_names(df)
    # df = df.head(5)
    df = df.set_index('ntd_id')
    df_rev_inventory = pd.read_csv('NTD_Files/2019 Revenue Vehicle Inventory.csv', dtype='str')
    df_rev_inventory = clean_names(df_rev_inventory)
    df_rev_inventory['modes'] = df_rev_inventory['modes'].str.split('/').str[0]
    df_rev_inventory.to_csv('Output/2019_rev_vehicle_inventory_modified.csv')
    # df_rev_inventory['active_fleet_vehicles'] = df_rev_inventory['active_fleet_vehicles'].fillna(0)

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

    df.to_csv('Output/step13_rvi_vehicle_type.csv')


def totalCalculation(df):
    for index2, row2, in df.iterrows():
        total = 0
        tdf2 = df.query("ntd_id== @index2")
        total = float(str(row2['number_of_Bus'])) \
                + float(str(row2['number_of_Cutaway'])) \
                + float(str(row2['number_of_Van'])) \
                + float(str(row2['number_of_Minivan'])) \
                + float(str(row2['number_of_Automobile'])) \
                + float(str(row2['number_of_School Bus'])) \
                + float(str(row2['number_of_Over-the-road Bus'])) \
                + float(str(row2['number_of_Sports Utility Vehicle'])) \
                + float(str(row2['number_of_Aerial Tramway'])) \
                + float(str(row2['number_of_Articulated Bus'])) \
                + float(str(row2['number_of_Ferryboat'])) \
                + float(str(row2['number_of_Streetcar Rail'])) \
                + float(str(row2['number_of_Trolleybus'])) \
                + float(str(row2['number_of_Light Rail Vehicle'])) \
                + float(str(row2['number_of_Commuter Rail Self-Propelled Passenger Car'])) \
                + float(str(row2['number_of_Commuter Rail Passenger Coach'])) \
                + float(str(row2['number_of_Monorail Vehicle'])) \
                + float(str(row2['number_of_Double Decker Bus'])) \
                + float(str(row2['number_of_Commuter Rail Locomotive'])) \
                + float(str(row2['number_of_Heavy Rail Passenger Car'])) \
                + float(str(row2['number_of_Vintage Trolley'])) \
                + float(str(row2['number_of_Inclined Plain Vehicle'])) \
                + float(str(row2['number_of_Automated Guideway Vehicle'])) \
                + float(str(row2['number_of_Cable Car'])) \
                + float(str(row2['number_of_Other']))
        df.loc[index2, 'number_of_vehicle_total'] = total


def vehicle_calculation(df, df_rev_inventory, vehicletype):
    for index, row in df.iterrows():
        sum = 0
        tdf = df_rev_inventory.query("ntd_id== @index and vehicle_type == @vehicletype")
        for openIndex, row in tdf.iterrows():
            if str(row['active_fleet_vehicles']) == 'nan':
                row['active_fleet_vehicles'] = '0'
            sum = sum + int(str(row['active_fleet_vehicles']).replace(',', ''))
        df.loc[index, 'number_of_' + vehicletype] = sum


if __name__ == '__main__':
    step13()
    print("Step 13 complete")
