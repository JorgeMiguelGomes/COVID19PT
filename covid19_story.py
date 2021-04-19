# Import all libraries 
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

# Read CSV file   
df = pd.read_csv('COVID19PT_STORY.csv')

# CSV file has the following fields 
# DATA - Date 
# CONCELHO - County
# ARS - Health Region 
# Valor - Cases per 100,000k inhabitants during a 14 day period 
# RT - The R(t) value for ARS at the 'DATA'

# Make sure that 'DATA' is in the right format 

df['DATA'] = pd.to_datetime(df['DATA'],format='%Y-%m-%d')
print(df.info())

# Make Graph
# Notes: Due to limitations on plotly we turn the field 'DATA' into a string so that the animation plays nicely 

fig = px.scatter(df, 
	x="RT", 
	y="VALOR",
	width=1920,
	height=1080,
	animation_frame=df.DATA.astype(str),
	animation_group="CONCELHO",
    size="VALOR", 
    color="CONCELHO", 
    hover_name="CONCELHO",
    log_x=False, 
    size_max=45, 
    range_x=[0,2],
    range_y=[0,2400])


#Plot Graph 
fig.show()
