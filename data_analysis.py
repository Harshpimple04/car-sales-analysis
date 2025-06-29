import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df = pd.read_csv("Car_sales.csv")
#print(df.head())
model_sales = df['Model'].value_counts()
#print(model_sales)




#use of matplotlib
plt.figure(figsize=(10,6))
model_sales.plot(kind="bar" , color= "skyblue")
plt.title("number of cars sold by model")
plt.xlabel("car model")
plt.ylabel("number of cars sold")
plt.xticks(rotation=45)
plt.tight_layout()
#plt.show()




# use of plotly
fig = px.pie(
    values= model_sales.values,
    names= model_sales.index,
    title="Sale distribution my car model",
    hole= 0.3
)
fig.update_traces(textinfo='label+value')

fig.show()