from .realestate import (
    total_mortgage_breakdown,
    mortgage_payment
)

class LiveMortgageLoan:
    """Explore a live mortgage."""
    def __init__(self, original_price,
        frac_down=0.0,
        years_of_loan=30,
        annual_interest_rate=0.05,
        average_appreciate_rate=0.05,
        current_year=0
        ):
        self.original_price = original_price
        self.frac_down = frac_down
        self.annual_interest_rate = annual_interest_rate
        self.years_of_loan = years_of_loan
        self.average_appreciate_rate = average_appreciate_rate,
        self.current_year = current_year

    def __repr__(self):
        # Break down the mortgage.
        down, equity, interest = total_mortgage_breakdown(
            self.original_price,
            frac_down=self.frac_down,
            years=self.years_of_loan,
            annual_rate=self.annual_interest_rate
        )
        print(f"Price of the house:    {self.original_price}")
        print(f"Money down:            {down}")
        print(f"Estimated interest:    {interest}")
        print(f"Equity earned:         {equity}")
        print(f"Monthly mortgage:      {self.monthly_payment}")
        print("")
        print(f"Predicted value in 5 years:     {self.predicted_value(5)}")
        print(f"Predicted profit in 5 years:    {self.predicted_profit(5)}")

    @property
    def monthly_payment(self):
        return mortgage_payment(
            self.original_price,
            frac_down=self.frac_down,
            years=self.years_of_loan,
            annual_rate=self.annual_interest_rate
        )

    def predicted_value(self, current_year=None, average_appreciate_rate=None):
        """Predict the value of the house after N (current) years."""
        if current_year is None:
            current_year = self.current_year
        if average_appreciate_rate is None:
            average_appreciate_rate = self.average_appreciate_rate
        price = self.original_price
        for i in range(current_year):
            price *= 1 + average_appreciate_rate
        return price

    def predicted_profit(self, current_year=None, average_appreciate_rate=None):
        """Calculate the predicted profit.
        """
        # Calculate a predicted price.
        predicted_price = self.predicted_value(
            current_year=current_year,
            average_appreciate_rate=average_appreciate_rate
        )
        # Appreciation
        appreciation = predicted_price - self.original_price    
        total_payments = current_year * 12 * self.monthly_payment

        # HARDCODED... I need to look this up!
        # fraction of monthly_payment that goes to principle (not interest)
        frac_payment_to_principal = 0.9
        equity = current_year * 12 * (self.monthly_payment * frac_payment_to_principal)
                



class RentalMortgage(LiveMortgageLoan):
    pass