import pandas as pd

df = pd.read_csv("data/event_study_dataset.csv")

df["Abnormal_Return"] = (
    df["Stock_Return"] -
    df["Market_Return"]
)

df.to_csv(
    "data/event_study_with_ar.csv",
    index=False
)
print("Abnormal Returns Calculated")