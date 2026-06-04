# Climate Risk Alpha: Analyzing the Impact of Extreme Weather Events on Stock Market Performance

## Project Overview

Climate Risk Alpha is a data analytics and financial risk analysis project that investigates how extreme weather events affect stock market performance across climate-sensitive industries.

The project uses historical weather event data from NOAA and stock market data from Yahoo Finance to measure the impact of hurricanes, floods, wildfires, winter storms, and other severe weather events on selected companies and sectors.

Using Event Study Methodology, the project calculates abnormal returns and cumulative abnormal returns (CAR) to identify whether extreme weather events create statistically significant effects on stock prices.

---

## Objectives

* Analyze the impact of extreme weather events on stock prices.
* Measure abnormal stock returns around weather-related disasters.
* Compare the sensitivity of different sectors to climate risk.
* Identify sectors most vulnerable to extreme weather events.
* Build an interactive Power BI dashboard for visualization and reporting.

---

## Business Problem

Climate change has increased the frequency and severity of extreme weather events worldwide. These events can disrupt business operations, supply chains, infrastructure, and insurance liabilities, ultimately affecting stock market performance.

This project aims to quantify the relationship between climate-related disasters and stock market reactions.

---

## Research Questions

1. Do extreme weather events affect stock returns?
2. Which sectors are most vulnerable to climate risk?
3. Are hurricanes more impactful than floods or winter storms?
4. Do severe weather events generate statistically significant abnormal returns?
5. Which sectors recover fastest after major climate events?

---

## Dataset Sources

### Weather Event Data

Source: NOAA Storm Events Database

Data Includes:

* Event Type
* Event Date
* State
* Magnitude
* Property Damage
* Crop Damage
* Event Location

Examples:

* Hurricanes
* Floods
* Wildfires
* Winter Storms
* Heat Waves
* Tropical Storms

---

### Stock Market Data

Source: Yahoo Finance

Downloaded using:

```python
import yfinance as yf
```

---

## Selected Companies

### Energy Sector

| Ticker | Company     |
| ------ | ----------- |
| XOM    | Exxon Mobil |
| CVX    | Chevron     |

Reason:
Extreme weather events can disrupt oil production, refineries, and energy supply chains.

---

### Insurance Sector

| Ticker | Company                      |
| ------ | ---------------------------- |
| AIG    | American International Group |
| TRV    | Travelers Companies          |

Reason:
Insurance firms are directly exposed to disaster-related claims.

---

### Utilities Sector

| Ticker | Company        |
| ------ | -------------- |
| NEE    | NextEra Energy |

Reason:
Power grids and utility infrastructure are affected by storms and extreme weather.

---

### Agriculture Sector

| Ticker | Company         |
| ------ | --------------- |
| DE     | Deere & Company |

Reason:
Agricultural productivity is highly dependent on weather conditions.

---

### Market Benchmark

| Index   | Ticker |
| ------- | ------ |
| S&P 500 | ^GSPC  |

Used for calculating expected returns and abnormal returns.

---

## Project Structure

```text
Climate_Risk_Alpha/
│
├── climate_alpha_env/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── data/
│   │
│   ├── raw/
│   │   └── weather/
│   │       ├── StormEvents_details-ftp_v1.0_d2018_*.csv
│   │       ├── StormEvents_details-ftp_v1.0_d2019_*.csv
│   │       ├── StormEvents_details-ftp_v1.0_d2020_*.csv
│   │       ├── StormEvents_details-ftp_v1.0_d2021_*.csv
│   │       ├── StormEvents_details-ftp_v1.0_d2022_*.csv
│   │       ├── StormEvents_details-ftp_v1.0_d2023_*.csv
│   │       ├── StormEvents_details-ftp_v1.0_d2024_*.csv
│   │       └── StormEvents_details-ftp_v1.0_d2025_*.csv
│   │
│   ├── stocks/
│   │   ├── AIG.csv
│   │   ├── CVX.csv
│   │   ├── DE.csv
│   │   ├── NEE.csv
│   │   ├── SP500.csv
│   │   ├── TRV.csv
│   │   └── XOM.csv
│   │
│   ├── event_study_dataset.csv
│   ├── event_study_with_ar.csv
│   ├── car_results.csv
│   └── event_type_summary.csv
│
├── stock_download.py
├── final_dataset.py
├── calculate_abnormal_returns.py
├── calculate_car.py
├── event_analysis.py
├── event_visualization.py
├── analysis.py
├── check_dataset.py
│
├── power bi dashboard.pbix
│
├── climate_risk_alpha.md
│
└── README.md
```

---

# Project Workflow

## Step 1: Download Stock Data

File:

```text
stock_download.py
```

Output:

```text
AIG.csv
CVX.csv
DE.csv
NEE.csv
SP500.csv
TRV.csv
XOM.csv
```

---

## Step 2: Build Event Study Dataset

File:

```text
final_dataset.py
```

Input:

- NOAA Storm Events Data
- Stock Data

Output:

```text
event_study_dataset.csv
```

---

## Step 3: Calculate Abnormal Returns

File:

```text
calculate_abnormal_returns.py
```

Output:

```text
event_study_with_ar.csv
```

---

## Step 4: Calculate CAR

File:

```text
calculate_car.py
```

Output:

```text
car_results.csv
```

---

## Step 5: Event Analysis

File:

```text
event_analysis.py
```

Output:

```text
event_type_summary.csv
```

---

## Step 6: Visualization

File:

```text
event_visualization.py
```

Output:

- Sector Analysis Charts
- Event Impact Charts
- CAR Visualizations

---

## Step 7: Dashboard Development

Tool:

```text
Power BI
```

File:

```text
power bi dashboard.pbix
```

Purpose:

- Interactive Climate Risk Dashboard
- Sector Performance Analysis
- Event Impact Analysis
- CAR Comparison

---

## Methodology

### Step 1: Environment Setup

Create a virtual environment:

```bash
python -m venv climate_alpha_env
```

Activate environment:

```bash
.\climate_alpha_env\Scripts\activate
```

Install dependencies:

```bash
pip install pandas numpy yfinance scipy statsmodels matplotlib seaborn openpyxl
```

---

### Step 2: Weather Data Collection

Download NOAA Storm Events data.

Files Used:

* StormEvents_details
* StormEvents_locations

Extract:

* Event Date
* Event Type
* State
* Severity

---

### Step 3: Stock Data Collection

Download historical stock prices using Yahoo Finance.

Example:

```python
import yfinance as yf

stock = yf.download(
    "XOM",
    start="2015-01-01",
    end="2025-12-31"
)
```

---

### Step 4: Event Study Dataset Creation

For each weather event:

1. Identify event date.
2. Extract stock returns around the event.
3. Create an event window.

Event Window:

```text
[-10,+10]
```

Meaning:

* 10 trading days before event
* Event day
* 10 trading days after event

Dataset Columns:

* Event_Date
* Event_Type
* State
* Ticker
* Date
* Relative_Day
* Stock_Return
* Market_Return

---

### Step 5: Abnormal Return Calculation

Daily Return:

```text
Return = (Current Price - Previous Price)
/ Previous Price
```

Expected Return:

```text
Expected Return =
α + β(Market Return)
```

Abnormal Return:

```text
AR =
Actual Return -
Expected Return
```

---

### Step 6: Cumulative Abnormal Return (CAR)

CAR measures total abnormal impact over the event window.

Formula:

```text
CAR = Σ AR
```

Interpretation:

| CAR Value | Meaning           |
| --------- | ----------------- |
| Positive  | Beneficial Impact |
| Negative  | Adverse Impact    |
| Near Zero | Minimal Impact    |

---

### Step 7: Statistical Testing

Perform hypothesis testing.

Null Hypothesis (H0):

```text
Extreme weather events have no impact on stock returns.
```

Alternative Hypothesis (H1):

```text
Extreme weather events significantly affect stock returns.
```

Methods:

* One-Sample T-Test
* Regression Analysis

Libraries:

```python
from scipy.stats import ttest_1samp
```

---

## Power BI Dashboard

### Executive Summary

* Total Events
* Average CAR
* Sector Comparison

### Weather Event Analysis

* Event Type Distribution
* State-wise Event Counts

### Stock Market Impact

* Stock Returns
* Market Returns
* Event Windows

### Sector Comparison

* Energy
* Insurance
* Utilities
* Agriculture

### Statistical Findings

* CAR Results
* T-Test Results
* Regression Outputs

---

## Expected Outcomes

The project aims to:

* Quantify climate-related financial risks.
* Identify vulnerable sectors.
* Measure abnormal returns caused by extreme weather events.
* Support climate risk assessment and investment decisions.

---

## Technologies Used

* Python
* Pandas
* NumPy
* SciPy
* StatsModels
* Matplotlib
* Seaborn
* Yahoo Finance API
* NOAA Storm Events Database
* Power BI
* VS Code

---

## Future Enhancements

* Add machine learning models for climate risk prediction.
* Include international weather events.
* Analyze additional sectors.
* Develop real-time climate risk monitoring dashboards.
* Incorporate ESG and sustainability indicators.

---

## Author

 Jana Akshaya Kumar

Project: Climate Risk Alpha

Domain: Data Analytics | Financial Analytics | Climate Risk Analysis
