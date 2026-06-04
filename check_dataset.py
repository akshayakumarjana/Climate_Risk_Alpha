import pandas as pd

df = pd.read_csv("data/event_study_dataset.csv")

print(df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nEvent Type Counts:")
print(df["Event_Type"].value_counts())