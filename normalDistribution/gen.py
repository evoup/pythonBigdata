#!/usr/bin/python
# -*- coding:utf-8 -*-
#正态分布数据生成
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
mu = 0
sigma = 1
#http://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.arange.html#numpy.arange
x = np.arange(-5, 5, 0.1) # start stop step 
y = stats.norm.pdf(x, 0, 1)
plt.plot(x, y)
plt.title('Normal distribution with $\mu=0,\ \sigma=1$')
plt.xlabel('x')
plt.ylabel('Probability density') 
plt.show()
