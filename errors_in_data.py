import matplotlib.pyplot as plt
import pandas as pd
import io
from google.colab import files


uploaded = files.upload()
for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, 
      length=len(uploaded[fn])))

# name of the upladed file:
fn

# df = pd.read_csv(io.BytesIO(uploaded['RC2017-20.csv']))
df_lc = pd.read_csv(io.BytesIO(uploaded[fn]))
# USE RC2017-20.csv


df_lc = df_lc.rename(columns={'Ком. очки':'Очки',
                              'Толчок':'Толчок ДЦ'})
df_lc = df_lc.drop(columns={'Unnamed: 2',
                            'Unnamed: 12'})
df_lc = df_lc[df_lc['Толчок ДЦ'] != "снят врачом"]
df_lc['Толчок ДЦ'] = pd.to_numeric(df_lc['Толчок ДЦ'])
df_lc['Соб. вес'] = pd.to_numeric(df_lc['Соб. вес'])



uploaded2 = files.upload()
for fn2 in uploaded2.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn2, 
      length=len(uploaded2[fn2])))

# name of the upladed file:
fn2

# df = pd.read_csv(io.BytesIO(uploaded['RC2017-20.csv'])) # USE RC_dv_2017+18+19+20.csv
df_bi = pd.read_csv(io.BytesIO(uploaded2[fn2]))

df_bi = df_bi.drop(columns={'Unnamed: 2',
                            'Unnamed: 17'})
df_bi = df_bi.rename(columns={'Ком. Очки':'Очки',
                              'Сумма       дв-рья':'Сумма дв-рья',
                              'Unnamed: 11':'Рывок (очки)',
                              'Рывок':'Рывок (сумма)'})
df_bi = df_bi[df_bi['Толчок'] != "Cнят врачом"]
df_bi = df_bi[df_bi['Толчок'] != "Снят врачом"]
df_bi = df_bi[df_bi['Соб. вес'] != "снят врачом"]
df_bi = df_bi[df_bi['Сумма дв-рья'] != "снят врачом"]
df_bi['Толчок'] = pd.to_numeric(df_bi['Толчок'])
df_bi['Соб. вес'] = df_bi['Соб. вес'].str.replace(',', '.').astype(float)
df_bi['Соб. вес'] = pd.to_numeric(df_bi['Соб. вес'])
df_bi['Сумма дв-рья'] = pd.to_numeric(df_bi['Сумма дв-рья'])


# merge datasets
df = df_lc.append(df_bi, sort=False)
df['name'] = df['Ф.И.'].apply(lambda x: str.strip(x))
df['ФИО тренера(тренеров)'] = df['ФИО тренера(тренеров)'].astype(str)
df['ФИО тренера(тренеров)'] = df['ФИО тренера(тренеров)'].apply(lambda x: str.strip(x))
df['vk'] = df['в/к'].apply(lambda x: str(x))

#get 85+ category for 2020 
df2020_85p_bi = df999[(df['Год']==2020) & (df['Вид']=='Двоеборье') & (df['в/к']==999)]



fig, ax6 = plt.subplots(1,1, figsize=(10,10))
ax6.scatter(df2020_85p_bi['Соб. вес'], df2020_85p_bi['Сумма дв-рья'], c='b')
ax6.grid(True, c='g', alpha=0.5)
ax6.set_xticks([63,68,73,78,85])
ax6.set_title('ЧР 2020. вк 85+', size=22, c='g')
ax6.set_ylim(0,280)
ax6.plot(74.55,194.5,'ro', marker="o", markersize=12) 

plt.savefig("CR_2020.85+.png", dpi=80)
files.download("CR_2020.85+.png")

