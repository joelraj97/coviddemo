import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import json
import numpy as np
from dash.dependencies import Input,Output
df = pd.read_csv('owid-covid-data.csv')
df = df[df.location != 'World']
df = df.sort_values(by=['date'])
df_latest = df[df.date == df.date.max()]
fig = px.choropleth(df, locations="iso_code",
                    color="new_cases",
                    hover_name="location",
                    animation_frame="date",
                    title = "Daily new COVID cases",
                    color_continuous_scale=px.colors.sequential.PuRd)

fig["layout"].pop("updatemenus")
fig.show()
df['new_date'] = pd.to_datetime(df['date'])
df['Year-Week'] = df['new_date'].dt.strftime('%Y-%U')
df['Year-Week'].head()
fig = px.choropleth(df, locations="iso_code",
                    color="total_cases",
                    hover_name="location", # column to add to hover information
                    animation_frame="Year-Week",
                    title = "Weekly total COVID cases",
                    color_continuous_scale=px.colors.sequential.PuRd)
fig.show()
