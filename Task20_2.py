import pandas as pd

dct = {'Кол-во_январь': [10, 20, 30, 40, 50],
       'Кол-во_февраль': [15, 'нет', 35, 45, 55]}

df = pd.DataFrame(dct)
total = 0
for i in df.index:
  for j in df.columns:
      if df.loc[i, j].isdigit():
          total += df.loc[i, j]

print(total)


