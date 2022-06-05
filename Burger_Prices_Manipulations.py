#Calculations on prices of burgers/
#This script`s aim is to help manage some basic /
#calculations regarding running a restaurant.

#First, the msot important thing - list of sandwiches
burgers = ["BBQ", "Classic", "Polish", "hawaian", "chipotle", "vege", "keto-burger", "fancy"]
#Pricing for each burger (indexes have a corresponding numbers)
prices = [30, 25, 40, 20, 20, 35, 50, 35]
#List of how many customers bought of each burger
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#Aim in this part was to calculate a total pricing for burgers
total_price = 0
for price in prices:
  total_price += price
print (total_price)
#Here we calculate average price for a burger
average_price = total_price / len(prices)
print ("Average Burger Price:")
print (average_price)
#Here we`ve did a little discount to encourage more customers /
#to visit our restaurant.
new_prices = [price - 5 for price in prices]
print (new_prices)

#Here we want to knwo how much profit did we make
total_revenue = 0

for element in range(len(burgers)):
  total_revenue += prices[element]
  total_revenue += last_week[element]
print ("Total revenue: " + str(total_revenue))
average_daily_revenue = total_revenue / 7
print ("Average daily revenue: ", int(average_daily_revenue))

#The code below aims to cut-off all the burgers that are cheaper than 30$ /
#so that we can advertise them
burgers_under_30 = [burgers[i] for i in range(len (burgers)) if prices[i] < 30]
print (burgers_under_30)
