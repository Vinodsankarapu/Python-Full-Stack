"""What is Matplotlib?
Definition:
Matplotlib is a powerful Python library used to create graphs, charts, and other visualizations from data.
It helps represent data visually, making it easier to understand trends, patterns, and comparisons.
Usage:
Data Analysis
Data Science
Machine Learning
Business Reports
Dashboards
Research Projects
import matplotlib.pyplot as plt
#figure
plt.figure(figsize=(12,8))
x = [1,2,3,4,5]
y = [10,20,15,30,5]

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title("Simple plot")
plt.xlabel('x axis')
plt.ylabel('y axis')


#Plot
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]
plt.subplot(2, 3, 2)
plt.bar(x,y,color = 'Purple')
plt.title("Bar Plot ")
plt.xlabel('years')
plt.ylabel('Number of cars')


#bar
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,95,70]
plt.subplot(2, 3, 3)
plt.bar(x,y,color = 'Purple',edgecolor = 'yellow')
plt.title("car sales")
plt.xlabel('years')
plt.ylabel('Number of cars')


#pie
import matplotlib.pyplot as plt
subjects_ = ['Python','Java','C','C++']
stu_ = [20,30,10,40]

plt.subplot(2,3,4)
plt.title("Pie")
plt.pie(stu_ ,labels = subjects_,autopct = '%1.1f%%',colors = ['red','white','purple','yellow'])
plt.legend(subjects_)
plt.title('Courses')



#Scatter
import matplotlib.pyplot as plt
x = ['Python','Java','C']
y= [69,13,50]

plt.subplot(2,3,5)
plt.scatter(x,y,color ='red')
plt.title('Scatter ')
plt.xlabel('Years')
plt.ylabel('Number of cars')



#Histogram
y=[10,40,20,50]
plt.subplot(2,3,6)
plt.hist(y,bins = 5) #it spread the bins
plt.title('Car Sales')
plt.xlabel('Years')
plt.ylabel('Number of cars')

plt.tight_layout()
plt.show()"""












