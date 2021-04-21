import matplotlib.pyplot as plt

def draw_median_and_mean(df, discipline, year, save, dpi):

    df_year = df[df['Год']==year]

    df_year_63 = df_year[df_year['в/к']==63]
    df_year_68 = df_year[df_year['в/к']==68]
    df_year_73 = df_year[df_year['в/к']==73]
    df_year_85 = df_year[df_year['в/к']==85]
    df_year_999 = df_year[df_year['в/к']==999]

    medians_year=[]

    medians_year.append(df_year_63[discipline].median())
    medians_year.append(df_year_68[discipline].median())
    medians_year.append(df_year_73[discipline].median())
    medians_year.append(df_year_85[discipline].median())
    medians_year.append(df_year_999[discipline].median())

    if year == 2017:
        df_year_78 = df_year[df_year['в/к']==78]
        df_year_95 = df_year[df_year['в/к']==95]

        medians_year.insert(3, df_year_78[discipline].median())
        medians_year.insert(5, df_year_95[discipline].median())

        w_categories=[63, 68, 73, 78, 85, 95, 100]
        w_categories_str=['63','68','73','78','85','95','95+']
    else:
        w_categories=[63,68,73,85,100]
        w_categories_str=['63','68','73','85','85+']


    if discipline=='Сумма дв-рья':
        ylim=(0,260)
    elif discipline=='Толчок ДЦ':
        ylim=(20,90)
    else:
        ylim=(0,300)
   
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5.5))

    ax1.plot(w_categories, medians_year, 'r')
    ax1.plot(w_categories, medians_year, 'ro', label='медиана')
    ax1.set_xticks(w_categories)
    ax1.set_xlabel('в/к')
    ax1.set_yticks(medians_year)
    ax1.grid()
    ax1.legend(loc='upper left')

    ax2.plot(w_categories_str, medians_year, color='r')
    ax2.plot(w_categories_str, medians_year, 'ro')
    ax2.set_xlabel('в/к')
    ax2.set_ylim(ylim)
    ax2.grid()


    plt.suptitle('Медианы для каждой в/к. ' + discipline + '. ЧР ' + str(year), 
                size=22, 
                color='g', y=1)

    fig.tight_layout(rect=[0, 0, 1, 0.95])


    switcher = {
        'Толчок ДЦ':'LC',
        'Сумма дв-рья':'BI',
        'Толчок':'Jerk',
        'Рывок (сумма)':'Snatch_Summ'
    }

    print(switcher.get(discipline, 'UN'))

    filename='../Median_catagories_' + switcher.get(discipline, 'UN') + '_CR_'  + str(year)  + '.png'

    if save:
        plt.savefig(filename, dpi=dpi)
        
    plt.show()