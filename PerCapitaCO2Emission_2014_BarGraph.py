import pandas as pd
import matplotlib.pyplot as plt

#Reading File and Parsing
file = 'API_EN.ATM.CO2E.PC_DS2_en_excel_v2_9944766.xls'
data = pd.ExcelFile(file)
df1 = data.parse('Data', skiprows=3)
df1 = df1.drop(["Country Code", "Indicator Name", "Indicator Code"], axis=1)
df1 = df1.set_index("Country Name")
df1 = df1.sort_values('2014', ascending=False)

#print (df1.loc['India']['2014'])
df1.loc[["Qatar", "Kuwait","Bahrain","United Arab Emirates","Saudi Arabia","United States","Australia","Canada","Russian Federation","Singapore","Netherlands", "Japan","Norway","Germany", "China", "United Kingdom" ,"France","India"], "2014"].plot(kind='bar')

#Fromatting axis ticks
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xticks(fontsize=8)
plt.suptitle('CO2 emissions (metric tons per capita) 2014', fontsize=19)


plt.show()
