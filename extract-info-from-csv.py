import pandas as pd

table = pd.read_csv("requests.csv")
colunas = [
    "Name",
    "Request Count",
    "Failure Count",
    "Average Response Time",
    "Max Response Time",
]

df = table[colunas]
df_agg = df.groupby("Name", as_index=False).agg(
    {
        "Request Count": "sum",
        "Failure Count": "sum",
        "Average Response Time": "mean",
        "Max Response Time": "max",
    }
)

print(df_agg)
