#%%
#1
import pandas as pd
data = pd.read_csv(r"cereal.csv")
data

#%%
#2
import pandas as pd
data = pd.read_csv(r"cereal.csv")
data.head()

#%%
#3
import pandas as pd
data = pd.read_csv(r"cereal.csv")
data.describe()

# %%
#4
import pandas as pd
data = pd.read_csv(r"cereal.csv")
correlation = data[["calories", "protein", "fat", "sodium", "fiber", "carbo", "sugars", "potass", "vitamins"]].corr()
print("Highest correlation: 0.562340, sugars+calories")
print("Lowest correlation: 0.005407, sodium+fat")
correlation

# %%
#5
import pandas as pd
data = pd.read_csv(r"cereal.csv")
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 8))
correlation = data[["calories", "protein", "fat", "sodium", "fiber", "carbo", "sugars", "potass", "vitamins"]].corr()
sns.heatmap(correlation, annot=True)
plt.title('Correlation Matrix')
plt.show()

#%%
#6
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"cereal.csv")
manufacturer_counts = data['mfr'].value_counts()
plt.figure(figsize=(11, 6))
manufacturer_counts.plot(kind='bar')
plt.title('Number of Cereals by Manufacturer')
plt.xlabel('Manufacturer')
plt.ylabel('Number of Cereals')
plt.show()

# %%
#7
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"cereal.csv")
fig, ax = plt.subplots()
ax.scatter(data['calories'], data['rating'], s=12)
ax.set_xlabel('Calories')
ax.set_ylabel('Rating')
ax.set_title('Scatter Plot of Calories vs. its Rating in Cereal')
plt.show()

# %%
#8
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"cereal.csv")
plt.figure(figsize=(10, 6))
plt.scatter(data['sugars'], data['rating'], alpha=0.7)
plt.title('Sugar Content vs. Rating of Cereals')
plt.xlabel('Sugars')
plt.ylabel('Rating')
plt.show()

# %%
#9
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"cereal.csv")
cereals = data.head(5)
fig, ax = plt.subplots()
ax.bar(cereals['nae'], cereals['rating'])
ax.set_xlabel('Cereal Brand')
ax.set_ylabel('Rating')
ax.set_title('Ratings for the First 5 Cereal Brands')
plt.xticks(rotation=50)
ax.set_ylim(0, cereals['rating'].max() + 10)
plt.show()

# %%
#10
print("From the data set, it can be concluded that a higher sugar and calorie content typically constituded towards a lower rating, while aspects such as potassium, protein, and fiber contents correlated with eachother at a higher level.")
