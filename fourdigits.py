import pandas as pd
import numpy as np
import time

t0 = time.time()
number_array = np.arange(1101,2000)
df = pd.read_html("http://numbering.nbtc.go.th/searchnum/map4digits/show4digits.php?number=1100")[0]
for number in number_array:
    url = f"http://numbering.nbtc.go.th/searchnum/map4digits/show4digits.php?number={str(number)}"
    try:
        df_unit = pd.read_html(url)[0]
        df = df.append(df_unit)
    except:
        pass
t1 = time.time()
print(f"Processing time is {t1-t0}")
df = df[df['หน่วยงาน'].notna()]
df.to_csv("4_digit.csv")