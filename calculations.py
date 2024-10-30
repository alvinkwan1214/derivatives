import derivatives
import numpy as np

import matplotlib.pyplot as plt 



present_value = derivatives.present_value(1, 0.08, [2/12, 5/12])
value = derivatives.futures_value(50, t = 6/12, model="known-cash income", 
                      r = 0.08, I = present_value)
print(present_value)
print(value)

present_value_3 = derivatives.present_value(1, 0.08, [2/12])
value_3 = derivatives.futures_value(48, t = 3/12, model="known-cash income", 
                      r = 0.08, I = present_value_3)
print(present_value_3, value_3)
print(derivatives.future_value(value, 48, r = 0.08, delta_t=3/12, other=present_value_3))