# coded by Ramon Medeiro. Please use this content only to knowledge. Try to do this project yourself.
# FREECODECAMP project 1.

import numpy as np

def calculate(lista):
    # define a dict
    d = {}

    # make a array with 3x3 dim.
    a = np.array(lista).reshape(3,3)

    # make mean
    media1 = list(np.mean(a, axis=0))
    media2 = list(np.mean(a, axis=1))
    media3 = np.mean(a)
    d['mean'] = [media1, media2, media3]

    # make variance
    variance1 = list(np.var(a, axis=0))
    variance2 = list(np.var(a, axis=1))
    variance3 = np.var(a)
    d['variance'] = [variance1, variance2, variance3]

    # make standard deviation. std = sqrt(variance)
    std1 = list(np.std(a, axis=0))
    std2 = list(np.std(a, axis=1))
    std3 = np.std(a)
    d['standard deviation'] = [std1, std2, std3]

    # max
    max1 = list(np.max(a, axis=0))
    max2 = list(np.max(a, axis=1))
    max3 = np.max(a)
    d['max'] = [max1, max2, max3]

    # min
    min1 = list(np.min(a, axis=0))
    min2 = list(np.min(a, axis=1))
    min3 = np.min(a)
    d['min'] = [min1, min2, min3]

    # sum
    sum1 = list(np.sum(a, axis=0))
    sum2 = list(np.sum(a, axis=1))
    sum3 = np.sum(a)
    d['sum'] = [sum1, sum2, sum3]

    return d


    
