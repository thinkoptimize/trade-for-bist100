import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from tvDatafeed import TvDatafeed, Interval
import time

username = 'akdag.cagtay@yandex.com'
password = '***.'

tv = TvDatafeed(username, password)

# True Range
def true_range(high, low, close):
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)
    return tr

def rma(series, length):
    return series.ewm(alpha=1/length, adjust=False).mean()

def strateji_uygula(hisse_kodu):

    try:
        df = tv.get_hist(symbol=hisse_kodu, exchange='BIST', interval=Interval.in_daily, n_bars=524)
        if df is None or df.empty:
            return {'Hisse': hisse_kodu, 'Hata': 'Veri bulunamadı'}

        df['EMA19'] = df['close'].ewm(span=19, adjust=False).mean()
        # ADX hesaplamaları
        lenadx, lensig, limadx = 14, 14, 18
        up = df['high'].diff()
        down = -df['low'].diff()
        tr = true_range(df['high'], df['low'], df['close'])
        trur = rma(tr, lenadx)

        plus_dm = np.where((up > down) & (up > 0), up, 0)
        minus_dm = np.where((down > up) & (down > 0), down, 0)

        plus_di = 100 * rma(pd.Series(plus_dm, index=df.index), lenadx) / trur
        minus_di = 100 * rma(pd.Series(minus_dm, index=df.index), lenadx) / trur
        dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di).replace(0, 1)
        adx = rma(dx, lensig)
        weights = np.arange(1, 35)
        df['MA_ADX'] = df['close'].rolling(window=34).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
        colors = []
        for i in range(len(df)):
            if adx.iloc[i] > limadx:
                if plus_di.iloc[i] > minus_di.iloc[i]:
                    colors.append('yeşil')
                elif plus_di.iloc[i] < minus_di.iloc[i]:
                    colors.append('kırmızı')
                else:
                    colors.append('siyah')
            else:
                colors.append('siyah')
        result = pd.DataFrame({
            'Kapanış Tarihi': df.index,
            'Kapanış Fiyatı': df['close'].values,
            'EMA 19': df['EMA19'].values,
            'MA ADX': df['MA_ADX'].values,
            'Renk': colors
        }).dropna()

        signals = []
        for _, row in result.iterrows():
            ema, ma_adx, renk = row['EMA 19'], row['MA ADX'], row['Renk']
            if abs(ema - ma_adx) < 0:
                signals.append('BEKLE')
            elif ema > ma_adx and renk == 'yeşil':
                signals.append('AL')
            elif ema < ma_adx:
                signals.append('SAT')
            else:
                signals.append('BEKLE')
        result['Sinyal'] = signals
        # Backtest
        balance, position = 10000, 0
        entry_price = 0
        for _, row in result.iterrows():
            fiyat, sinyal = row['Kapanış Fiyatı'], row['Sinyal']
            if sinyal == 'AL' and position == 0:
                position = balance / fiyat
                entry_price = fiyat
                balance = 0
            elif sinyal == 'SAT' and position > 0:
                balance = position * fiyat
                position, entry_price = 0, 0
        if position > 0:
            balance = position * result.iloc[-1]['Kapanış Fiyatı']

        final_balance = round(balance, 2)
        net_profit = final_balance - 10000
        roi = round((final_balance / 10000 - 1) * 100, 2)

        return {
            'Hisse': hisse_kodu,
            'Başlangıç Bakiye': 10000,
            'Final Bakiye': final_balance,
            'Net Kar/Zarar': round(net_profit, 2),
            'ROI (%)': roi
        }

    except Exception as e:
        return {'Hisse': hisse_kodu, 'Hata': str(e)}


# Hisse listesi
hisseler = ['FROTO', 'TAVHL', 'AKSA', 'TUPRS', 'YEOTK', 'MIATK', 'BIMAS', 'MGROS', 'NUHCM', 'GOLTS'
            ,'BANVT','GARAN','GRSEL','ISCTR','DOAS','ASTOR','ANSGR','TCELL','AYGAZ','KCHOL','MPARK']




# Tüm sonuçları topla
sonuclar = [strateji_uygula(hisse) for hisse in hisseler]
df_sonuclar = pd.DataFrame(sonuclar)
print(df_sonuclar)
