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

