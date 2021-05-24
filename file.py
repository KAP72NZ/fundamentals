num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #type check
string = 'Hello World' # Data Types
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Tuples
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms') #Tuples change value
print(person['name']) #log statement
person['name'] = 'George' #function return
person['eye_color'] = 'blue' #function return
print(fruit[2]) #log statement

if num1 > 45:
    print("It's greater")
else:
    print("It's lower") #conditional if,else

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #conditional if,else if,else

for x in range(5):
    print(x) #for loop 
for x in range(2,5):
    print(x) #for loop
for x in range(2,10,3):
    print(x) #for loop
x = 0
while(x < 5):
    print(x)
    x += 1  #while loop

pizza_toppings.pop() #List delete value
pizza_toppings.pop(1) #List delete value

print(person) #log statement
person.pop('eye_color') #List delete value
print(person) #log statement

for topping in pizza_toppings: 
    if topping == 'Pepperoni':
        continue  
    print('After 1st if statement')
    if topping == 'Olives':
        break    

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)