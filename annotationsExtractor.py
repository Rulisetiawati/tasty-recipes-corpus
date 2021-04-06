import pandas as pd
df = pd.read_csv("mturk_results.csv")[['Input.document_url', 'Answer.category.label']]
df["annotator"] = ["first_annotator", "second_annotator", "third_annotator"] * 800
data = df.pivot(index='Input.document_url', columns='annotator', values='Answer.category.label').reset_index()

def most_common(lst):
    return max(set(lst), key=lst.count)

classes = []
for a,b,c, in zip(data['first_annotator'], data['second_annotator'], data['third_annotator']):
    if a!=b and b!=c and c!=a:
        classes.append("None")
    else:
        classes.append(most_common([a,b,c]))
        
data['most_common'] = classes

data.to_csv("mturk_cleaned.csv", index=False)
