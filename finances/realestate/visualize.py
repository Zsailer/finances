import pandas as  pd
import numpy as np
import altair as alt

from .calculators import mortgage_payment
from .constants import (
    INTEREST_RATES,
    ANNUAL_APPRECIATION_RATE
)

def _data_over_time(house_price, monthly_payment=None, 
    frac_down=0.2, years=30, apr=INTEREST_RATES, 
    appreciate_rate=ANNUAL_APPRECIATION_RATE):
    """Summary of the lifetime of a loan.

    Returns a DataFrame with columns:
    1. time (months)
    2. equity
    3. principal
    4. profit
    5. estimated_price
    """
    if monthly_payment is None:
        monthly_payment, down_payment = mortgage_payment(house_price, frac_down=frac_down,
            years=years, annual_rate=apr)
    
    monthly_rate = apr / 12
    monthly_appreciate = appreciate_rate / 12
    price = house_price
    down_payment = house_price * frac_down

    time = np.arange(0, years*12+1)
    equity = np.empty(len(time), dtype=float)
    principal = np.empty(len(time), dtype=float)
    profit = np.empty(len(time), dtype=float)
    estimated_price = np.empty(len(time), dtype=float)
    equity[0] = down_payment
    principal[0] = house_price - down_payment
    profit[0] = 0
    estimated_price[0] = price

    for month in time[1:]:
        appreciation = monthly_appreciate * price
        price = price + appreciation
        interest_paid = principal[month-1] * monthly_rate
        principal_paid = monthly_payment - interest_paid
        principal[month] = principal[month-1] - principal_paid
        equity[month] = equity[month-1] + principal_paid
        profit[month] = profit[month-1] - interest_paid + \
            principal_paid + appreciation
        estimated_price[month] = price

    df = pd.DataFrame(dict(
        time=time,
        equity=equity,
        principal=principal,
        profit=profit,
        estimated_price=estimated_price
    ))
    return df


def plot_equity_over_time(house_price, monthly_payment=None,
    frac_down=0.2, years=30, apr=INTEREST_RATES, 
    appreciate_rate=ANNUAL_APPRECIATION_RATE):
    """"""
    df = _data_over_time(
        house_price, monthly_payment=monthly_payment,
        frac_down=frac_down, years=years, apr=apr, appreciate_rate=appreciate_rate)
    
    down_payment = frac_down * house_price

    origin = alt.Chart(pd.DataFrame({
        'time':[0, years*12],
        'equity': [down_payment, down_payment]
    })).mark_line(
        color='black',
        strokeDash=[3, 1],
        opacity=0.5
    ).encode(
        x='time:Q', y='equity:Q'
    )

    # Begin building the altair chart
    line = alt.Chart(df).mark_line(
        point=True, 
    ).encode(
        x='time',
        y=alt.Y('equity', axis=alt.Axis(format="$,f")),
        tooltip=[
            alt.Tooltip('equity', format="$,.0f"),
            alt.Tooltip('profit', format="$,.0f"),
            alt.Tooltip('estimated_price', format="$,.0f"),
            'time'
        ]
    )
    return line + origin


def plot_profit_over_time(house_price, monthly_payment=None,
                          frac_down=0.2, years=30, apr=INTEREST_RATES, 
                          appreciate_rate=ANNUAL_APPRECIATION_RATE):
    """"""
    df = _data_over_time(
        house_price, monthly_payment=monthly_payment,
        frac_down=frac_down, years=years, apr=apr, appreciate_rate=appreciate_rate)
    
    origin = alt.Chart(pd.DataFrame({
        'time': [0, years*12],
        'profit': [0, 0]
    })).mark_line(
        color='black',
        strokeDash=[3, 1],
        opacity=0.5
    ).encode(
        x='time:Q', y='profit:Q'
    )

    # Begin building the altair chart
    line = alt.Chart(df).mark_line(
        point=True,
    ).encode(
        x='time',
        y=alt.Y('profit', axis=alt.Axis(format="$,f")),
        tooltip=[
            alt.Tooltip('equity', format="$,.0f"),
            alt.Tooltip('profit', format="$,.0f"),
            alt.Tooltip('estimated_price', format="$,.0f"),
            'time'
        ]
    )
    return line + origin
