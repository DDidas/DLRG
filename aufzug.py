import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Time", "Acceleration"]
df = pd.read_excel("/Users/daviddidas/Downloads/Aufzug 2023-03-02 11-37-45.xls", sheet_name="Acceleration", usecols=columns)
print(df.columns)
print("Contents in csv file:", df)
plt.plot(df.columns)
plt.show()