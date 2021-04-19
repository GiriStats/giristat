import matplotlib.pyplot as plt
import prepere_merged_file as pf

df=pf.get_df()

df_lc = df[df['Вид'] == 'ДЦ']
df_bi = df[df['Вид'] == 'Двоеборье']


fig, (ax1,ax2) = plt.subplots(1,2, figsize=(20,10))

ax1.scatter(x=df_lc['Соб. вес'], y=df_lc['Толчок ДЦ'])
ax1.set_yticks([20,30,40,45,50,55,60,65,70,75,80,85,90,95])
ax1.set_xticks([63,68,73,78,85,95])
ax1.grid(color = 'g', linewidth=0.5, alpha=0.5)
ax1.yaxis.grid(False)
ax1.set_title("Вес vs Результат ДЦ. Чемпионаты России 2017-2020", size=22, color='g')
ax1.set_xlim(60,110)
ax1.set_ylim(25)

for tick in ax1.xaxis.get_major_ticks():
                tick.label.set_fontsize(15) 

ax2.scatter(x=df_bi['Соб. вес'], y=df_bi['Сумма дв-рья'])
ax2.set_yticks([80,100,120,140, 160, 180, 200, 220, 240, 260, 275])
ax2.set_xticks([63,68,73,78,85,95])
ax2.grid(color = 'g', linewidth=0.5, alpha=0.5)
ax2.yaxis.grid(False)
ax2.set_title('Вес vs Сумма двоеборья. Чемпионаты России 2017-2020', size=22, color='g')
ax2.set_xlim(60,110)
ax2.set_ylim(65)

for tick in ax2.xaxis.get_major_ticks():
                tick.label.set_fontsize(15) 

plt.tight_layout()

title='../Weight _vs_result_RC17-20.png'
plt.savefig(title, dpi=80)