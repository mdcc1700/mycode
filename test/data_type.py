#!/usr/bin/env python3

#!usr/bin/python3

integer_1=22
print ("integer_1 is type", type(integer_1), "with value:", integer_1,"\n")

float_1=3.14
print ("float_1 is type", type(float_1), "with value:", float_1,"\n")

string_1="string"
print ("string_1 is type", type(string_1), "with value", string_1,"\n")

boolean_1=True
boolean_0=False
print ("boolean_0 is type", type(boolean_0), "with value", boolean_0)
print ("boolean_1 is type", type(boolean_1), "with value", boolean_1,"\n")

list_1=[1,'2',3.14,True]
print ("list_1 is type", type(list_1), "with value", list_1)
print ("list_1[0] is type", type(list_1[0]), "with value", list_1[0])
print ("list_1[1] is type", type(list_1[1]), "with value", list_1[1])
print ("list_1[2] is type", type(list_1[2]), "with value", list_1[2])
print ("list_1[3] is type", type(list_1[3]), "with value", list_1[3],"\n")

# List can be overwritten/append/extend, but not Tuple
list_1[0]="999"
print ("list_1 is type", type(list_1), "with value", list_1)
print ("list_1[0] is type", type(list_1[0]), "with new value", list_1[0],"\n")

tuple_1=(5,6,7,8)
print ("tuple_1 is type", type(tuple_1), "with value", tuple_1)
print ("tuple_1[0] is type", type(tuple_1[0]), "with value", tuple_1[0],"\n")

dictionary_1={9: 'nine', 10: 'geek'}
print ("dictionary_1 is type", type(dictionary_1), "with value", dictionary_1)
#print ("dictionary_1.key[1] is type", type(dictionary_1.key[1]), "with value", dictionary_1.key[1])


# Remove space between 2 variables
a="World"
print("Hello",a)
print("Hello{}".format(a))
