import pandas as pd

df = pd.read_csv('/Users/Marcita/forma/uber_reviews_without_reviewid.csv')
print(df.info())
print(df.head())

df_cleaned = df.drop(columns=["userImage"])

df_cleaned.fillna({"reviewCreatedVersion": "Desconhecida"}, inplace= True)
df_cleaned.fillna({"appVersion": "Desconhecida"}, inplace=True)

df_cleaned["score"].value_counts()

df_cleaned["thumbsUpCount"].describe()

df_cleaned["at"] = pd.to_datetime(df_cleaned["at"])
df_cleaned["at"].dt.date.value_counts().sort_index().head()

df_cleaned[["replyContent", "repliedAt"]].dropna().head()

df_cleaned[["score", "thumbsUpCount"]].corr()

import matplotlib.pyplot as plt

print(df_cleaned.columns)

df_cleaned["score"].value_counts().plot(kind="bar", title="Distribuição de Avaliações (SCORE)")

plt.xlabel("Score")
plt.ylabel("Quantidade")
plt.show()

df_cleaned.to_csv("/Users/Marcita/forma/uber_reviews_without_reviewid_cleaned.csv")