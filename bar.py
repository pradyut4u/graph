import pandas as pd
import plotly_express as pe

df = pd.read_csv(r"D:/python/Data-visualization-master/csv files/data.csv")
diagram = pe.bar(df,x="Country",y="InternetUsers")
diagram.show()