import pandas as pd
import lxml
import os
print(lxml.__version__)

url1='https://en.wikipedia.org/wiki/List_of_ethnic_slurs'
tables = pd.read_html(url1)
first_26_tables = tables[:26]

combined_df = pd.concat(first_26_tables, ignore_index=True)
combined_df_clean = combined_df.dropna()
first_col_df = combined_df_clean.iloc[:, :1]

#print(first_col_df)

url2='http://www.rsdb.org/full'
tables2=pd.read_html(url2,encoding='latin1')
df2 = tables2[0]
second_col_df = df2.iloc[:, :1]

combined_columns = pd.concat([first_col_df, second_col_df], axis=1)
csv_filename = 'combined_table.csv'
combined_columns.to_csv(csv_filename, index=False)

df_pandas = pd.read_csv("combined_table.csv")
df_combined2 = pd.DataFrame({"Term": pd.concat([df_pandas["Term"], df_pandas["Slur"]], ignore_index=True)})
df_combined2_clean = df_combined2.dropna()
df_combined2_clean.to_csv("output.csv", index=False)

# third url are for acronyms, numbers, then later on is phrases

url3='https://en.wikipedia.org/wiki/List_of_symbols_designated_by_the_Anti-Defamation_League_as_hate_symbols'

tables3= pd.read_html(url3)
first_3= tables3[:3]

for i, df in enumerate(first_3, start=1):
    # Create a filename. For example: table_1.csv, table_2.csv, etc.
    df_first_col = df.iloc[:, :1]

    filename = f'table_{i}.csv'
    df_first_col.to_csv(filename, index=False)



