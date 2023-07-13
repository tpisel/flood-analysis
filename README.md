# flood-analysis

Analysing the impact of climate change on Queensland Cattle markets, intermediated by increased flood events


## Questions

### Question 1: Understand the shape of flooding data over time

Taryn

**Hypotheses**

- Flood data will be highly seasonal from year to year
- La Nina / El Nino multi-year cycles will be evident across multi-year cycles
- The frequency of floods will increase over the last few decades

**Data sources**

- Open Meteo Flood API (GloFAS), 1990-2020, Queensland

**Visualisation**

- Seasonality time series
- Autoregression


### Question 2: Impact of flooding on cattle headcounts and other agricultural output

Anna

**Hypotheses**

- Excess flooding will decrease cattle head counts
- Excess flooding will increase cattle prices
- Flooding impacts will be specific to affected regions

**Data sources**

- Open Meteo Flood API (GloFAS), yearly 1990-2020, Queensland
- Ag Output / price data (TBD)

**Visualisation**

Time series line graphs
Regression


### Question 3: Temperature as a driver of flooding 

Van

**Hypotheses**

- Hotter weather leads to more flooding (more severe, more frequent)

**Data sources**

- Open Meteo Flood API (GloFAS) 1990-2020
- Open Meteo Weather API

**Visualisation**

- Time series
- Linear regression


### Question 4: Forecasting spatial changes in agricultural productivity in 2040

Tom

**Hypotheses**

- Some areas will be less productive, some more

**Data sources**

- Open Meteo Flood API (GloFAS) 1990-2020
- Open Meteo Weather API
- Some Global warming forecasts?

**Visualisation**

- Geospatial heatmap view



## Repository structure

`/data` - Data extracts  
`ingest.ipynb` - Scripts to download, clean, and join data for subsequent analysis  
`question_1.ipynb`  
`question_2.ipynb`   
`question_3.ipynb`   
`question_4.ipynb`   
`/plots` - Rendered plots  


## Data sources

- [Open Meteo Global Flood API](https://open-meteo.com/en/docs/flood-api)
- [Open Meteo Weather API](https://open-meteo.com/)
- [Agricultural Data] -- to add

