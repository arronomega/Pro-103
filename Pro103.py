import pandas as pd
import plotly.express as px
df2 = pd.read_csv("Copy+of+data+-+data.csv")
fig3 = px.scatter(df2,x ="date",y = "cases" ,color = "country",size_max = 67)
fig3.show()