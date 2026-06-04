import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/event_study_with_ar.csv")

avg_returns = (
    df.groupby("Event_Type")
      ["Abnormal_Return"]
      .mean()
      .sort_values()
)

plt.figure(figsize=(8,5))

avg_returns.plot(kind="bar")

plt.title(
    "Average Abnormal Return by Event Type"
)

plt.ylabel(
    "Average Abnormal Return"
)

plt.tight_layout()

plt.show()