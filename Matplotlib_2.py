import matplotlib.pyplot as plt

x1 = [0,20,30,40,50,60,70,80]
y1 = [80,60,50,45,40,30,20,0]

plt.plot(x1,y1,label = 'literacy rate')

x2 = x1
y2 = [0,25,40,55,62,70,75,80]

plt.plot(x2,y2,label = 'Financial rate')


plt.xlabel('Age Group')
plt.ylabel('y-axis')

plt.title('My First Plot')

plt.legend()
plt.show()
