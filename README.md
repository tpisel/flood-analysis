# flood-analysis

Analysing the impact of weather, including extreme weather events and climate change, on Queensland's agricultural industries.

## Questions

### Question 1: Understand the shape of flooding data over time

_Taryn_

**Hypotheses**

- Flood data will be highly seasonal from year to year
- La Nina / El Nino multi-year cycles will be evident across multi-year cycles
- The frequency of floods will increase over the last few decades

**Data sources**

- Open Meteo Flood API (GloFAS), 1990-2020, Queensland

**Visualisation**

- Seasonality time series
- Autoregression


### Question 2: Impact of flooding on cattle headcounts in Queensland and Australian saleyard prices

_Anna_

**Hypotheses**

- Excess flooding will decrease cattle head counts
- Excess flooding will increase cattle prices

**Data sources**

- Open Meteo Flood API (GloFAS), yearly 1990-2020, Queensland
- Ag Output / price data:
- [Saleyard Prices 1991-2017](https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2020)
- [Herd Size 1974-2021](https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2022)

**Visualisation**

- Time series line graphs
- Regression


### Question 3: Temperature as a driver of flooding 

_Van_

**Hypotheses**

- Hotter weather leads to more flooding (more severe, more frequent)

**Data sources**

- Open Meteo Flood API (GloFAS) 1990-2020
- Open Meteo Weather API

**Visualisation**

- Time series
- Linear regression


### Question 4: Forecasting sugar cane yields in 2040

_Tom_

**Hypotheses**

- Rising global temperatures will increase sugar cane yields in cooler climates

**Data sources**

- Open Meteo Weather API
- Australian Sugar Milling Council production data (2014 to 2021)
- Open Meteo Climate Change forecast API (from 2040)

**Visualisation**

- Prediction of sugar cane yields in Queensland



## Repository structure

Each of the above questions has been investigated in its Jupyter notebook, as follows:

- `Q1 Flooding Over Time (Taryn).ipynb`
- `Q2 Flooding on Cattle Industry (Anna).ipynb`
- `Q3 Temperature and Flooding (Van).ipynb`
- `Q4 Sugarcane and Climate Change (Tom).ipynb`

The questions utilise data saved in the `/Data` directory, primarily `flooddata.csv`. This data table has been retrieved from the Open Meteo API in `ingest.ipynb`, using tooling exposed in `queryscripts.py`.

Other files stored in the `/Data` directory include:

- `ORIGINAL_abs_cattle_totals_2020.xlsx` - herd size file downloaded from Australia Bureau of Statistics
- `abs_cattle_totals_2020.csv` - excerpt taken from original herd file
- `abs_cattle_totals_2020_transform.ipynb` - notebook that transforms herd size excerpts and creates `abs_qld_cattle_counts_excerpt.csv`
- `abs_qld_cattle_counts_excerpt.csv` - used in the analysis in Q2
- `abs_meat_prices.xlsx` - original file of saleyard prices downloaded from Australian Bureau of Statistics
- `abs_meat_prices_saleyard_prices_excerpt.csv` - cleaned up excerpt from original saleyard prices file that is used in the analysis in Q2
- `sugar_weather_future.csv` and `sugar_weather_history.csv` - weather data exported via `queryscripts.py`
- `sugar_raw_yield_data.csv` - retrieved from the Australian Sugar Milling Council, and reshaped into `sugar_production.csv` in Q4

Plots have also been exported to `/visuals`


## Summary of sources

- [Open Meteo Global Flood API](https://open-meteo.com/en/docs/flood-api)
- [Open Meteo Weather API](https://open-meteo.com/)
- [Open Meteo Climate Change API](https://open-meteo.com/en/docs/climate-api)
- Agricultural Data: [Saleyard Prices](https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2020), [Outlooks](https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2020) and[Herd Size](https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2022)


## Conda environment

The environment requirements is stored in `environment.yml` and can be recreated with `conda env create -f environment.yml`.