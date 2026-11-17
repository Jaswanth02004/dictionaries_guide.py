#ONE
'''
a = {"name":"jaswanth",  "age":22}
print(dict(a))
print(a["name"])
'''

#TWO
'''
a = {"name": 'jaswanth', 'age':"22"}
a["name"] = 'jas'
print(a)
'''

'''
#THREE
a = {"name": 'jaswanth', 'age':"22"}
print(a.pop("name"))    #reutrns 'jaswanth'
print(a.popitem())  #returns last element
'''


#THREE

a = {"a":1, "b":2, "c":3, "d":4}

'''
for key in a:
    print(key)
print()

for value in a.values():
    print(value)
print()

for key,value in a.items():
   print(key,"=", value)
'''

#FOUR "NESTED DICTIONARIES"
'''
dict_s ={
"Myself":{
"name":'Jaswanth',
"age": 22
    }}
print(dict_s)
print(dict_s["Myself"]["name"])
'''

#FIVE
'''
a = {"a":1, "b":2}
a["c"] = 3
print(a)
'''

#SIX
'''
a = {"a":1, "b":2}
print(a.get("c",3))
'''

#SEVEN  "DOUBLING ELEMENTS INSIDE DICT WOTHOUT WRITING SEPARATE CODE"
'''
a = {"a":1, "b":2}
aa = {p:q*2 for p,q in a.items()}
print(aa)
'''


#EIGHT "JOINT's"
a = {"a":1, "b":2}
b = {"b":2, "c":4}
print(a.keys()-b.keys())    #{'a'}
print(a.keys()&b.keys())    #{'b'}
print(a.keys()^b.keys())    #{'a','c'}
print(a.keys()| b.keys())   #{'c', 'a', 'b'} "THREE UNIQUE KEY's"




















