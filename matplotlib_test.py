labels = ["Class 1", "Class 2", "Class 3", "Did Not Survive"]

class1Surv = df.loc[(df["Survived"]==1) & (df["PClass"]=="1st"),"Survived"]
countClass1 = (len(class1Surv)/len(df["Survived"]==1))*100
class2Surv = df.loc[(df["Survived"]==1) & (df["PClass"]=="2nd"),"Survived"]
countClass2 = (len(class2Surv)/len(df["Survived"]==1))*100
class3Surv = df.loc[(df["Survived"]==1) & (df["PClass"]=="3rd"),"Survived"]
countClass3 = (len(class3Surv)/len(df["Survived"]==1))*100
noSurv = len(df.loc[df["Survived"]==0])/len(df["Survived"])*100
values = [countClass1,countClass2,countClass3,noSurv]
plt.figure(0)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:

fig1, ax1 = plt.subplots()
ax1.pie(values, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.figure(1)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
animals = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


#Gender 

maleSurv = df.loc[(df["Survived"]== 1) & (df["Sex"] == "male"), "Sex"]
maleRate = (maleSurv.count()/(df["Sex"].count())*100)
femSurv = df.loc[(df["Survived"]== 1) & (df["Sex"] == "female"), "Sex"]
femRate = (femSurv.count()/(df["Sex"].count())*100)
nonSurv = (df.loc[df["Survived"]== 0]).count()
  


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Male Survived', 'Female Survived', 'Did Not Survive']
sizes = [maleRate, femRate, nonSurv]
  
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
