import pandas as pd

# Load dataset with abnormal returns
df = pd.read_csv("data/event_study_with_ar.csv")

# Average abnormal return by event type
summary = (
    df.groupby("Event_Type")["Abnormal_Return"]
      .agg(["mean", "min", "max", "count"])
      .sort_values("mean")
)

print("\n===== EVENT TYPE ANALYSIS =====\n")
print(summary)

# Save results
summary.to_csv(
    "data/event_type_summary.csv"
)

print("\nSummary saved successfully.")