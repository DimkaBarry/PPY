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
#num_1 = int(input("Enter first number: "))
#num_2 = int(input("Enter second number: "))

#print("+ -> adding", "- -> substraction", "* -> multiplication", "/ -> division", sep="\n")
#operator = input("Enter operator: ")

#if operator == "+":
#    print(num_1 + num_2)
#elif operator == "-":
#    print(num_1 - num_2)
#elif operator == "*":
#    print(num_1 * num_2)
#elif operator == "/":
#    print(num_1 / num_2)
#else:
#    print("Error")

#zad3
answer_count = 0
questions = ["Jak masz na imie i nazwisko:",
             "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ",
             "W jakich okolicznościach czytasz książki najczęściej?",
             "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
             "Po książki w jakiej formie sięgasz najczęściej?",
             "Ile książek czytasz średnio w ciągu roku?",
             "Jak często średnio czytasz książki?",
             "Po jakie gatunki książek sięgasz najczęściej?"]

dict = {questions[0]:[],
        questions[1]:[],
        questions[2]:[],
        questions[3]:[],
        questions[4]:[],
        questions[5]:[],
        questions[6]:[],
        questions[7]:[]}

dict[questions[0]].append(input("Podaj odpowiedz: "))

print(questions[1], "Można udzielić jednej odpowiedzi", "Oglądanie telewizji/filmów/seriali", "Słuchanie muzyki", "Podrożowanie", sep="\n")
dict[questions[1]].append(input("Podaj odpowiedz: "))

print(questions[2], "Można zaznaczyć kilka odpowiedzi", "Podczas podróży", "W czasie wolnym (po pracy, na urlopie)", "podczas pracy/nauki (to ich element)", sep="\n")
answer_count = int(input("Ile odpowiedzi chcesz podać: "))
if(answer_count == 0):
    print("Proszę zaznaczyć chociaż")
    answer_count = int(input("Ile odpowiedzi chcesz podać: "))
for i in range(answer_count):
    dict[questions[2]].append(input("Podaj odpowiedz: "))

print(questions[3], "Można udzielić jednej odpowiedzi", "Chęć poszerzenia wiedzy", "Czytanie mnie relaksuje/odpręża", "Fakt, że czytanie jest modne", sep="\n")
dict[questions[3]].append(input("Podaj odpowiedz: "))

print(questions[4], "Można udzielić jednej odpowiedzi", "Papierowej (tradycyjnej)", "e-booki (książki elektroniczne) na komputerze", "e-booki na answerslecie/telefonie", sep="\n")
dict[questions[4]].append(input("Podaj odpowiedz: "))

print(questions[5], "Można udzielić jednej odpowiedzi", "0", "Żadnej w całości - jedynie fragmenty", "1", sep="\n")
dict[questions[5]].append(input("Podaj odpowiedz: "))

print(questions[6], "Można udzielić jednej odpowiedzi", "Codziennie", "Raz w tygodniu", "Raz w miesiącu", sep="\n")
dict[questions[6]].append(input("Podaj odpowiedz: "))

print(questions[7], "Można zaznaczyć kilka odpowiedzi", "Kryminały/thrillery", "Fantastykę", "Historyczne", sep="\n")
answer_count = int(input("Ile odpowiedzi chcesz podać: "))
for i in range(answer_count):
    dict[questions[7]].append(input("Podaj odpowiedz: "))

for k, v in dict.items():
    for i in v:
        print("Pytanie: " + k + "\n", "Odpowiedź: " + i)