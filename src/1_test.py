import pandas as pd
import numpy as np
from os import path

datapath = "../data/"

filepath_orders = path.join(datapath, 'orders - training.csv')
filepath_products = path.join(datapath, 'order_product.csv')
filepath_shoppers = path.join(datapath, 'shoppers.csv')
filepath_stores = path.join(datapath, 'storebranch.csv')

filepaths_all = [filepath_orders,filepath_products,filepath_shoppers,filepath_stores]
for filepath in filepaths_all:
	print(path.exists(filepath))

for filepath in filepaths_all:
	data = pd.read_csv(filepath)
	print(data.head(3))
	print('\n\n__________________________________________________________________________\n\n')
	#print(data.set_index('order_id').head(3))
	#print(data['rec_vel'])
	#s = pd.Series(data)
