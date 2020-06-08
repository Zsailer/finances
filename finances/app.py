import sys
import clize

from .realestate.calculators import (
    house_price,
    mortgage_payment,
    total_mortgage_breakdown
)

from .taxes.calculators import cli_tax_summary
from .budget.calculator import cli_monthly_income


funcs = {
    'house_price': house_price,
    'mortgage_payment': mortgage_payment,
    'total_mortgage_breakdown': total_mortgage_breakdown,
    'tax_summary': cli_tax_summary,
    'monthly_income': cli_monthly_income
}

def main():
    clize.run(funcs)