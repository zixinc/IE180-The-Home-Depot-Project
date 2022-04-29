import pandas as pd
pick = pd.read_csv('THD Tracy DFC - Pick Locations.csv')
pick = pick.dropna(subset=['SKU', 'LOCATION_TYPE'])
pick["LV"] = pick["LOC WIDTH"]*pick["LOC LENGTH"]*pick["LOC HEIGHT"]
pick["IV"] = pick["UNIT VOLUME"]*pick["CURR MAX"]
pick["DS"] = pick["LV"] - pick["IV"]
DS = pick["LV"].sum() - pick["IV"].sum()

# Just trying with top 10 rows of dataset
pick_first_10=pick.iloc[0:10]
num_of_rows=len(pick_first_10.index)




from py3dbp import Packer, Bin, Item

packer = Packer()

for i in range(num_of_rows):
    packer.add_bin(Bin(pick_first_10.iloc[i,4], pick_first_10.iloc[i,7], pick_first_10.iloc[i,8], pick_first_10.iloc[i,9], 9999))
    for j in range(int(pick_first_10.iloc[i,11])):
        packer.add_item(Item(pick_first_10.iloc[i,12], pick_first_10.iloc[i,14], pick_first_10.iloc[i,15], pick_first_10.iloc[i,16], pick_first_10.iloc[i,17]))


packer.pack()
total_fitted_item=0
for b in packer.bins:
    total_fitted_item+=len(b.items)
print(total_fitted_item)'''




for b in packer.bins:
    print(":::::::::::", b.string())

    print("FITTED ITEMS:")
    for item in b.items:
        print("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())
