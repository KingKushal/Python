import matplotlib.pyplot as plt

x = [10,20,30,40,50,60,70,80] # Age group
y = [72,62,52,45,42,38,32,25] #Literacy Rate

plt.plot(x,y)

plt.xlabel('Age Group')
plt.ylabel('Literacy')

plt.title("my First Plot")

plt.show()