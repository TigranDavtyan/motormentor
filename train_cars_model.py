import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBRegressor
import pickle
import json
import logging

from collections import Counter

logger = logging.getLogger('listamscraper')
logger.setLevel(logging.INFO)

# create file handler
fh = logging.FileHandler('listamscraper.log','a', 'utf-8')

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - MODEL - %(message)s ')
fh.setFormatter(formatter)

# add file handler to logger
logger.addHandler(fh)

logger.info('Loading data...')
#LOAD
data = pd.read_csv('ForSale/Cars/listings.csv')

data = data[data['cleared_customs'] == 'yes']
data.drop('cleared_customs',axis=1,inplace=True)

data['gas_equipment'].fillna('no', inplace=True)

data = data[['itemid', 'car_brand', 'model', 'body_type', 'year', 'engine_type',
       'engine_size', 'transmission', 'drive_type', 'mileage', 'condition',
       'gas_equipment', 'steering_wheel', 'exterior_color',
       'headlights', 'interior_color', 'interior_material', 'sunroof',
       'wheel_size', 'dollar_price']]

# data.set_index('itemid',inplace=True)
data.dropna(inplace=True)

#PREPROCESS
car_brand_counts = data['car_brand'].value_counts()
model_counts = data['model'].value_counts()

car_brand_threshold = 0.001 * len(data)
model_threshold = 0.001 * len(data)
logger.info(f'Brand threshold {car_brand_threshold}')
logger.info(f'Model threshold {model_threshold}')

rare_brands = car_brand_counts[car_brand_counts < car_brand_threshold].index.tolist()
rare_models = model_counts[model_counts < model_threshold].index.tolist()

data['car_brand'] = data['car_brand'].apply(lambda x: 'Other' if x in rare_brands else x)
data['model'] = data['model'].apply(lambda x: 'Other' if x in rare_models else x)

categorical_cols = ['car_brand','model', 'body_type', 'engine_type', 'transmission', 'drive_type',
                    'condition', 'gas_equipment', 'steering_wheel',
                    'exterior_color', 'headlights', 'interior_color', 'interior_material', 'sunroof']

onehot_encoder = OneHotEncoder(drop='first')
onehot_encoder.fit(data[categorical_cols])
data_encoded = onehot_encoder.transform(data[categorical_cols]).toarray()
data_encoded = pd.DataFrame(data_encoded, columns=onehot_encoder.get_feature_names_out(), index = data.index)
data_encoded = pd.concat([data[['itemid', 'year', 'engine_size', 'mileage', 'wheel_size','dollar_price']],data_encoded], axis=1)
data_encoded.set_index('itemid', inplace=True)

with open('trained_model/encoder.pkl', 'wb') as file:
    pickle.dump(onehot_encoder, file)


#Remove outliers round 1
# Calculate the IQR
Q1 = data_encoded['dollar_price'].quantile(0.25)
Q3 = data_encoded['dollar_price'].quantile(0.97)
IQR = Q3 - Q1

# Define the lower and upper bounds for outliers
lower_bound = 500
upper_bound = Q3 + 1.5 * IQR
logger.info(f'Price bounds [{int(lower_bound)}, {int(upper_bound)}]')

# Remove outliers
data_encoded = data_encoded[(data_encoded['dollar_price'] >= lower_bound) & (data_encoded['dollar_price'] <= upper_bound)]

logger.info('Starting ROUND 1 train')
logger.info(f'    Whole data length {len(data_encoded)}')
#ROUND 1 TRAIN MODEL
X = data_encoded.drop('dollar_price', axis=1)
y = data_encoded['dollar_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Create the XGBoost regressor model
xgb_model = XGBRegressor(n_estimators = 100, colsample_bytree = 1, max_depth = 6)# colsample_bylevel = 0.5, colsample_bynode = 0.5,
xgb_model.fit(X_train, y_train)

#Evaluate
y_pred = xgb_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
logger.info(f"    TEST:  Mean Absolute Error: {mae}")

train_y_pred = xgb_model.predict(X_train)
mae = mean_absolute_error(y_train, train_y_pred)
logger.info(f"    TRAIN: Mean Absolute Error: {mae}")


pred = xgb_model.predict(data_encoded.drop('dollar_price',axis=1))
data_encoded['score'] = data_encoded['dollar_price'] - pred

low_score = data_encoded.score.quantile(0.03)
high_score = data_encoded.score.quantile(0.97)

data_length = len(data_encoded)
data_encoded = data_encoded[(data_encoded.score > low_score) & (data_encoded.score < high_score)]
logger.info(f'    Removed {data_length - len(data_encoded)} outliers based on score')


#ROUND 2 TRAIN MODEL
logger.info('Starting ROUND 2 train')
logger.info(f'    Whole data length {len(data_encoded)}')

data_encoded.drop('score', axis = 1, inplace=True)

X = data_encoded.drop('dollar_price', axis=1)
y = data_encoded['dollar_price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Create the XGBoost regressor model
xgb_model = XGBRegressor(n_estimators = 100, colsample_bytree = 1, max_depth = 6)# colsample_bylevel = 0.5, colsample_bynode = 0.5,
xgb_model.fit(X_train, y_train)

#Evaluate
y_pred = xgb_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
logger.info(f"    TEST:  Mean Absolute Error: {mae}")

train_y_pred = xgb_model.predict(X_train)
mae = mean_absolute_error(y_train, train_y_pred)
logger.info(f"    TRAIN: Mean Absolute Error: {mae}")

pred = xgb_model.predict(data_encoded.drop('dollar_price',axis=1))
data_encoded['score'] = data_encoded['dollar_price'] - pred

logger.info('Saving model...')
# Save the model to a file
with open('trained_model/xgb_model.pkl', 'wb') as file:
    pickle.dump(xgb_model, file)


# Dictionary to store the unique values
unique_values = {}

brands = list(data['car_brand'].unique())

unique_values['brands'] = {}
for brand in brands:
    value_counts = Counter(data[data.car_brand == brand]['model'])
    sorted_values = sorted(value_counts, key=value_counts.get, reverse=True)
    unique_values['brands'][brand] = sorted_values

# Iterate over the categorical columns
for column in categorical_cols:
    if column != 'car_brand':
        value_counts = Counter(data[column])
        sorted_values = sorted(value_counts, key=value_counts.get, reverse=True)
        unique_values[column] = sorted_values

# Save the dictionary to a JSON file
with open('trained_model/categorical.json', 'w') as file:
    json.dump(unique_values, file)

logging.info('Finished model training!')