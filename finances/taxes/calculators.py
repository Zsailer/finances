import numpy as np
import pandas as pd

from ..objects import Dollars
from .constants import (
    federal_tax_brackets,
    federal_standard_deduction,
    state_tax_brackets
)

def graduated_tax_calculator(taxable_income:float, status: str, brackets: pd.DataFrame):
    # Get column that's relevant
    col = brackets[status]

    # Get index of highest bracket.
    idx = col[col > taxable_income].index[0]

    # Calculate fraction of highest bracket
    amount = (taxable_income -
              brackets.iloc[idx-1][status]) * brackets.iloc[idx]['rate']

    # Calculate amount
    for i in range(1, idx):
        amount += (
            brackets.iloc[i]['rate']
            * (
                brackets.iloc[i][status] -
                brackets.iloc[i-1][status]
            )
        )
    return Dollars(amount)


def federal_taxes(
    income: float,
    deduction: float=None, # Standard deduction
    status='married-jointly'
):
    """Calculate federal taxes on taxable income (assuming graduated).
    """
    if deduction is None:
        deduction = federal_standard_deduction.iloc[0][status]

    taxable_income = income - deduction
    amount =  graduated_tax_calculator(
        taxable_income=taxable_income,
        brackets=federal_tax_brackets,
        status=status
    )
    return amount


def property_taxes(property_value):
    """Calculate property taxes for owning a house."""
    return property_value * 0.0125


def state_taxes(
    income: float,
    state: str='CA',
    status: str='married-jointly',
):
    amount = graduated_tax_calculator(
        taxable_income=income,
        status=status,
        brackets=state_tax_brackets
    )
    return amount


def cli_tax_summary(
    income: float,
    deduction: float=None, # Standard deduction
    status='married-jointly'
):
    if deduction is None:
        deduction = federal_standard_deduction.iloc[0][status]

    taxable_income = income - deduction

    print(f"Income:\t\t\t\t{Dollars(income)}")
    print(f"Deduction (Fed):\t\t{Dollars(deduction)}")
    print(f"Taxable Income (Fed):\t\t{Dollars(taxable_income)}")

    fed_taxes_owed = federal_taxes(income=income, deduction=deduction, status=status)
    state_taxes_owed = state_taxes(income=income, state='CA', status=status)

    print(f"Federal Taxes Owed:\t\t{Dollars(fed_taxes_owed)}")
    print(f"Effective Tax Rate (Fed):\t{round(fed_taxes_owed/income * 100, 2)}%")

    print(f"State Taxes Owed:\t\t{Dollars(state_taxes_owed)}")
    print(f"Effective Tax Rate (State):\t{round(state_taxes_owed/income * 100, 2)}%")
    print("-"*50)

    total_taxes = fed_taxes_owed + state_taxes_owed

    print(f"Federal Withholding:\t\t{Dollars(fed_taxes_owed/ 12)}")
    print(f"State Withholding:\t\t{Dollars(state_taxes_owed/ 12)}")
    print(f"Total Monthly Withholding:\t{Dollars(total_taxes/ 12)}")



