import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data_csv2=pd.read_csv("covid-19-tests-country.csv")
data_csv2M=data_csv2[(data_csv2['Total COVID-19 tests']<=50000)]
data_csv2M=data_csv2M.reset_index(drop=True)
# =============================================================================
# print(data_csv.dtypes)
# print(data_csv.select_dtypes(exclude=[object]))
# print(data_csv.info())
# print(data_csv['Code'].nunique(dropna=False))
# print(data_csv['Code'].nunique(dropna=True))
# =============================================================================
# =============================================================================
# print(data_csv['Code'].nbytes)
# print(data_csv.isnull().sum())
# =============================================================================
data_csv2M.insert(4,"Class","")
count=len(data_csv2.Entity)
count1=len(data_csv2M.Entity)

for i in range(0,count1):
    if(data_csv2M["Total COVID-19 tests"][i]<=2000):
         data_csv2M["Class"][i]="Low"
    elif((data_csv2M["Total COVID-19 tests"][i]>2000) and (data_csv2M["Total COVID-19 tests"][i]<12000 )):
         data_csv2M["Class"][i]="Medium"
    else:
         data_csv2M["Class"][i]="High"
    
#print(pd.crosstab(index=data_csv["Class"],columns="Count",dropna=True))

coronaIndia=pd.read_excel(r"C:\Users\Pavan786\.spyder-py3\Ex.xlsx")
coronaIndia2=coronaIndia[['day','month','countryterritoryCode','cases','deaths']]
coronaIndiaSubset1=coronaIndia2[(coronaIndia2.countryterritoryCode=='IND') & (coronaIndia2.cases !=0) & (coronaIndia2.month==3) & (coronaIndia2.deaths<=4)]
coronaIndiaSubset2=coronaIndia2[(coronaIndia2.countryterritoryCode=='IND') & (coronaIndia2.cases !=0) & (coronaIndia2.month==4)]
coronaIndiaSubset1['deaths']=coronaIndiaSubset1['deaths'].astype('category')
# =============================================================================
# sns.distplot(data_csv2['Total COVID-19 tests'],kde=False,bins=15)
# sns.countplot(x='Class',data=data_csv2)
# sns.countplot(x='Class',data=data_csv2)
# sns.countplot(x='cases',data=coronaIndiaSubset1,hue='deaths')
# =============================================================================
sns.boxplot(y='Total COVID-19 tests',x='Class',data=data_csv2M)
#coronaIndiaSubset1mod=coronaIndiaSubset1.drop(3555)
# =============================================================================
# coronaIndiaSubset3=coronaIndia2[ (coronaIndia2.cases !=0) & (coronaIndia2.month==3) & (coronaIndia2.day==1)]
#coronaIndiaSubset2.dropna(axis=0,inplace=True)
# =============================================================================
# =============================================================================
# plt.ion()
# plt.plot(coronaIndiaSubset1['day'],coronaIndiaSubset1['cases'],"-b")
# plt.plot(coronaIndiaSubset2['day'],coronaIndiaSubset2['cases'],"-b")
# plt.scatter(coronaIndiaSubset1['day'],coronaIndiaSubset1['cases'],s=10,c='red',marker=r'$\clubsuit$')
# plt.scatter(coronaIndiaSubset2['day'],coronaIndiaSubset2['cases'],s=10,c='red',marker=r'$\clubsuit$')
# plt.title('Daily increase in Corona Cases')
# plt.xlabel('DayWise')
# plt.ylabel('No of Cases')
# =============================================================================
#sns.set(style="darkgrid")
#sns.lmplot('day','cases',data=coronaIndiaSubset1,hue='deaths',legend=True,palette='Set1',fit_reg=False)
#sns.distplot(coronaIndiaSubset1['cases'])
#plt.hist(coronaIndiaSubset1['cases'],color='red',bins=5,edgecolor="black")
