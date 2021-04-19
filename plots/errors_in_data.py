import matplotlib.pyplot as plt
import pandas as pd
import prepere_merged_file as pf

df=pf.get_df()


#get 85+ category for 2020 
df2020_85p_bi = df[(df['Год']==2020) & (df['Вид']=='Двоеборье') & (df['в/к']==999)]


fig, ax6 = plt.subplots(1,1, figsize=(10,10))
ax6.scatter(df2020_85p_bi['Соб. вес'], df2020_85p_bi['Сумма дв-рья'], c='b')
ax6.grid(True, c='g', alpha=0.5)
ax6.set_xticks([63,68,73,78,85])
ax6.set_title('ЧР 2020. вк 85+', size=22, c='g')
ax6.set_ylim(0,280)
ax6.plot(74.55,194.5,'ro', marker="o", markersize=12) 

# plt.savefig("/home/aleksei/Dropbox/GiriStat/CR_2020.85+_bi.png", dpi=80)
plt.savefig("../CR_2020.85+_bi.png", dpi=80)




