import pandas as pd
import plotly_express as pe

df = pd.read_csv(r"D:/python/Data-visualization-master/csv files/line_chart.csv")
diagram = pe.line(df,x="Year",y="Per capita income",color="Country",title="Income of Countries")
diagram.show()