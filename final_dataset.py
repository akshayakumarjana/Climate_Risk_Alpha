import pandas as pd
import glob
import os

# =====================================
# STEP 1 : LOAD WEATHER EVENTS
# =====================================

weather_files = glob.glob(
    "data/raw/weather/StormEvents_details-ftp_v1.0_d*.csv"
)

weather_list = []

for file in weather_files:

    try:
        df = pd.read_csv(file, low_memory=False)

        df = df[[
            "BEGIN_DATE_TIME",
            "EVENT_TYPE",
            "STATE"
        ]]

        weather_list.append(df)

    except Exception as e:
        print(f"Error reading {file}: {e}")

weather = pd.concat(weather_list)

weather["BEGIN_DATE_TIME"] = pd.to_datetime(
    weather["BEGIN_DATE_TIME"],
    format="%d-%b-%y %H:%M:%S",
    errors="coerce"
)

weather = weather.dropna()

# Keep only major events

major_events = [
    "Hurricane",
    "Tropical Storm",
    "Flood",
    "Flash Flood",
    "Wildfire",
    "Winter Storm"
]

weather = weather[
    weather["EVENT_TYPE"].isin(major_events)
]

# Keep first 100 events (optional)

weather = weather.head(100)

print("Weather events loaded:", len(weather))

# =====================================
# STEP 2 : LOAD MARKET DATA
# =====================================

market = pd.read_csv("data/stocks/SP500.csv")

print(market.columns.tolist())

market["Date"] = pd.to_datetime(
    market["Date"]
)

market["Market_Return"] = (
    market["Close"].pct_change()
)

market = market[[
    "Date",
    "Market_Return"
]]

# =====================================
# STEP 3 : PROCESS STOCKS
# =====================================

stock_files = glob.glob(
    "data/stocks/*.csv"
)

stock_files = [
    f for f in stock_files
    if "SP500" not in f
]

all_results = []

for stock_file in stock_files:

    ticker = os.path.basename(
        stock_file
    ).replace(".csv", "")

    print(f"Processing {ticker}")

    stock = pd.read_csv(stock_file)

    stock["Date"] = pd.to_datetime(
        stock["Date"]
    )

    stock["Stock_Return"] = (
        stock["Close"].pct_change()
    )

    stock = stock.merge(
        market,
        on="Date",
        how="left"
    )

    stock = stock.sort_values(
        "Date"
    ).reset_index(drop=True)

    # =================================
    # LOOP THROUGH EVENTS
    # =================================

    for _, event in weather.iterrows():

        event_date = event[
            "BEGIN_DATE_TIME"
        ].normalize()

        matches = stock[
            stock["Date"] == event_date
        ]

        if len(matches) == 0:
            continue

        idx = matches.index[0]

        if idx < 10:
            continue

        if idx + 10 >= len(stock):
            continue

        window = stock.iloc[
            idx-10:idx+11
        ].copy()

        window["Relative_Day"] = range(
            -10,
            11
        )

        window["Event_Date"] = event_date

        window["Event_Type"] = event[
            "EVENT_TYPE"
        ]

        window["State"] = event[
            "STATE"
        ]

        window["Ticker"] = ticker

        all_results.append(window)

# =====================================
# STEP 4 : FINAL DATASET
# =====================================

event_study = pd.concat(
    all_results,
    ignore_index=True
)

event_study = event_study[[
    "Event_Date",
    "Event_Type",
    "State",
    "Ticker",
    "Date",
    "Relative_Day",
    "Stock_Return",
    "Market_Return"
]]

event_study.to_csv(
    "data/event_study_dataset.csv",
    index=False
)

print("\nDataset Created Successfully")
print(event_study.head())
print(
    f"\nRows Created: {len(event_study)}"
)