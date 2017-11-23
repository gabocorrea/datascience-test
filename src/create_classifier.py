import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, cross_val_score
import pickle, os

settings_model_filename = 'LinearRegression'
settings_scale = True
settings_convert_bool_to_number = True
settings_crossvalidation_test_size = 0.1
settings_crossvalidation_random_seed = 3
np.set_printoptions(suppress=True)

train_filename = '../data/pd_data_train.csv'
test_filename = '../data/pd_data_test.csv'
selected_columns = 'google_eta,num_products_KG,num_products_UN,picking_speed,dow,on_demand,total_minutes'.split(',')
# :: last_column is the one being predicted
last_column = selected_columns[-1]


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

# do cross_validation
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=settings_crossvalidation_test_size, random_state=settings_crossvalidation_random_seed)

# train classifier
clf = LinearRegression()
clf.fit(X_train, y_train)

# save model to a file
filename_out = ''
for i in range(1000):
    filename_out = 'classifiers/'+str(settings_model_filename) + '{0:0=3d}'.format(i) + '.pickle'
    if os.path.exists(filename_out) == False:
        with open(filename_out, 'wb') as f:
            pickle.dump(clf, f)
        break

print('\n\n\n\n\n___________________________________\n\n\n\n\nClassifier {}:'.format(filename_out))
print("\nscore")
print(clf.score(X_test, y_test))
print("\nexplained_variance")
print(cross_val_score(clf, X_test, y_test, scoring='explained_variance'))
print("\nneg_mean_absolute_error")
print(cross_val_score(clf, X_test, y_test, scoring='neg_mean_absolute_error'))
print("\nneg_mean_squared_error")
print(cross_val_score(clf, X_test, y_test, scoring='neg_mean_squared_error'))
print("\nneg_mean_squared_log_error")
print(cross_val_score(clf, X_test, y_test, scoring='neg_mean_squared_log_error'))
print("\nneg_median_absolute_error")
print(cross_val_score(clf, X_test, y_test, scoring='neg_median_absolute_error'))
print("\nr2")
print(cross_val_score(clf, X_test, y_test, scoring='r2'))



# print(df.head())
# print(df.tail())