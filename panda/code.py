# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank = pd.DataFrame(bank_data)

#Code starts here
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

banks = bank.drop(['Loan_ID'],axis = 1)
print(banks)
print(banks.isnull().sum())
bank_mode = banks.mode(axis = 0)
for x in banks.columns.values:
        banks[x]=banks[x].fillna(value=bank_mode[x].iloc[0])
print(banks.isnull().sum().values.sum())

avg_loan_amount = pd.pivot_table(banks,values = 'LoanAmount',index = ['Gender','Married','Self_Employed'])
print(round(avg_loan_amount['LoanAmount'][1],2))

loan_approved_se = ((banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')).sum()
loan_approved_nse = ((banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')).sum()
percentage_se = (loan_approved_se/(banks['Loan_Status'].count()))*100
print(round(percentage_se,2))
percentage_nse = (loan_approved_nse/(banks['Loan_Status'].count()))*100
print(round(percentage_nse,2))

loan_term = banks['Loan_Amount_Term'].apply(lambda x:(x/12))
big_loan_term = (banks['Loan_Amount_Term'] >= 300).sum()
print(big_loan_term)

loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()
print(round(mean_values.iloc[1,0],2))




