import numpy as np
import pandas as pd


#Bins = np.array([ [10, 5, 2], [3, 2, 2]  ])
#Items = np.array([ [1, 5, 5], [1, 3, 1]  ])

bin_length = float(input("Enter bin length:"))
bin_width = float(input("Enter bin width:"))
bin_height = float(input("Enter bin height:"))
item_length = float(input("Enter item length:"))
item_width = float(input("Enter item width:"))
item_height = float(input("Enter item height:"))

Bins=np.array([[bin_length,bin_width,bin_height]])
Items=np.array([[item_length,item_width,item_height]])


Bins = Bins.repeat(6).reshape((Bins.shape[0], Bins.shape[1], 6))
Items = Items.repeat(6).reshape((Bins.shape[0], Bins.shape[1], 6))


Items[:, :, 0] = Items[:, np.array([0, 1, 2]), 0]
Items[:, :, 1] = Items[:, np.array([0, 2, 1]), 1]
Items[:, :, 2] = Items[:, np.array([1, 0, 2]), 2]
Items[:, :, 3] = Items[:, np.array([1, 2, 0]), 3]
Items[:, :, 4] = Items[:, np.array([2, 0, 1]), 4]
Items[:, :, 5] = Items[:, np.array([2, 1, 0]), 5]

Div = np.floor(Bins / Items)
Div = Div[:, 0] * Div[:, 1] * Div[:, 2]
print('Max number of item slotted under different orientations:')
print (Div)
maxArg = np.argmax(Div, axis=1)
#print (maxArg)

print('Optimum slotting method:')
if maxArg == 0:
    print("Align each packet's length along the container length, each packet's width along the container width, and each packet's height along the container height.")
elif maxArg ==1:
    print("Align each packet's length along the container length, each packet's height along the container width, and each packet's width along the container height.")
elif maxArg ==2:
    print("Align each packet's width along the container length, each packet's length along the container width, and each packet's height along the container height.")
elif maxArg ==3:
    print("Align each packet's width along the container length, each packet's height along the container width, and each packet's length along the container height.")
elif maxArg ==4:
    print("Align each packet's height along the container length, each packet's length along the container width, and each packet's width along the container height.")
elif maxArg ==5:
    print("Align each packet's height along the container length, each packet's width along the container width, and each packet's length along the container height.")





quit()