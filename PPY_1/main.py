#zad1
a = "Python 2023"
b = "Python 2023"
c = "Python 2023"
print(a == b)
print(b == c)
print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

c = "Java 11"
print(b == c)
print(type(c))
print(hex(id(c)))

#zad2
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

print("+ -> adding", "- -> substraction", "* -> multiplication", "/ -> division", sep="/n")
operator = input("Enter operator: ")

if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)
else:
    print("Error")

#zad3
