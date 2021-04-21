import data_processing.prepare_merged_data as perd
import plots.median_mean as mm



df = perd.get_df()


mm.draw_median_and_mean(df, discipline='Сумма дв-рья', year=2020,  save=False, dpi=100)

# mm.draw_median_and_mean(df, discipline='Толчок', year=2020,  save=False, dpi=100)

# mm.draw_median_and_mean(df, discipline='Рывок (сумма)', year=2020,  save=False, dpi=100)

