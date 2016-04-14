#2.10  Exercises

print ("Exercise 1")#Exercise 1
#Repeating my advice from the previous chapter, whenever you learn a new feature, you should try it out in interactive mode and make errors on purpose to see what goes wrong.
#We’ve seen that n = 42 is legal. What about 42 = n?
#How about x = y = 1?
#In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
#What if you put a period at the end of a statement?
#In math notation you can multiply x and y like this: x y. What happens if you try that in Python?



print ("Exercise 2")
#Practice using the Python interpreter as a calculator:
#The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5?
r = 5
pi = 3.141592653589793
volume = (4/3) * pi * r**3
print("the volume of a sphere with radius 5 is: ", volume)

#Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
book_price = 24.95
discount = 0.6
amount_books = 60
shipping = 3 + (amount_books - 1)* 0.75
wholesale = amount_books * (book_price * discount) + shipping
print("Wholesale for ", amount_books, "copies is:$",wholesale)

#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

""""in seconds"""
easy_pace = (8*60)+15
tempo = (7*60)+12
run_time = 2 * easy_pace + 3 * tempo
run_minutes = run_time / 60
time = int(run_minutes)-8
print("I get home for breakfast at: 7:",time, "am")
""""in minutes"""
easy_pace = 8.25
tempo = 7.2
run_time = 2 * easy_pace + 3 * tempo
time = int(run_time)-8
print("I get home for breakfast at: 7:",time, "am")



