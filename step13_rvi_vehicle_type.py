import pandas as pd
from janitor import clean_names

def step13():
    df = pd.read_csv('Output/step12_revenue_source_capital.csv', dtype ='str')
    df = clean_names(df)
    #df = df.head(5)
    df = df.set_index('ntd_id')
    df_rev_inventory = pd.read_csv('NTD_Files/2019 Revenue Vehicle Inventory.csv', dtype ='str')
    df_rev_inventory = clean_names(df_rev_inventory)
    df_rev_inventory['modes'] = df_rev_inventory['modes'].str.split('/').str[0]
    df_rev_inventory.to_csv('Output/2019_rev_vehicle_inventory_modified.csv')
    df_rev_inventory['active_fleet_vehicles'] = df_rev_inventory['active_fleet_vehicles'].fillna(0)
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
    df.to_csv('Output/step13_rvi_vehicle_type.csv')


def vehicle_calculation(df, df_rev_inventory,vehicletype):
    for index, row in df.iterrows():
        sum = 0
        tdf = df_rev_inventory.query("ntd_id== @index and vehicle_type == @vehicletype")
        for openIndex, row in tdf.iterrows():
            sum = sum + int(row['active_fleet_vehicles'].replace(',', ''))
        df.loc[index, 'number_of_'+vehicletype] = sum


if __name__ == '__main__':
    step13()
    print("Step 13 complete")