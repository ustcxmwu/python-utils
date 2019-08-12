import pandas as pd
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import numpy as np
from sklearn.svm import SVR



pd.set_option('display.max_colwidth', 200)


def read_spy():
    start_date = pd.to_datetime('2010-01-01')
    stop_date = pd.to_datetime('2019-01-01')
    spy = pdr.data.get_data_yahoo('SPY', start_date, stop_date)
    return spy


if __name__ == '__main__':
    sp = read_spy()
    for i in range(1, 21, 1):
        sp.loc[:, 'Close Minus ' + str(i)] = sp['Close'].shift(i)
    sp20 = sp[[x for x in sp.columns if 'Close Minus' in x or x == 'Close']].iloc[20:,]
    print(sp20)
    sp20 = sp20.iloc[:, ::-1]
    print(sp20)
    clf = SVR(kernel='linear')
    X_train = sp20[:-1000]
    y_train = sp20['Close'].shift(-1)[:-1000]
    X_test = sp20[-1000:]
    y_test = sp20['Close'].shift(-1)[-1000:]

    model = clf.fit(X_train, y_train)
    preds = model.predict(X_test)

    tf = pd.DataFrame(list(zip(y_test, preds)), columns=['Next Day Close', 'Predicted Next Close'], index=y_test.index)
    print(tf)