import operator




dicti  = {
    1: "hello",
    9: "hi",
    5: "9999",
    3: "abc"




}

dict1 = sorted(dicti.items(), key = operator.itemgetter(0,1), reverse=True)

list1 = list(dicti.keys())
print(list1)

print(dict1)

del dict1[1]
print(dict1)





dict3 = { }

dict3[0] = "abc"
dict3[3] = 9999

print(dict3)






