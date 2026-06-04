import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/event_study_with_ar.csv")

print("\n===== FINDING 1 =====")
print("Overall Average Abnormal Return:")
print(df["Abnormal_Return"].mean())

print("\n===== FINDING 2 =====")

event_summary = (
    df.groupby("Event_Type")
      ["Abnormal_Return"]
      .mean()
      .sort_values()
)
print("Weather events impact:")
print(event_summary)

print("\n===== FINDING 3 =====")

stock_summary = (
    df.groupby("Ticker")
      ["Abnormal_Return"]
      .mean()
      .sort_values()
)
print("Most effected stocks:")
print(stock_summary)

car = pd.read_csv("data/car_results.csv")

print("\n===== FINDING 4 =====")

car_summary = (
    car.groupby("Event_Type")
       ["CAR"]
       .mean()
       .sort_values()
)

print(car_summary)

print("\n===== FINDING 5 =====")

event_window = (
    df.groupby("Relative_Day")
      ["Abnormal_Return"]
      .mean()
)

print(event_window)

event_window.plot()

plt.axvline(x=0, linestyle="--")

plt.title("Average Abnormal Return Around Event Date")
plt.xlabel("Relative Day")
plt.ylabel("Abnormal Return")

plt.show()

print("\n===== FINDING 6 =====")

positive_alpha = (
    df.groupby("Ticker")
      ["Abnormal_Return"]
      .mean()
      .sort_values(ascending=False)
)

print(positive_alpha)