import pandas as pd
from janitor import clean_names


def step14():
    df = pd.read_csv('Output/step13_rvi_vehicle_type.csv', dtype='str')
    df = clean_names(df)
    # df = df.head(5)
    df = df.set_index('ntd_id')
    df_rev_inventory = pd.read_csv('Output/2019_rev_vehicle_inventory_modified.csv', dtype='str')

    vehicleCalculationByMode(df, df_rev_inventory, "DR")
    totalCalculation(df, "DR")
    vehicleCalculationByMode(df, df_rev_inventory, "MB")
    totalCalculation(df, "MB")
    vehicleCalculationByMode(df, df_rev_inventory, "CB")
    totalCalculation(df, "CB")
    vehicleCalculationByMode(df, df_rev_inventory, "VP")
    totalCalculation(df, "VP")
    vehicleCalculationByMode(df, df_rev_inventory, "DT")
    totalCalculation(df, "DT")

    df.to_csv('Output/step14_rvi_vehicle_type_by_mode.csv')

def totalCalculation(df, mode):
    for index2, row2, in df.iterrows():
        total = 0
        tdf2 = df.query("ntd_id== @index2")
        total = float(str(row2['number_of_Bus_'+mode.lower()])) \
                + float(str(row2['number_of_Cutaway_'+mode.lower()])) \
                + float(str(row2['number_of_Van_'+mode.lower()])) \
                + float(str(row2['number_of_Minivan_'+mode.lower()])) \
                + float(str(row2['number_of_Automobile_'+mode.lower()])) \
                + float(str(row2['number_of_School Bus_'+mode.lower()])) \
                + float(str(row2['number_of_Over-the-road Bus_'+mode.lower()])) \
                + float(str(row2['number_of_Sports Utility Vehicle_'+mode.lower()])) \
                + float(str(row2['number_of_Aerial Tramway_'+mode.lower()])) \
                + float(str(row2['number_of_Articulated Bus_'+mode.lower()])) \
                + float(str(row2['number_of_Ferryboat_'+mode.lower()])) \
                + float(str(row2['number_of_Streetcar Rail_'+mode.lower()])) \
                + float(str(row2['number_of_Trolleybus_'+mode.lower()])) \
                + float(str(row2['number_of_Light Rail Vehicle_'+mode.lower()])) \
                + float(str(row2['number_of_Commuter Rail Self-Propelled Passenger Car_'+mode.lower()])) \
                + float(str(row2['number_of_Commuter Rail Passenger Coach_'+mode.lower()])) \
                + float(str(row2['number_of_Monorail Vehicle_'+mode.lower()])) \
                + float(str(row2['number_of_Double Decker Bus_'+mode.lower()])) \
                + float(str(row2['number_of_Commuter Rail Locomotive_'+mode.lower()])) \
                + float(str(row2['number_of_Heavy Rail Passenger Car_'+mode.lower()])) \
                + float(str(row2['number_of_Vintage Trolley_'+mode.lower()])) \
                + float(str(row2['number_of_Inclined Plain Vehicle_'+mode.lower()])) \
                + float(str(row2['number_of_Automated Guideway Vehicle_'+mode.lower()])) \
                + float(str(row2['number_of_Cable Car_'+mode.lower()])) \
                + float(str(row2['number_of_Other_'+mode.lower()]))
        df.loc[index2, 'number_of_vehicle_'+mode.lower()+'_total'] = total

def vehicleCalculationByMode(df, df_rev_inventory, mode):
    vehicle_calculation(df, df_rev_inventory, "Bus", mode)
    vehicle_calculation(df, df_rev_inventory, "Cutaway", mode)
    vehicle_calculation(df, df_rev_inventory, "Van", mode)
    vehicle_calculation(df, df_rev_inventory, "Minivan", mode)
    vehicle_calculation(df, df_rev_inventory, "Automobile", mode)
    vehicle_calculation(df, df_rev_inventory, "School Bus", mode)
    vehicle_calculation(df, df_rev_inventory, "Over-the-road Bus", mode)
    vehicle_calculation(df, df_rev_inventory, "Sports Utility Vehicle", mode)
    vehicle_calculation(df, df_rev_inventory, "Aerial Tramway", mode)
    vehicle_calculation(df, df_rev_inventory, "Articulated Bus", mode)
    vehicle_calculation(df, df_rev_inventory, "Ferryboat", mode)
    vehicle_calculation(df, df_rev_inventory, "Streetcar Rail", mode)
    vehicle_calculation(df, df_rev_inventory, "Trolleybus", mode)
    vehicle_calculation(df, df_rev_inventory, "Light Rail Vehicle", mode)
    vehicle_calculation(df, df_rev_inventory, "Commuter Rail Self-Propelled Passenger Car", mode)
    vehicle_calculation(df, df_rev_inventory, "Commuter Rail Passenger Coach", mode)
    vehicle_calculation(df, df_rev_inventory, "Monorail Vehicle", mode)
    vehicle_calculation(df, df_rev_inventory, "Double Decker Bus", mode)
    vehicle_calculation(df, df_rev_inventory, "Commuter Rail Locomotive", mode)
    vehicle_calculation(df, df_rev_inventory, "Heavy Rail Passenger Car", mode)
    vehicle_calculation(df, df_rev_inventory, "Vintage Trolley", mode)
    vehicle_calculation(df, df_rev_inventory, "Inclined Plain Vehicle", mode)
    vehicle_calculation(df, df_rev_inventory, "Automated Guideway Vehicle", mode)
    vehicle_calculation(df, df_rev_inventory, "Cable Car", mode)
    vehicle_calculation(df, df_rev_inventory, "Other", mode)


def vehicle_calculation(df, df_rev_inventory, vehicletype, mode):
    for index, row in df.iterrows():
        sum = 0
        tdf = df_rev_inventory.query("ntd_id== @index and vehicle_type == @vehicletype and modes == @mode")
        for openIndex, row in tdf.iterrows():
            if str(row['active_fleet_vehicles']) == 'nan':
                row['active_fleet_vehicles'] = '0'
            sum = sum + int(str(row['active_fleet_vehicles']).replace(',', ''))
        df.loc[index, 'number_of_' + vehicletype+"_"+mode.lower()] = sum


if __name__ == '__main__':
    step14()
    print("Step 14 complete")
