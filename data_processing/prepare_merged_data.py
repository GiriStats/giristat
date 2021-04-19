import pandas as pd


def get_df():
    df_lc = pd.read_csv('source/RC_LC_2017-20.csv')

    df_lc = df_lc.rename(columns={'Ком. очки':'Очки',
                                'Толчок':'Толчок ДЦ'})
    df_lc = df_lc.drop(columns={'Unnamed: 2',
                                'Unnamed: 12'})
    df_lc = df_lc[df_lc['Толчок ДЦ'] != "снят врачом"]
    df_lc['Толчок ДЦ'] = pd.to_numeric(df_lc['Толчок ДЦ'])
    df_lc['Соб. вес'] = pd.to_numeric(df_lc['Соб. вес'])


    df_bi = pd.read_csv('source/RC_BI_2017-20.csv')

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

    df.loc[(df['Год'] == 2017) & (df['vk']=='999'), 'vk'] = "95+"
    df.loc[(df['Год'] != 2017) & (df['vk']=='999'), 'vk'] = "85+"

    return df
