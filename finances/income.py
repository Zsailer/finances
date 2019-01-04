import numpy as np
import pandas as pd

from .constants import brackets, standard_deduction

class Budget(object):
    """
    """
    def __init__(self, income, status='married-jointly'):

        self.income = income

    @property
    def federal_taxes(self):
        """Calculate taxes on taxable income (assuming graduated).
        """
        # Get column that's relevant
        col = brackets[status]

        # Get index of highest bracket.
        idx = col[col > taxable_income].index[0]

        # Calculate fraction of highest bracket
        amount = (taxable_income - brackets.iloc[idx-1][status]) * brackets.iloc[idx]['rate']

        # Calculate amount
        for i in range(idx):
            amount += brackets.iloc[i]['rate'] * brackets.iloc[i][status]

        return amount
