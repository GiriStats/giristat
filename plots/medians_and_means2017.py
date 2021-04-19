import matplotlib.pyplot as plt
PACKAGE_PARENT = '..'
from prepere_merged_file import get_df 

df=pf.get_df()

df2017 = df[df['Год']==2017]

df2017_63 = df2017[df2017['в/к']==63]
df2017_68 = df2017[df2017['в/к']==68]
df2017_73 = df2017[df2017['в/к']==73]
df2017_78 = df2017[df2017['в/к']==78]
df2017_85 = df2017[df2017['в/к']==85]
df2017_95 = df2017[df2017['в/к']==95]
df2017_95p = df2017[df2017['в/к']==999]

median_2017_63 = df2017_63['Толчок ДЦ'].median()
mean_2017_63 = df2017_63['Толчок ДЦ'].mean()

median_2017_68 = df2017_68['Толчок ДЦ'].median()
mean_2017_68 = df2017_68['Толчок ДЦ'].mean()

median_2017_73 = df2017_73['Толчок ДЦ'].median()
mean_2017_73 = df2017_73['Толчок ДЦ'].mean()

median_2017_78 = df2017_78['Толчок ДЦ'].median()
mean_2017_78 = df2017_78['Толчок ДЦ'].mean()

median_2017_85 = df2017_85['Толчок ДЦ'].median()
mean_2017_85 = df2017_85['Толчок ДЦ'].mean()

median_2017_95 = df2017_95['Толчок ДЦ'].median()
mean_2017_95 = df2017_95['Толчок ДЦ'].mean()

median_2017_999 = df2017_95p['Толчок ДЦ'].median()
mean_2017_999 = df2017_95p['Толчок ДЦ'].mean()

medians2017 = [median_2017_63, median_2017_68, median_2017_73, median_2017_78, median_2017_85, median_2017_95, median_2017_999]
means2017 = [mean_2017_63, mean_2017_68, mean_2017_73, mean_2017_78, mean_2017_85, mean_2017_95, mean_2017_999]


w_categories=[63, 68, 73, 78, 85, 95, 100]

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5.5))

ax1.plot(w_categories, medians2017, 'r')
ax1.plot(w_categories, medians2017, 'ro', label='медиана')

ax1.plot(w_categories, means2017, 'b' )
ax1.plot(w_categories, means2017, 'bo', label='среднее')

ax1.set_xticks(w_categories)
ax1.set_xlabel('в/к')
ax1.set_yticks(medians2017)
ax1.grid()
ax1.legend(loc='upper left')

ax2.plot(['63','68','73','78','85','95','95+'], medians2017, color='r')
ax2.plot(['63','68','73','78','85','95','95+'], medians2017, 'ro')
ax2.set_xlabel('в/к')
ax2.set_ylim(20,90)
ax2.grid()


plt.suptitle('Медианные и средние значения в категориях. ДЦ.ЧР 2017', 
             size=22, 
             color='g', y=1)

fig.tight_layout(rect=[0, 0, 1, 0.95])

filename='../Median_and_mean_CR_LC_2017.png'
plt.savefig(filename, dpi=80)
