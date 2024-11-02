#type: ignore
def is_prime(number):
 B=False;A=number
 if A<=1:return B
 for C in range(2,A):
  if A%C==0:return B
 return True
def is_palindrome(string):A=string;return A==A[::-1]
def is_leap_year(year):A=year;return A%4==0 and(A%100!=0 or A%400==0)
def is_even(number):return number%2==0
def is_odd(number):return number%2==1
__all__=['is_prime','is_palindrome','is_leap_year','is_even','is_odd']