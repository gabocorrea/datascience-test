import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, ridge, Lasso
from sklearn.svm import LinearSVR, SVR, NuSVR
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import  mean_squared_error, r2_score
import pickle, os, math
import matplotlib.pyplot as plt
from tabulate import tabulate

# columns used from input .csv file
selected_columns = 'google_eta,num_products_KG,num_products_UN,picking_speed,dow,on_demand,total_minutes'.split(',')

# filename of the classifier that is stored with pickle
settings_model_filename = 'LinearRegression'

# normalize all values
settings_scale = False

# should on_demand column be converted to 0 or 1 ?
settings_convert_bool_to_number = False

# test size (in %)
settings_crossvalidation_test_size = 0.3

# random seed for test-train split
settings_crossvalidation_random_seed = 1

# show plots
settings_plot = False

# save a file with the model info
settings_classifier_stats = True

# create a file similar to orders.csv, but with prediccions on it
settings_output_orders_file = True

# :: last_column is the one being predicted
last_column = selected_columns[-1]




train_filename = '../data/pd_data_train.csv'
test_filename = '../data/pd_data_unknown.csv'
predicted_output_filename = 'predictions/predictions.csv'
predicted_output_filename_orders = 'predictions/orders_with_predictions.csv'




# read data from .csv
df = pd.read_csv(train_filename)
df = df[selected_columns]



# convert True and False to 1 and 0
if settings_convert_bool_to_number:
    df['on_demand'] = df['on_demand'].apply(lambda x: 1 if x==True else 0)




# :: set X and y
X = np.array(df.drop(columns=last_column))
if settings_scale:
    X = preprocessing.scale(X)
y = np.array(df[last_column])



# split to train and test parts
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=settings_crossvalidation_test_size, random_state=settings_crossvalidation_random_seed)




# train classifier
clf = LinearRegression()
clf.fit(X_train, y_train)



# test classifier
y_true, y_pred = y_test, clf.predict(X_test)
df_test_pred = pd.DataFrame([], columns=['total_minutes','total_minutes_predicted','diff'])
df_test_pred['total_minutes'] = pd.Series(y_true)
df_test_pred['total_minutes_predicted'] = pd.Series(y_pred)
df_test_pred['diff'] = pd.Series(y_pred) - pd.Series(y_true)



# save model to a file. Auto-generates a new name for each file (No replacing)
filename_out = ''
for i in range(1000):
    filename_out = 'classifiers/'+str(settings_model_filename) + '{0:0=3d}'.format(i) + '.pickle'
    if os.path.exists(filename_out) == False:
        with open(filename_out, 'wb') as f:
            pickle.dump(clf, f)
        


        # Write model info to a file
        if settings_classifier_stats:

            filename_out = 'classifiers/'+str(settings_model_filename) + '{0:0=3d}'.format(i) + '.txt'
            with open(filename_out, 'w') as f:
                
                f.write('Linear Ecuation of the Model:\n')

                L0 = list(zip(df.columns,clf.coef_))
                L0.append( ['constant',str(clf.intercept_)] )
                f.write( tabulate( L0 ) )


                L = [
                    ['r' + u'\u00B2' + ' score', str(clf.score(X_test, y_test)) ] ,
                    ['mean error', str(math.sqrt(  mean_squared_error(y_test, y_pred)  )) ],
                    ['explained_variance', str(sum(cross_val_score(clf, X_test, y_test, scoring='explained_variance')) / 3) ],
                    ['neg_mean_absolute_error', str(sum(cross_val_score(clf, X_test, y_test, scoring='neg_mean_absolute_error')) / 3) ] ,
                    ['neg_mean_squared_error',  str(sum(cross_val_score(clf, X_test, y_test, scoring='neg_mean_squared_error')) / 3)] ,
                    ['neg_mean_squared_log_error', str(sum(cross_val_score(clf, X_test, y_test, scoring='neg_mean_squared_log_error')) / 3) ] ,
                    ['neg_median_absolute_error', str(sum(cross_val_score(clf, X_test, y_test, scoring='neg_median_absolute_error')) / 3) ]
                ]
                f.write('\n\n\n\n\n')
                f.write( tabulate(L, headers=['Metric','Value']))

                f.write('\n\n\n\n\nSome Predictions:\n')
                f.write(str(df_test_pred))

        break





X_test = pd.DataFrame(X_test)
y_test = pd.DataFrame(y_test)





# :: Plot ::
if settings_plot:
    X_test.columns = selected_columns[:-1]
    for col in X_test.columns:
        plt.scatter(X_test[col] ,df_test_pred['total_minutes'], marker='.', s=1)
        plt.scatter(X_test[col] ,df_test_pred['total_minutes_predicted'], marker='x', s=1)
        plt.xlabel(col)
        plt.legend(loc=2)
        plt.show()






# predict values. read data from .csv first
df_prediction_original = pd.read_csv(test_filename)
df_prediction = df_prediction_original[selected_columns]

X_prediction = np.array(df_prediction.drop(columns=last_column))
y_prediction = clf.predict(X_prediction)

df_prediction_original[last_column] = y_prediction
df_prediction_original[last_column] = df_prediction_original[last_column].round(6)









# Crear un archivo similar a pd_data_unknown.csv, con los datos predecidos
if not os.path.exists(predicted_output_filename):
    os.makedirs(predicted_output_filename.split('/')[0])
df_prediction_original.to_csv(predicted_output_filename, index=False)








# Crear un archivo similar al original (orders.csv), con los datos predecidos
if settings_output_orders_file:
    df = pd.read_csv('../data/orders.csv')
    df = pd.DataFrame(df)
    df = pd.merge(df.drop(columns=last_column), df_prediction_original[['order_id',last_column]], how='outer', left_on='order_id', right_on='order_id')
    df.to_csv(predicted_output_filename_orders, index=False)
