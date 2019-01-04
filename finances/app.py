import sys
import clize

from .realestate import house_price

funcs = {
    'house_price': house_price 
}

def main():
    clize.run(funcs)