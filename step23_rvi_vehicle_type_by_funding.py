import pandas as pd
from janitor import clean_names


def step23():
    df = pd.read_csv('Output/step22_rvi_vehicle_type_by_ownership.csv', dtype='str')
    df = clean_names(df)
    #df = df.head(15)
    df = df.set_index('ntd_id')
    df_rev_inventory = pd.read_csv('Output/2019_rev_vehicle_inventory_modified.csv', dtype='str')

    vehicleCalculationByMode(df, df_rev_inventory, "Enhanced Mobility of Seniors & Individuals with Disabilities  (EMSID)")
    totalCalculation(df, "EMSID")
    vehicleCalculationByMode(df, df_rev_inventory, "Non-Federal Private Funds (NFPE)")
    totalCalculation(df, "NFPE")
    vehicleCalculationByMode(df, df_rev_inventory, "Non-Federal Public Funds (NFPA)")
    totalCalculation(df, "NFPA")
    vehicleCalculationByMode(df, df_rev_inventory, "Other Federal Funds (OF)")
    totalCalculation(df, "OF")
    vehicleCalculationByMode(df, df_rev_inventory, "Rural Area Formula Program  (RAFP)")
    totalCalculation(df, "RAFP")
    vehicleCalculationByMode(df, df_rev_inventory, "Urbanized Area Formula Program (UA)")
    totalCalculation(df, "UA")
    df = clean_names(df)
    df.to_csv('Output/step23_rvi_vehicle_type_by_funding.csv')

def totalCalculation(df, fund):
    for index2, row2, in df.iterrows():
        total = 0
        tdf2 = df.query("ntd_id== @index2")
        total = float(str(row2['number_of_Bus_'+fund.lower()])) \
                + float(str(row2['number_of_Cutaway_'+fund.lower()])) \
                + float(str(row2['number_of_Van_'+fund.lower()])) \
                + float(str(row2['number_of_Minivan_'+fund.lower()])) \
                + float(str(row2['number_of_Automobile_'+fund.lower()])) \
                + float(str(row2['number_of_School Bus_'+fund.lower()])) \
                + float(str(row2['number_of_Over-the-road Bus_'+fund.lower()])) \
                + float(str(row2['number_of_Sports Utility Vehicle_'+fund.lower()])) \
                + float(str(row2['number_of_Aerial Tramway_'+fund.lower()])) \
                + float(str(row2['number_of_Articulated Bus_'+fund.lower()])) \
                + float(str(row2['number_of_Ferryboat_'+fund.lower()])) \
                + float(str(row2['number_of_Streetcar Rail_'+fund.lower()])) \
                + float(str(row2['number_of_Trolleybus_'+fund.lower()])) \
                + float(str(row2['number_of_Light Rail Vehicle_'+fund.lower()])) \
                + float(str(row2['number_of_Commuter Rail Self-Propelled Passenger Car_'+fund.lower()])) \
                + float(str(row2['number_of_Commuter Rail Passenger Coach_'+fund.lower()])) \
                + float(str(row2['number_of_Monorail Vehicle_'+fund.lower()])) \
                + float(str(row2['number_of_Double Decker Bus_'+fund.lower()])) \
                + float(str(row2['number_of_Commuter Rail Locomotive_'+fund.lower()])) \
                + float(str(row2['number_of_Heavy Rail Passenger Car_'+fund.lower()])) \
                + float(str(row2['number_of_Vintage Trolley_'+fund.lower()])) \
                + float(str(row2['number_of_Inclined Plain Vehicle_'+fund.lower()])) \
                + float(str(row2['number_of_Automated Guideway Vehicle_'+fund.lower()])) \
                + float(str(row2['number_of_Cable Car_'+fund.lower()])) \
                + float(str(row2['number_of_Other_'+fund.lower()]))
        df.loc[index2, 'number_of_vehicle_'+fund.lower()+'_total'] = total

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


def vehicle_calculation(df, df_rev_inventory, vehicletype, fund):
    for index, row in df.iterrows():
        sum = 0
        tdf = df_rev_inventory.query("ntd_id== @index and vehicle_type == @vehicletype and funding_source == @fund")
        for openIndex, row in tdf.iterrows():
            if str(row['active_fleet_vehicles']) == 'nan':
                row['active_fleet_vehicles'] = '0'
            sum = sum + int(str(row['active_fleet_vehicles']).replace(',', ''))
        if "EMSID" in fund:
            df.loc[index, 'number_of_' + vehicletype + "_emsid"] = sum
        if "NFPE" in fund:
            df.loc[index, 'number_of_' + vehicletype + "_nfpe"] = sum
        if "NFPA" in fund:
            df.loc[index, 'number_of_' + vehicletype + "_nfpa"] = sum
        if "OF" in fund:
            df.loc[index, 'number_of_' + vehicletype + "_of"] = sum
        if "RAFP" in fund:
            df.loc[index, 'number_of_' + vehicletype + "_rafp"] = sum
        if "UA" in fund:
            df.loc[index, 'number_of_' + vehicletype + "_ua"] = sum

if __name__ == '__main__':
    step23()
    print("Step 23 complete")
