import re

import numpy as np
import pandas as pd 

# Formatting functions
def fix_date(s):
    return s[3:5] + '.' + s[0:2]


def reduce_whitespace(s):
    return re.sub(r'\s+', ' ', s).strip()


def remove_whitespace(s):
    return re.sub(r'\s', '', s)


def remove_commas(s):
    return re.sub(r',', '', s)


# Don't ask me what this means... 
# Thank you to: 
# https://github.com/dpwrussell/BankOfAmericaStatementConverter
PAYMENT = 'BA ELECTRONIC PAYMENT'
ESCAPE_REGEX = re.compile(u'\x96', re.MULTILINE)
TRANSACTION_REGEX =  re.compile(
    r'^\s*(\d{2}\/\d{2})\s+'
    r'(\d{2}\/\d{2})\s+'
    r'(.*\w)\s+(\d{4})\s+'
    r'((?:\d{4})|(?:Virtual Card))\s+'
    r'((?:-\s)?[\d\.,]+'
    r')\n?\s*((?:-\s)?[\d\.,]*\s\w{3})?$', 
    re.MULTILINE
)

def read_statement(statement_file):
    """Read statement from file, return dataframe.
    """
    with open(statement_file, 'rb') as f:
        txt = f.read()

    txt = txt.decode('utf-8', 'replace')
    df = parse_statement(txt)
    return df

def parse_statement(statement_txt):
    """Parse a Bank of America Statement txt string and return a DataFrame.
    """
    items = []
    transactions = re.findall(TRANSACTION_REGEX, statement_txt)
    for t in transactions:
        transaction_date = fix_date(t[0])
        posting_date = fix_date(t[1])
        description = reduce_whitespace(t[2])
        reference = t[3]
        account = t[4]
        amount = remove_commas(remove_whitespace(t[5]))
        foreign = ' (' + reduce_whitespace(t[6] + ')') if t[6] != '' else ''

        # Add element to data.
        if description != PAYMENT:
            item = {
                'transaction_date': transaction_date,
                'posting_date': posting_date,
                'description': description,
                'reference': reference,
                'account': account,
                'amount': float(amount),
                'foreign': foreign
            }
            items.append(item)
    
    df = pd.DataFrame(items)
    return df