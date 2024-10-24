from derivatives import eu_option, futures, normal_stock
import numpy as np
import matplotlib.pyplot as plt 

underlying_range = np.linspace(20, 60, 41)
payout_call = eu_option(50, underlying_range, option_type="Call", position='short', cost=5)

payout_put = eu_option(30, underlying_range, option_type="Put", position='long', cost=7)

payout_stock = normal_stock(40, underlying_range)

total = (payout_put + payout_stock)

plt.plot(underlying_range, total)
plt.axhline(0, color='black', linewidth=1)
#plt.axvline(0, color='black', linewidth=.5)
plt.grid()
plt.show()