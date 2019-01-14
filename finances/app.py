import sys
import clize

from .realestate.calculators import house_price, mortgage_payment, total_mortgage_breakdown

funcs = {
    'house_price': house_price,
    'mortgage_payment': mortgage_payment,
    'total_mortgage_breakdown': total_mortgage_breakdown
}

def main():
    clize.run(funcs)