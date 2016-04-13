#Excersise 1
print("Excersise 1")
print("Hello World")
print(2++2)
print(2)

#Excersise 2
#How many seconds are there in 42 minutes and 42 seconds?
print("Excersise 2")
minutes = 42
seconds = 42
seconds = seconds + (minutes * 60)
print (seconds)

#How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
print("Excersise 2.1")
km = 10
ml = km / 1.61
print(ml)

#If you run a 10 kilometer race in 42 minutes 42 seconds,
 # what is your average pace (time per mile in minutes and seconds)?
 # What is your average speed in miles per hour?
print("Excersise 2.3")
distance_km = 10
distance_ml = distance_km/1.61
total_seconds = (42*40)+42
time_hour = total_seconds / (60*60)
time_mile = total_seconds/distance_ml
average_pace = distance_ml/total_seconds
average_speed = distance_ml/time_hour

print(total_seconds)
print(distance_ml)
print("average pace in miles per second =", + average_pace)
print("average speed in miles per hour =", + average_speed)