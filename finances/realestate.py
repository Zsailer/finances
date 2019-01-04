from .objects import Dollars

def house_price(mortgage_payment: float, frac_down=0.2, years=30, annual_rate=0.045):
    """Given a monthly mortgage payment, returns the price of the house and down payment.
    
    This is useful for calculating the price of a house you can afford given
    a monthly payment amount. P is the loan amount. Formulas for the loan ammount 
    were pulled from Wikipedia (https://en.wikipedia.org/wiki/Mortgage_calculator).
    Nothing fancy going on here! :)

    Parameters: 

    :param mortgage_payment: dollar amount of the monthly mortgage payment to query.
    :param frac_down: fraction of the total house price to put down. 
    :param years: number of years to pay out mortgage.
    :param annual_rate: house loan interest rate.

    Returns:

    :param total: dollar amount of the total loan.
    :param down: dollar amount of down payment required for the fraction down.
    """
    if frac_down > 1.0 or  frac_down < 0.0:
        raise Exception("frac_down must between 0 and 1.")
    if annual_rate > 1.0 or annual_rate < 0.0:
        raise Exception("annual_rate must between 0 and 1.")

    c = mortgage_payment
    N = 12*years
    r = annual_rate / 12
    P = c * ((1+r)**N - 1) / (r*(1+r)**N)
    total = (1/(1-frac_down)) * P
    down = frac_down * total
    return Dollars(total), Dollars(down)


