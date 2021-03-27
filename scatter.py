import pandas as pd
import plotly_express as pe

df = pd.read_csv(r"D:/python/Data-visualization-master/csv files/data.csv")
diagram = pe.scatter(df,x="Population",y="Per capita",color="Country",size="Percentage",size_max=10)
diagram.show()