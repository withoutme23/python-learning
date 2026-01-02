name = input("Podaj swoje imię: ")
age = int(input("Podaj swój wiek: "))

if age >= 18:
    print("Dostęp dozwolony")
else:
    print("Dostęp zabroniony")

print(f"Cześć, {name}!")
