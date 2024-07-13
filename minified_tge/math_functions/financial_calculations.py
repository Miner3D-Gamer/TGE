def calculate_present_value(principal,rate,years):return principal*pow(1+rate/100,years)
def percentage_increase(old_grade,new_grade):A=old_grade;return(new_grade-A)/A
def percentage_decrease(old_grade,new_grade):A=old_grade;return(A-new_grade)/A
def discount_price(price,discount):return price*(1-discount)
def body_mass_index(weight,height):return weight/height**2