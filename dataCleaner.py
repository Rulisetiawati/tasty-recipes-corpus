import pandas as pd
import json

with open("recipies_docs_new.json", "r") as f:
    file = json.load(f)
df = pd.DataFrame(file['docs'][:1600])

df["ingredients"] = df['ingredients'].apply(lambda x : " ".join(x))
df["preparation"] = df['preparation'].apply(lambda x : " ".join(x))

df['document_url'] = df['title']
del df['title']

df = df.copy().astype(str).apply(lambda x: x.str.encode('ascii', 'ignore').str.decode('ascii'))

df.to_csv("recipies_1600_docs.csv", encoding="utf-8",index=False)
