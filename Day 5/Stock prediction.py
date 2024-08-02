import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, r2_score
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.callbacks import EarlyStopping

pd.set_option('display.float_format', lambda x: '%.3f' % x)

filename = 'TESLA.csv'
stock = pd.read_csv(filename)
print(stock.head())

stock['Adj Close'].plot()
plt.title('Adjusted Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.show()

output_var = pd.DataFrame(stock['Adj Close'])
features = ['Open', 'High', 'Low', 'Volume']

if not all(col in stock.columns for col in features):
    raise ValueError("One or more feature columns are missing from the dataset")

scaler = MinMaxScaler()
feature_transform = scaler.fit_transform(stock[features])
feature_transform = pd.DataFrame(columns=features, data=feature_transform, index=stock.index)
print(feature_transform.head())

timesplit = TimeSeriesSplit(n_splits=5)
for train_index, test_index in timesplit.split(feature_transform):
    X_train, X_test = feature_transform.iloc[train_index], feature_transform.iloc[test_index]
    y_train, y_test = output_var.iloc[train_index].values.ravel(), output_var.iloc[test_index].values.ravel()

    y_scaler = MinMaxScaler()
    y_train_scaled = y_scaler.fit_transform(y_train.reshape(-1, 1)).ravel()
    y_test_scaled = y_scaler.transform(y_test.reshape(-1, 1)).ravel()

    X_train = np.array(X_train).reshape(X_train.shape[0], 1, X_train.shape[1])
    X_test = np.array(X_test).reshape(X_test.shape[0], 1, X_test.shape[1])

    lstm = Sequential()
    lstm.add(LSTM(32, input_shape=(1, X_train.shape[2]), activation='relu', return_sequences=False))
    lstm.add(Dense(1))
    lstm.compile(loss='mean_squared_error', optimizer='adam')

    early_stopping = EarlyStopping(monitor='val_loss', patience=5)

    history = lstm.fit(X_train, y_train_scaled, epochs=200, batch_size=4, verbose=1, shuffle=True,
                       validation_data=(X_test, y_test_scaled), callbacks=[early_stopping])

    y_pred_scaled = lstm.predict(X_test)
    y_pred = y_scaler.inverse_transform(y_pred_scaled)

    plt.plot(y_test, label='True Value')
    plt.plot(y_pred, label='LSTM Value')
    plt.title("Prediction by LSTM")
    plt.xlabel('Time Scale')
    plt.ylabel('Scaled USD')
    plt.legend()
    plt.show()

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"MSE: {mse:.3f}, R-squared: {r2:.3f}")
