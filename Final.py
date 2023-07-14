import pandas as pd, pathlib as pb, numpy , matplotlib.pyplot as plt
data = pd.read_csv("DOB_Permit_Issuance.csv")

borough = {}

for index in range(0,len(data)):
        if data['BOROUGH'][index] in borough:
            borough[data['BOROUGH'][index]] += 1
        else:
            borough[data['BOROUGH'][index]] = 1
borough_list = []
borough_count = []
for key, value in borough.items():
    print(f"There were {value} permits given out in {key}.")
    borough_list.append(key)
    borough_count.append(value)
    
plt.pie(borough_count, labels=borough_list,autopct='%1.1f%%')
plt.show()


job_type = {}

for index in range(0,len(data)):
        if data['Job Type'][index] in job_type:
            job_type[data['Job Type'][index]] += 1
        else:
            job_type[data['Job Type'][index]] = 1
job_list = []
job_count = []
for key, value in job_type.items():
    print(f"There were {value} {key} permits given out.")
    job_list.append(key)
    job_count.append(value)

plt.pie(job_count, labels=job_list,autopct='%1.1f%%')
plt.show()


bldg_type = {}

for index in range(0,len(data)):
        if numpy.isnan(data['Bldg Type'][index]):
             pass
        elif data['Bldg Type'][index] in bldg_type:
            bldg_type[data['Bldg Type'][index]] += 1
        else:
            bldg_type[data['Bldg Type'][index]] = 1
bldg_list = []
bldg_count = []
for key, value in bldg_type.items():
    print(f"There were {value} {key} family building permits given out.")
    bldg_list.append(key)
    bldg_count.append(value)

plt.pie(bldg_count, labels=bldg_list,autopct='%1.1f%%')
plt.show()


residential = {}

for index in range(0,len(data)):
        if data['Residential'][index] in residential:
            residential[data['Residential'][index]] += 1
        else:
            residential[data['Residential'][index]] = 0
residential_list = []
residential_count = []

for key, value in residential.items():
    print(f'''{value} of 3,946,358 total permits were {key}, residential.''')
    residential_list.append(key)
    residential_count.append(value)
plt.pie(residential_count, labels=residential_list,autopct='%1.1f%%')
plt.show()


buisness_type = {}

for index in range(0,len(data)):
        if data['''Owner's Business Type'''][index] in buisness_type:
            buisness_type[data['''Owner's Business Type'''][index]] += 1
        else:
            buisness_type[data['''Owner's Business Type'''][index]] = 1
buisness_type_list = []
buisness_type_count = []
for key, value in buisness_type.items():
    print(f"There are {value} building permits given out to {key} buisness types.")
    buisness_type_list.append(key)
    buisness_type_count.append(value)

plt.pie(buisness_type_count, labels=buisness_type_list,autopct='%1.1f%%')
plt.show()



import folium, math
from folium.plugins import HeatMap

building_data_nyc = pd.read_csv("DOB_Permit_Issuance.csv")
building_data_nyc.dropna()

avg_lat = building_data_nyc["LATITUDE"].mean()
avg_lon = building_data_nyc["LONGITUDE"].mean()

map = folium.Map(location=[avg_lat, avg_lon], zoom_start=10.5)

heat_data = []
for index, row in building_data_nyc.iterrows():
    individual_data_location = []
    if math.isnan(row["LATITUDE"]) == False:
        individual_data_location.append(row["LATITUDE"])
        individual_data_location.append(row["LONGITUDE"])
        heat_data.append(individual_data_location)

HeatMap(heat_data).add_to(map)
map.save("heatmaapp.html")






