#!/usr/bin/env python3

#define proto variable
proto = ["ssh", "http", "https"]

#define protoa variable
protoa = ["ssh", "http", "https"]

#print proto variable
print(proto)

proto.extend("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
print(protoa,"\n")

#define proto2 variable
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto3 = [ 1,2,3,4 ] # a list of common ports

#demonstrate lists method with extend
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)

#demonstrate lists method with append
proto2.append(proto3) # pass proto2 as an argument to the append method
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
print(protoa[4][4][3])

