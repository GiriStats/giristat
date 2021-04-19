import data_processing.prepare_merged_data as perd
import plots.median_mean as mm



df = perd.get_df()

mm.draw_median_and_mean(df, True, 100)