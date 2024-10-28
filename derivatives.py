import numpy as np 

def eu_option(strike_price, underlying, option_type, position, cost=0):
    if position == "long":
        if option_type == "Call":
            return np.maximum(underlying - strike_price, 0) - cost
        elif option_type == "Put":
            return np.maximum(strike_price - underlying, 0) - cost
        else: 
            return "Please input the correct type of options"
    elif position == "short":
        if option_type == "Call":
            return np.minimum(strike_price - underlying, 0) + cost
        elif option_type == "Put":
            return np.minimum(underlying - strike_price, 0) + cost
        else: 
            return "Please input the correct type of options"

def futures(future_price, underlying, position):
    if position == "long":
        return underlying - future_price
    elif position == "short":
        return future_price - underlying
    else: 
        return "Please input the correct type of options"

def normal_stock(original_price, underlying):
    return underlying - original_price


def futures_value(spot_price, t, model = "COC model", r = 0, income_yield = 0, I = 0):
    if model == "CoC model":
        return spot_price * np.exp((r - income_yield) * t)
    if model == "known-cash income":
        return (spot_price + I) * np.exp(r * t)
    
def present_value(c, r, t, loops):
    #assume regular interval 
    cur = 0
    for i in range(1, loops + 1):
        cur += c * np.exp(-r * t * i)
    
    return c + cur