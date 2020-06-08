from finances.taxes.calculators import federal_taxes, state_taxes
from finances.objects import Dollars


def monthly_income(
    annual_gross_income: float,
    state: str='CA',
    federal_deduction: float=None,
    status: str='married-jointly',
    print_steps=False,
):
    federal_taxes_owed = federal_taxes(
        annual_gross_income,
        status=status,
        deduction=federal_deduction,
    )

    state_taxes_owed = state_taxes(
        annual_gross_income,
        state=state,
        status=status,
    )

    monthly_gross_income = annual_gross_income / 12

    monthly_fed_withheld = federal_taxes_owed / 12
    monthly_state_withheld = state_taxes_owed / 12



    monthly_net_income = (
        monthly_gross_income -
        (monthly_fed_withheld + monthly_state_withheld)
    )

    if print_steps:
        print(f"Monthly gross income:             {Dollars(monthly_gross_income)}")
        print(f"Monthly federal taxes withheld:   {Dollars(monthly_fed_withheld)}")
        print(f"Monthly state taxes withheld:     {Dollars(monthly_state_withheld)}")
        print(f"---------------------------------------------")
        print(f"Monthly net income:               {Dollars(monthly_net_income)}")

    return Dollars(monthly_net_income)


def cli_monthly_income(
    annual_gross_income: float,
    state: str='CA',
    federal_deduction: float=None,
    status: str='married-jointly'
):

    monthly_income(
        annual_gross_income=annual_gross_income,
        state=state,
        federal_deduction=federal_deduction,
        status=status,
        print_steps=True
    )