
# module one prject
# mr. olson's cumputer science
# by jagger adams

# import modules
import time

# set book cover
author=("H.G.WELLS").center(25)
break_bar=("------------").center(25)
title1=("THE WAR OF").center(25)
title2=("THE WORLDS").center(25)
subtitle=("with an afterword by ISAAC ASIMOV").center(25)

# print book cover 
print(f"""{author}
{break_bar}
{title1}
{title2}
{subtitle}
""")
time.sleep(1)

# ask number of books
quantity=int(input("How many boooks would you like to purchase? "))
time.sleep(1)

# math
price=19.99
sub_total=round((quantity*price),2)
total=round((sub_total+(sub_total*0.07)), 2)

print(f"You bought {quantity} books. They cost ${price} each for a total of ${total} with tax.")
time.sleep(1)
