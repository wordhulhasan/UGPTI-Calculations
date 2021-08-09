import pandas as pd
from janitor import clean_names


def step22():
    df = pd.read_csv('Output/step21_rvi_vehicle_seat_missing.csv', dtype='str')
    df = clean_names(df)
    # df = df.head(5)
    df = df.set_index('ntd_id')
    df_rev_inventory = pd.read_csv('Output/2019_rev_vehicle_inventory_modified.csv', dtype='str')

    vehicleCalculationByMode(df, df_rev_inventory, "Leased or borrowed from related parties by a private entity (LRPE)")
    totalCalculation(df, "LRPE")
    vehicleCalculationByMode(df, df_rev_inventory, "Leased or borrowed from related parties by a public agency (LRPA)")
    totalCalculation(df, "LRPA")
    vehicleCalculationByMode(df, df_rev_inventory, "Leased under lease purchase agreement by a private entity (LPPE)")
    totalCalculation(df, "LPPE")
    vehicleCalculationByMode(df, df_rev_inventory, "Leased under lease purchase agreement by a public agency (LPPA)")
    totalCalculation(df, "LPPA")
    vehicleCalculationByMode(df, df_rev_inventory, "Owned outright by private entity (OOPE)")
    totalCalculation(df, "OOPE")
    vehicleCalculationByMode(df, df_rev_inventory, "Owned outright by public agency (OOPA)")
    totalCalculation(df, "OOPA")
    vehicleCalculationByMode(df, df_rev_inventory, "True lease by private entity (TLPE)")
    totalCalculation(df, "TLPE")
    vehicleCalculationByMode(df, df_rev_inventory, "True lease by public agency (TLPA)")
    totalCalculation(df, "TLPA")
    df = clean_names(df)
    df.to_csv('Output/step22_rvi_vehicle_type_by_ownership.csv')

def totalCalculation(df, owner):
    for index2, row2, in df.iterrows():
        total = 0
        tdf2 = df.query("ntd_id== @index2")
        total = float(str(row2['number_of_Bus_'+owner.lower()])) \
                + float(str(row2['number_of_Cutaway_'+owner.lower()])) \
                + float(str(row2['number_of_Van_'+owner.lower()])) \
                + float(str(row2['number_of_Minivan_'+owner.lower()])) \
                + float(str(row2['number_of_Automobile_'+owner.lower()])) \
                + float(str(row2['number_of_School Bus_'+owner.lower()])) \
                + float(str(row2['number_of_Over-the-road Bus_'+owner.lower()])) \
                + float(str(row2['number_of_Sports Utility Vehicle_'+owner.lower()])) \
                + float(str(row2['number_of_Aerial Tramway_'+owner.lower()])) \
                + float(str(row2['number_of_Articulated Bus_'+owner.lower()])) \
                + float(str(row2['number_of_Ferryboat_'+owner.lower()])) \
                + float(str(row2['number_of_Streetcar Rail_'+owner.lower()])) \
                + float(str(row2['number_of_Trolleybus_'+owner.lower()])) \
                + float(str(row2['number_of_Light Rail Vehicle_'+owner.lower()])) \
                + float(str(row2['number_of_Commuter Rail Self-Propelled Passenger Car_'+owner.lower()])) \
                + float(str(row2['number_of_Commuter Rail Passenger Coach_'+owner.lower()])) \
                + float(str(row2['number_of_Monorail Vehicle_'+owner.lower()])) \
                + float(str(row2['number_of_Double Decker Bus_'+owner.lower()])) \
                + float(str(row2['number_of_Commuter Rail Locomotive_'+owner.lower()])) \
                + float(str(row2['number_of_Heavy Rail Passenger Car_'+owner.lower()])) \
                + float(str(row2['number_of_Vintage Trolley_'+owner.lower()])) \
                + float(str(row2['number_of_Inclined Plain Vehicle_'+owner.lower()])) \
                + float(str(row2['number_of_Automated Guideway Vehicle_'+owner.lower()])) \
                + float(str(row2['number_of_Cable Car_'+owner.lower()])) \
                + float(str(row2['number_of_Other_'+owner.lower()]))
        df.loc[index2, 'number_of_vehicle_'+owner.lower()+'_total'] = total

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


def vehicle_calculation(df, df_rev_inventory, vehicletype, owner):
    for index, row in df.iterrows():
        sum = 0
        tdf = df_rev_inventory.query("ntd_id== @index and vehicle_type == @vehicletype and ownership_type == @owner")
        for openIndex, row in tdf.iterrows():
            if str(row['active_fleet_vehicles']) == 'nan':
                row['active_fleet_vehicles'] = '0'
            sum = sum + int(str(row['active_fleet_vehicles']).replace(',', ''))
        if "LRPE" in owner:
            df.loc[index, 'number_of_' + vehicletype + "_lrpe"] = sum
        if "LRPA" in owner:
            df.loc[index, 'number_of_' + vehicletype + "_lrpa"] = sum
        if "LPPE" in owner:
            df.loc[index, 'number_of_' + vehicletype + "_lppe"] = sum
        if "LPPA" in owner:
            df.loc[index, 'number_of_' + vehicletype + "_lppa"] = sum
        if "OOPE" in owner:
            df.loc[index, 'number_of_' + vehicletype + "_oope"] = sum
        if "OOPA" in owner:
            df.loc[index, 'number_of_' + vehicletype + "_oopa"] = sum
        if "TLPE" in owner:
            df.loc[index, 'number_of_' + vehicletype + "_tlpe"] = sum
        if "TLPA" in owner:
            df.loc[index, 'number_of_' + vehicletype + "_tlpa"] = sum
        # df.loc[index, 'number_of_' + vehicletype+"_"+mode.lower()] = sum


if __name__ == '__main__':
    step22()
    print("Step 22 complete")
