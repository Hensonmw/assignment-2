
# coding: utf-8

# In[3]:

#Running Python
#3rd way of running Python, in the jupyter notebook.
#!/usr/bin/env python
# encoding: utf-8

"""
my first little program

Created by Brant Faircloth on 18 Jan 2016.
Copyright 2016 Brant C. Faircloth. All rights reserved.

"""

import sys

print("Python {}".format(sys.version_info))
print("Hello world")


# #Imports
# 
# import numpy
# from numpy import *
# from numpy import random
# 
# 
# 1. How are these different from each other? Be specific.
# First, 'import numpy' besides importing this module, creates a reference to that module, so I can write numpy.name to refer to things or functions defined in this module. Second, 'from numpy import *' will import numpy and also creates reference in the namespace to all public objects defined in the module. Then, you can use just a plain name to refer to things defined in the module. You don't need to use numpy.name. Finally, 'from numpy import random' imports the module and creates a reference to 'random', so you can use this object in your program. In this last case, you also don't need to use numpy.random.
# 
# 2. Which of the above do you think is preferred? Why?
# I think using just 'import numpy' is prefered, since this will contribute to code clarity. For instance, if you use 'from numpy import random', you will be able to use 'random' allover your code, and this could make complicated to understand from where this object is comming. On the other hand, if you use 'import numpy', this means that everytime you call 'random', you will express that this is inside the 'numpy'module '(numpy.random)'. Furthermore, if you are going to use other functions in the same module, you don't need to import things again. Ultimatelly there is a potential problem of overwriting functions as I am going to explain in the next item.
# 
# 3. What happens to the stdlib module random if you run from numpy import random? Provide an example.
# It seems to me that as soon as I start using 'random' after this, I will be able to use only numpy 'random' and not stdlib 'random'. As you can see in the screenshot number 3 (RedefiningRandom-ImportTask3), as soon as I use 'from numpy import random', the random module is redefined and after that I am not able to get back to the 'stdlib random'. This could be avoided by importing 'numpy', and using 'numpy.random' always. I show the difference between both 'randoms' below.
# 
# 
# 

# In[11]:

import random
random


# In[12]:

from numpy import random
random


# #Paths
# 
# 1. On your computer, create a file on the Desktop. What's the path to that file (e.g. the file path)?
# "C:\Users\Glaucia\Desktop\Isotopes"
# 
# 2. If you created a file in the root directory of your computer, what would that file path be?
# "C:\Windows\Isotopes"
# 
# 3. On your computer, there is a setting/variable called $PATH. What does that setting do?
# This variable shows a set of directories where executable files are located. For example, one of the path that this variable shows in my computer is C:\Program Files\Common Files\Microsoft Shared\Windows Live.
# 
# 4. On your computer, there is a setting/variable called PYTHONPATH. What does that setting do?
# In my computer, probably a Windows thing, this variable is not recognized. So, I created a PYTHONPATH variable in the Advanced Settings of my computer. However I cannot find PYTHONPATH anyway. On the internet, I found the following explanation: "It has a role similar to PATH. This variable tells the Python interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. "
# 

# In[4]:

#Modules
"""
The module I picked is 'statistics', whose source is the Lib/statistics.py. 
This is going to be a valuable module for me to analyze raw data in terms of basic measurements as mean, median, standard deviation and variance. 
This is going to be valuable during the course to allow basic calculations and data management. 
Furthermore, its functions support integer, float, decimal and fractions, allowing all sorts of numeric inputs. 
Some examples of functions are:

"""
#Importing the module
import statistics

#Data
data = ([5,10,15,20,25,30,35])
print("data =",data)

#AVERAGES AND MEASURES OF CENTRAL LOCATION:
#Arithmetic mean of data:
print("data mean =", statistics.mean(data))

#Middle value (median) of data:
print("data median =",statistics.median(data))

#Low median: is always a member of the data set. When the number of data points is odd the middle value is returned. When it is even,
#the smaller of the two data points is returned:
print("data low median =",statistics.median_low(data))
#Example with a dataset with even number of data points:
print("even data set = ", (1,3,5,7))
print("even data set low median =",statistics.median_low([1,3,5,7]))

#Median high: when the number of points in the data set is odd, this function will return the middle value. When the number of data points
#is even, it will return the highest of the two middle points.
print("data high median =",statistics.median_high(data))
#Example with a dataset with even number of data points:
print("even data set high median =",statistics.median_high([1,3,5,7]))

#MEASURES OF SPREAD:
#Sample standard deviation
print("data standard deviation =", statistics.stdev(data))

#Variance
print("data variance =",statistics.variance(data))

#There is also another measurement of standard deviation, the population standard deviation:
print("data population standard deviation = ",statistics.pstdev(data,mu=None))

#And the population variance of data. In this function there is also the argument mu, that corresponds to the mean of data. If mu is
#not assigned or is 'None', than the men is also calculated by this function.
print("data population variance = ",statistics.pvariance(data))

#Taken from: Documentation » The Python Standard Library » 9. Numeric and Mathematical Modules » 9.7. statistics — Mathematical statistics functions
#https://docs.python.org/3/library/statistics.html


# In[ ]:



