from mymodule import myplot

# test import from local module
x = [0.5**i for i in range(20)]
myplot.myplot(x)


'''
# import function
from mymodule.myplot import myplot

# test import from local module
x = [0.5**i for i in range(20)]
myplot(x)

'''