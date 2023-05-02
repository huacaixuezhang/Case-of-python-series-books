import json

filename='data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)
#将jeson对象存储于文件中
# readable_file='data/readable_eq_data.json'
# with open(readable_file,'w') as f:
#     json.dump(all_eq_data,f,indent=4)

all_eq_dicts=all_eq_data['features']
mags,titles,lons,lats=[],[],[],[]

for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lats.append(lat)
    lons.append(lon)


