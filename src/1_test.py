import pandas as pd
import numpy as np
from os import path
from datetime import datetime
from collections import Counter

time_start = datetime.now()


#cuantas lineas de la tabla vamos a procesar. (None para usar toda la tabla)
FIRST_N_ROWS = 16

#archivos utilizados
datapath = "../data/"

filepath_orders = path.join(datapath, 'orders - training.csv')
filepath_products = path.join(datapath, 'order_product.csv')
filepath_shoppers = path.join(datapath, 'shoppers.csv')
filepath_stores = path.join(datapath, 'storebranch.csv')

filepaths_all = [filepath_orders,filepath_products,filepath_shoppers,filepath_stores]








#contar productos solicitados de una orden
data_orders = pd.read_csv(filepath_orders)
data_products = pd.read_csv(filepath_products)
data_shoppers = pd.read_csv(filepath_shoppers)
data_stores = pd.read_csv(filepath_stores)








#calcular numero de productos de tipo UN y KG, y agregarlos a la tabla principal
num_products_table = pd.DataFrame([], columns=['order_id', 'num_products_UN', 'num_products_KG'])
for row in data_orders['order_id'].iloc[:FIRST_N_ROWS]:
    product_count_UN = len(data_products.query('order_id==@row & buy_unit=="UN"')) #unidades
    product_count_KG = len(data_products.query('order_id==@row & buy_unit=="KG"')) #kilogramos
    d = {
        'order_id': [row],
        'num_products_UN': [product_count_UN],
        'num_products_KG': [product_count_KG]
    }
    num_products_table = num_products_table.append( pd.DataFrame(d) )

joined_table = pd.merge(data_orders, num_products_table, left_on='order_id', right_on='order_id')
del(data_orders)
data_orders = joined_table





#obtener seniority y picking_speed del shopper asociado a una orden. agregarlos a la tabla principal
data_orders = pd.merge(data_orders, data_shoppers[['shopper_id','seniority','picking_speed']], left_on='picker_id', right_on='shopper_id', how='left')





#delete unused columns
data_orders = data_orders.loc[:, data_orders.columns != 'shopper_id']
data_orders = data_orders.loc[:, data_orders.columns != 'picker_id']
data_orders = data_orders.loc[:, data_orders.columns != 'driver_id']
data_orders = data_orders.loc[:, data_orders.columns != 'promised_time']
data_orders = data_orders.loc[:, data_orders.columns != 'actual_time']





#obtener lat_store y lng_store de la store asociada a una orden. agregarlos a la tabla principal
data_stores.columns = ['store_branch_id','store','lat_store','lng_store']
data_orders = pd.merge(data_orders, data_stores, left_on='store_branch_id', right_on='store_branch_id')





#delete unused columns
data_orders = data_orders.loc[:, data_orders.columns != 'store']
data_orders = data_orders.loc[:, data_orders.columns != 'store_branch_id']



print(data_orders)











#mostrar duración de ejecucion del programa
time = datetime.now() - time_start
print("\toperacion tomó " + str(time) + " h:mm:ss:ms")


















