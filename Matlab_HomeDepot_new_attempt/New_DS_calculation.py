import numpy as np
import pandas as pd

pick = pd.read_csv('Pick_new.csv')
#Remove negative DS
pick = pick[pick['DS'] >= 0]



pick["new_IV"] = pick["UNIT VOLUME"]*pick["New_MAX"]
pick["new_DS"] = pick["LV"] - pick["new_IV"]

new_DS = pick["LV"].sum() - pick["new_IV"].sum()

DS = pick["LV"].sum() - pick["IV"].sum()




print(DS)
print(new_DS)

print((DS-new_DS)/DS)