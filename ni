import matplotlib.pyplot as plt

Weeks=[1,2,3,4]
onions=[45,25,32,80]
brinjal=[16,28,15,50]

plt.title('Sales Analysis')
plt.ylabel('Weeks')
plt.xlabel('Prices')

plt.plot(Weeks,onions,marker='D',markersize=15,markeredgecolor='r')
plt.plot(Weeks,brinjal)
plt.show()

****************************************************************************************************************

