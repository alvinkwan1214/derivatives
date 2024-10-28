from derivatives import eu_option, futures, normal_stock, futures_value, present_value
import numpy as np
import matplotlib.pyplot as plt 



present_value = present_value(0.06, 0.1, 0.25, 2)
value = futures_value(9, t = 9/12, model="known-cash income", 
                      r = 0.1, I = present_value)
print(value)