# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
#Code starts here
census = np.concatenate((data,new_record),axis = 0)
age = census[:,0]
max_age = max(age)
min_age = min(age)
age_mean = round(np.mean(age),2)
age_std = round(np.std(age),2)
race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
a = min(len_0,len_1,len_2,len_3,len_4)
if len_0 == a:
    minority_race = 0
elif len_1 == a:
    minority_race = 1
elif len_2 == a:
    minority_race = 2
elif len_3 == a:
    minority_race = 3
else:
    minority_race = 4
senior_citizens = census[census[:,0] > 60]
working_hours_sum = sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = round(working_hours_sum/senior_citizens_len,2)
print(avg_working_hours)
high = census[census[:,1] > 10]
low = census[census[:,1] <=10]
avg_pay_high = round(np.mean(high[:,7]),2)
avg_pay_low = round(np.mean(low[:,7]),2)



