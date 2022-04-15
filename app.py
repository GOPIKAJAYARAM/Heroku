import os
import dash
# from jupyter_dash import JupyterDash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_auth
from dash.dependencies import Input,Output 
import pandas as pd

USERNAME_PASSWORD_PAIRS=[["gopika","gopika"]]
df=px.data.tips()
# app=JupyterDash()
app=dash.Dash(__name__)
auth=dash.auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server=app.server
app.layout=html.Div([
                     dcc.Dropdown(
                         id="dropdown",
                         options=[{"label":x,"value":x} for x in df.day],
                         value=df.day[0],
                         clearable=False,
                     ),
                     dcc.Graph(id="bar-chart"),
])

@app.callback(
    Output("bar-chart","figure"),
    [Input("dropdown","value")])
def update_bar_chart(day):
  mask=df["day"]==day
  fig=px.bar(df[mask],x="sex",y="total_bill",color="smoker",barmode="group")
  return fig 

if __name__ == "__main__":
  app.run_server(debug=True)
