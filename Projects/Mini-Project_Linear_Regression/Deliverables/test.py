from dataprep.eda import plot
import pandas as pd
df = pd.read_csv('rick_diamonds_new.csv')
plot(df)