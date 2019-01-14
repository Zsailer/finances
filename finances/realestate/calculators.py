from ..objects import Dollars

def house_price(
    mortgage_payment: float, *, 
    frac_down: float=0.2, years: int=30, 
    annual_rate: float=0.045):
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
    """
    if frac_down > 1.0 or  frac_down < 0.0:
        raise Exception("frac_down must between 0 and 1.")
    if annual_rate > 1.0 or annual_rate < 0.0:
        raise Exception("annual_rate must between 0 and 1.")
    c = mortgage_payment
    N = 12*years
    r = annual_rate / 12
    P = c * ((1+r)**N-1)/(r*(1+r)**N)
    total = (1/(1-frac_down))*P
    down = frac_down * total
    return Dollars(total), Dollars(down)


def mortgage_payment(
    house_price: float, *,
    frac_down: float = 0.2, years: int = 30,
    annual_rate: float = 0.045):
    """Given the price of a house, return the estimated monthly mortgage payment.

    Formulas for the loan ammount 
    were pulled from Wikipedia (https://en.wikipedia.org/wiki/Mortgage_calculator).
    Nothing fancy going on here! :)

    Parameters: 

    :param house_price: price of the house in dollars.
    :param frac_down: fraction of the total house price to put down. 
    :param years: number of years to pay out mortgage.
    :param annual_rate: house loan interest rate.
    """
    if frac_down > 1.0 or frac_down < 0.0:
        raise Exception("frac_down must between 0 and 1.")
    if annual_rate > 1.0 or annual_rate < 0.0:
        raise Exception("annual_rate must between 0 and 1.")
    N = 12*years
    r = annual_rate / 12
    down = frac_down * house_price
    P = house_price - down
    mortgage_payment = P * (r*(1+r)**N) / ((1+r)**N - 1)
    return Dollars(mortgage_payment), Dollars(down) 


def total_mortgage_breakdown(house_price: float, *,
    frac_down: float = 0.2, years: int = 30,
    annual_rate: float = 0.045):
    """Calculate the total mortgage breakdown: down payment, equity gained, and interested paid.
    """
    # Breakdown mortgage payement
    payment, down = mortgage_payment(
        house_price, frac_down=frac_down, 
        years=years, annual_rate=annual_rate)
    total_paid = payment * 12 * years + down
    interest_paid = total_paid - (house_price + down)
    equity = total_paid - (down + interest_paid)
    return down, equity, interest_paid


