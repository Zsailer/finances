import numpy as np
import pandas as pd

from .constants import brackets

def federal_taxes(taxable_income, status='married-jointly'):
    """Calculate federal taxes on taxable income (assuming graduated).
    """
    # Get column that's relevant
    col = brackets[status]

    # Get index of highest bracket.
    idx = col[col > taxable_income].index[0]

    # Calculate fraction of highest bracket
    amount = (taxable_income -
              brackets.iloc[idx-1][status]) * brackets.iloc[idx]['rate']

    # Calculate amount
    for i in range(idx):
        amount += brackets.iloc[i]['rate'] * brackets.iloc[i][status]

    return amount


def property_taxes(property_value):
    """Calculate property taxes for owning a house."""
    return property_value * 0.0125
