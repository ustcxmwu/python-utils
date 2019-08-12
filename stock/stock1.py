import pandas as pd
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import numpy as np


pd.set_option('display.max_colwidth', 200)


if __name__ == '__main__':
    start_date = pd.to_datetime('2010-01-01')
    stop_date = pd.to_datetime('2019-01-01')

    spy = pdr.data.get_data_yahoo('SPY', start_date, stop_date)
    print(spy)
    spy_c = spy['Close']
    fig, x = plt.subplots(figsize=(15, 10))
    spy_c.plot(color='k')
    plt.title('SPY', fontsize=20)
    # plt.show()

    first_open = spy['Open'].iloc[0]
    print(first_open)
    last_close = spy['Close'].iloc[-1]
    print(last_close)

    spy['Daily Change'] = pd.Series(spy['Close'] - spy['Open'])
    print(spy['Daily Change'])
    print(spy['Daily Change'].sum())

    print(np.std(spy['Daily Change']))

    spy['Overnight Change'] = pd.Series(spy['Open'] - spy['Close'].shift(1))
    print(np.std(spy['Overnight Change']))