# flood-analysis

Analysing the impact of weather, including extreme weather events and climate change, on Queensland's agricultural industries.


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


### Question 2: Impact of flooding on cattle headcounts in Queensland and Australian saleyard prices

Anna

**Hypotheses**

- Excess flooding will decrease cattle head counts
- Excess flooding will increase cattle prices

**Data sources**

- Open Meteo Flood API (GloFAS), yearly 1990-2020, Queensland
- Ag Output / price data:
  
  Saleyard Prices 1991-2017 (https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2020)
  
  Herd Size 1974-2021 (https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2022)

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
The files are to be read in the following order:
 
`ingest.ipynb` - Scripts to download, clean, and join data for subsequent analysis  
`question_taryn.ipynb`  
`question_van.ipynb`   
`question_anna.ipynb`   
`question_tom.ipynb` 
`/data` - Data extracts:

'ORIGINAL_abs_cattle_totals_2020.xlsx' - herd size file downloaded from Australia Bureau of Statistics

'abs_cattle_totals_2020.csv' - excerpt taken from original herd file

'abs_cattle_totals_2020_transform.ipynb' - notebook that transforms herd size excerpts and creates 'abs_qld_cattle_counts_excerpt.csv'

'abs_qld_cattle_counts_excerpt.csv' - used in the analysis in question_anna_ipynb

'abs_meat_prices.xlsx' - original file of saleyard prices downloaded from Australian Bureau of Statistics

'abs_meat_prices_saleyard_prices_excerpt.csv' - cleaned up excerpt from original saleyard prices file that is used in the analysis in question_anna.ipynb

'flooddata.csv' - weather data generated in 'ingest.ipynb'

## Data sources

- [Open Meteo Global Flood API](https://open-meteo.com/en/docs/flood-api)
- [Open Meteo Weather API](https://open-meteo.com/)
- [Agricultural Data]: Saleyard Prices (https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2020)https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2020)
                       Herd Size (https://www.agriculture.gov.au/abares/research-topics/agricultural-outlook/data#_2022)

