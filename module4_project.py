# jagger adams
# 12.15.21
# module 4 project


# define calcCapacity function
def calcCapacity(venueType,maxCapacity):
    # large venue
    if venueType == "L":
        maxCapacity = (int(maxCapacity) * 0.07)
        return maxCapacity
    # small venue
    if venueType == "S":
        maxCapacity = (int(maxCapacity) * 0.3)
        if maxCapacity <= 100:
            maxCapacity = 100
            return maxCapacity
        else:
            return maxCapacity
    # movie theatre
    if venueType == "M":
        maxCapacity = (int(maxCapacity) * 0.3)
        if maxCapacity <= 100:
            maxCapacity = 100
            return maxCapacity
        else:
            return maxCapacity
    # amusment park
    if venueType == "P":
        maxCapacity = (int(maxCapacity) * 0.3)
        return maxCapacity
        
# loop (program start)
while True:
    venueType = input("What is your venue, L(large), S(small), M(movie), P(amusment park): ")
    if len(venueType) == 1:
        
    else:
        print("Your venue type is invalid.")
        continue
    maxCapacity = input("What is the pre-covid max capacity of your venue: ")
    try:
        int(maxCapacity)
    except ValueError:
        print("Your max capacity must be a number.")
        continue
    
    
    
