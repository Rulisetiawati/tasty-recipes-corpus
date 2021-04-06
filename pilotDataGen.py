import pandas as pd
import json

with open("docs.json", "r") as f:
    file = json.load(f)
df = pd.DataFrame(file['docs'][:10])

df["ingredients"] = df['ingredients'].apply(lambda x : " ".join(x))
df["preparation"] = df['preparation'].apply(lambda x : " ".join(x))

df.to_csv("pilot_study.csv", encoding="utf-8", index=False)