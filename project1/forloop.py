friends = ["Ebbin", "Jacob", "Babu"]
print(len(friends))
for name in friends:
    print(name)

for index in range(len(friends)):
    print(index)
    print(friends[index])


def raise_to_power(base,power):
    result = 1
    for index in range(power):
        result = result*base
    return result

print(raise_to_power(3,5))

def translate(phrase):
    for letter in phrase:
        if letter in "AEIOUaeiou":
            print("vowel is present")
        else:
            print("vowel not present")

translate("ebbin")

def functionname(name):
    print(name)
    return len(name)

print(functionname("ebbin"))

for letter in "name":
    print(letter)
