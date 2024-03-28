# Function to convert kilometers to miles
def km_to_miles(km):
    # 1 kilometer is equal to 0.621371 miles
    miles = km * 0.621371
    return miles

# Input kilometers from the user
kilometers = float(input("Enter distance in kilometers: "))

# Convert kilometers to miles using the function
miles = km_to_miles(kilometers)

# Display the result
print("Distance in miles:", miles)
