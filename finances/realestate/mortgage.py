from ..objects import Dollars
from .calculators import (
    total_mortgage_breakdown,
    mortgage_payment
)


class LiveMortgage:
    """Explore a live mortgage.
    
    This object assumes an amortized loan. 
    """
    def __init__(self, original_price,
        frac_down=0.0,
        years_of_loan=30,
        annual_interest_rate=0.05,
        average_appreciate_rate=0.05,
        current_year=0
        ):
        self.original_price = Dollars(original_price)
        self.frac_down = frac_down
        self.annual_interest_rate = annual_interest_rate
        self.years_of_loan = years_of_loan
        self.average_appreciate_rate = average_appreciate_rate
        self.current_year = current_year

    def __repr__(self):
        # Break down the mortgage.
        down, equity, interest = total_mortgage_breakdown(
            self.original_price,
            frac_down=self.frac_down,
            years=self.years_of_loan,
            annual_rate=self.annual_interest_rate
        )
        return (
            f"Price of the house:    {self.original_price}\n"
            f"Money down:            {down}\n"
            f"Estimated interest:    {interest}\n"
            f"Monthly mortgage:      {self.monthly_payment}\n"
            "\n"
            f"Predicted value in 5 years:     {self.predicted_appreciation(5)}\n"
            f"Predicted profit in 5 years:    {self.predicted_profit(5)}"
        )

    @property
    def down_payment(self):
        return self.original_price * self.frac_down

    @property
    def monthly_payment(self):
        return mortgage_payment(
            self.original_price,
            frac_down=self.frac_down,
            years=self.years_of_loan,
            annual_rate=self.annual_interest_rate
        )[0]

    def total_paid(self, current_year=None):
        return self.monthly_payment * 12 * current_year

    def predicted_appreciation(self, current_year=None, average_appreciate_rate=None):
        """Predict the value of the house after N (current) years."""
        if current_year is None:
            current_year = self.current_year
        if average_appreciate_rate is None:
            average_appreciate_rate = self.average_appreciate_rate
        price = self.original_price
        for i in range(current_year):
            price *= 1 + average_appreciate_rate
        return price

    def predicted_leftover_principal(self, current_year=None):
        """"""
        if current_year is None:
            current_year = self.current_year
        monthly_rate = self.annual_interest_rate / 12
        monthly_payment = self.monthly_payment
        principal = self.original_price * (1 - self.frac_down)
        for month in range(current_year * 12):
            interest_payment = principal * monthly_rate
            principal_paid = monthly_payment - interest_payment
            principal -= principal_paid
        return principal

    def predicted_profit(self, current_year=None, average_appreciate_rate=None):
        """Calculate the predicted profit.
        """
        appreciated_price = self.predicted_appreciation(
            current_year=current_year,
            average_appreciate_rate=average_appreciate_rate)
        predicted_leftover = self.predicted_leftover_principal(
            current_year=current_year)
        total_paid = self.total_paid(current_year=current_year)
        equity = appreciated_price - predicted_leftover - self.down_payment
        profit = equity - total_paid
        return profit





class RentalMortgage(LiveMortgage):
    pass
