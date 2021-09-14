
# jagger adams
# 09.13.21
# module 2 project

# set variables 

# set maximum and minimum weight
max_weight = 100
min_weight = 0.25

# set price per pound
ppp = 7.99

# customer order 
weight = round(float(input("Enter cheese order weight (numeric value): ")),2)


# item avalibility conditional statement

# oversized order
if weight > 100:
    print(f"{weight} lbs is more than currently is available in stock.")

# undersized order
elif weight < 0.25:
    print(f"{weight} lbs is below the minimum order amount.")
    
# fufilled order
else:
    subtotal = (weight*ppp)
    tax = (subtotal*0.07)
    total = (subtotal+tax)
    print(f"{weight} lbs of cheese costs ${total}.")
