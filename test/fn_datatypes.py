#!/usr/bin/env python3

# Function DataTypes
def datatypes():
    # Data Types Usage
    print("Data Types Usage")
    # define integer_1 to 22
    integer_1=22
    print ("integer_1 is type", type(integer_1), "with value:", integer_1,"\n")

    # define float_1 to 3.14
    float_1=3.14
    print ("float_1 is type", type(float_1), "with value:", float_1,"\n")

    print("## define string_1 to \"this is a string\" ##")
    string_1="this is a string"
    print ("string_1 is type", type(string_1), "with value:", string_1,"\n")

    print("## Splitting string to List using string_var.split(" ")  ##")
    string_1=string_1.split(" ") # string_1 is converted from string to a list 
    print(string_1,"\n")

    print("## Joining List back to string using \"-\".join(string_var) ##")
    string_1="-".join(string_1) # string_1 is converted from list to strings
    print(string_1,"\n")

    print("## Print string_1 in all lowecase ##")
    print(string_1.lower(),"\n")

    print("## Print string_1 in all UPPERCASE ##")
    print(string_1.upper(),"\n")

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

    list_2=[1,2,3,4]
    print ("list_2 is type", type(list_2), "with value", list_2)
    print("The minimum number is:", min(list_2))
    print("The maximum number is:", max(list_2),"\n")

    # List can be overwritten/append/extend, but not Tuple
    print("## Overwrite list_1[0] with 999 ##")
    list_1[0]="999"
    print ("list_1 is type", type(list_1), "with value", list_1)
    print ("list_1[0] is type", type(list_1[0]), "with new value", list_1[0],"\n")

    tuple_1=(5,6,7,8)
    print ("tuple_1 is type", type(tuple_1), "with value", tuple_1)
    print ("tuple_1[0] is type", type(tuple_1[0]), "with value", tuple_1[0],"\n")

    #print ("dictionary_1.key[1] is type", type(dictionary_1.key[1]), "with value", dictionary_1.key[1])
    dictionary_1={9: 'nine', 10: 'geek'}
    print ("dictionary_1 is type", type(dictionary_1), "with value", dictionary_1,"\n")

datatypes()
