import pandas as pd

df = pd.read_csv(
    "data/event_study_with_ar.csv"
)

car = (
    df.groupby(
        [
            "Event_Date",
            "Event_Type",
            "Ticker"
        ]
    )["Abnormal_Return"]
    .sum()
    .reset_index()
)

car.rename(
    columns={
        "Abnormal_Return": "CAR"
    },
    inplace=True
)

car.to_csv(
    "data/car_results.csv",
    index=False
)

print(car.head())