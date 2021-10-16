import matplotlib.pyplot as plt

x1 = [5,4,3,2,1,0]
y1 = [0,1,2,3,4,5]

plt.plot(x1,y1,label = 'literacy rate')


y2 = [0,2,4,6,8,10]
x2 = [10,8,6,4,2,0]

plt.plot(x2,y2,label = 'Financial rate')


x3 = [15,12,9,6,3,0]
y3 = [0,3,6,9,12,15]

plt.plot(x3,y3,label = 'y')


x4 = [20,16,12,8,4,0]
y4 = [0,4,8,12,16,20]

plt.plot(x4,y4,label = 'x')


plt.xlabel('Age Group')
plt.ylabel('y-axis')

plt.title('My Plot')

plt.legend()
plt.show()
