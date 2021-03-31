import os
from time import ctime,sleep
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("titanic.csv")
def start1():
  print('Started loop at',ctime())
  sleep(2)
  #Exercise 1: Find dimensions of dataframe
  print("Dimensions of dataframe:",df.shape[0], "rows and",df.shape[1],"columns \n")
  print("Ended loop at", ctime())

#Exercise 2: Find age of the oldest male and female aboard the Titanic
def start2():
  print('Started loop at',ctime())
  fem_age = df.loc[df["Sex"]=="female", "Age"]
  fem_age = pd.to_numeric(fem_age)
  print("Oldest female is:", fem_age.max().astype(int), "years old \n")
  male_age = df.loc[df["Sex"]=="male", "Age"]
  male_age = pd.to_numeric(male_age)
  print("Oldest male is:", male_age.max().astype(int), "years old \n")
  print("Ended loop at", ctime())

#Exercise 3: Find the average of surviving passengers
avgSurv = df.loc[df["Survived"] == 1, "Age"]
avgSurv = pd.to_numeric(avgSurv)
print("The average age of surviving passengers is:", avgSurv.mean(), "years old \n")



ageNonSurv = df.loc[df["Survived"] == 0, "Age"]
ageNonSurv = pd.to_numeric(ageNonSurv)
print("The average age of non-surviving passengers is:", ageNonSurv.mean(), "years old \n")
#Exercise 4: Key differentiators in survival rates (charts, histograms, pie graphs, etc.)

#Class (What level where the passengers on?)
labels = ["Class 1", "Class 2", "Class 3", "Did Not Survive"]

class1Surv = df.loc[(df["Survived"]==1) & (df["PClass"]=="1st"),"Survived"]
countClass1 = (len(class1Surv)/len(df["Survived"]==1))*100
class2Surv = df.loc[(df["Survived"]==1) & (df["PClass"]=="2nd"),"Survived"]
countClass2 = (len(class2Surv)/len(df["Survived"]==1))*100
class3Surv = df.loc[(df["Survived"]==1) & (df["PClass"]=="3rd"),"Survived"]
countClass3 = (len(class3Surv)/len(df["Survived"]==1))*100
noSurv = len(df.loc[df["Survived"]==0])/len(df["Survived"])*100
values = [countClass1,countClass2,countClass3,noSurv]
fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("Class to Survival Ratio")
plt.show()
#Gender 

maleSurv = df.loc[(df["Survived"]==1) & (df["Sex"] == "male")]

print(maleSurv)



#Exercise 5: Survival rate by age

infantSurv = df.loc[(df["Survived"]==1) & (df["Age"]<12)]
teenSurv = 0
adultSurv = 0
seniorSurv = 0
print(infantSurv)

