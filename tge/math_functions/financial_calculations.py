from typing import Union



__all__ = ['calculate_present_value', 'percentage_increase', 'percentage_decrease', 'discount_price', 'body_mass_index']




def calculate_present_value(principal: Union[int,float], rate: Union[int,float], years: int) -> float:
    """
    Calculate the present value of an investment based on the given parameters.

    Parameters:
    principal (float): The initial investment amount.
    rate (float): The annual interest rate as a percentage.
    years (int): The number of years the investment will be held.

    Returns:
    float: The present value of the investment after the specified number of years.
    """
    return principal * pow(1 + rate / 100, years)

def percentage_increase(number: Union[int,float], percentage: Union[int,float]) -> float:
    """
    Calculate the percentage increase from an old grade to a new grade.

    Parameters:
        old_grade (float): The initial grade.
        new_grade (float): The updated grade.

    Returns:
        float: The percentage increase from the old grade to the new grade.
               The result is represented as a decimal value (e.g., 0.10 for 10% increase).
    """
    return (percentage - number) / number


def percentage_decrease(old_grade: Union[int,float], new_grade: Union[int,float]) -> float:
    """
    Calculate the percentage decrease between an old grade and a new grade.

    Parameters:
        old_grade (float): The original grade or value.
        new_grade (float): The new grade or value.

    Returns:
        float: The percentage decrease as a decimal value.
    """
    return (old_grade - new_grade) / old_grade

def discount_price(price: Union[int,float], discount: Union[int,float]) -> float:
    """
    Calculate the discounted price based on the original price and discount percentage.

    Parameters:
    price (float): The original price before applying the discount.
    discount (float): The discount percentage to be applied, expressed as a decimal value.

    Returns:
    float: The discounted price calculated by multiplying the original price by (1 - discount).
    """
    return price * (1 - discount)

def body_mass_index(weight: Union[int,float], height: Union[int,float]) -> float:
    """
    Calculate the Body Mass Index (BMI) using weight and height.

    The Body Mass Index (BMI) is a numerical value calculated using a person's
    weight (in kilograms) divided by the square of their height (in meters).

    Args:
        weight (float): The weight of the individual in kilograms.
        height (float): The height of the individual in meters.

    Returns:
        float: The Body Mass Index (BMI) calculated as weight divided by height squared.
    """
    return weight / (height ** 2)