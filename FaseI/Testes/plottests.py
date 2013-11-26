import matplotlib.pyplot as plt
 
plt.figure()
#create some data
x_series = [0,1,2,3,4,5]
y_series_1 = [x**2 for x in x_series]
y_series_2 = [x**3 for x in x_series]
 
#plot the two lines
plt.plot(x_series, y_series_1)
plt.plot(x_series, y_series_2)
plt.show()