# #for loops are generally used for sequential traversal
# #for traversing a list or string tuples


# for i in range(1,10):
#     print(i)
# #range(1,10) will print numbers from 1 to 9

# for i in range(10,0,-1):
#     print(i)

# #range(10,0,-1) will print numbers from 10 to 1


# #loops are used for sequential traversal
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     print(i)

# #for else
# #for i in list:
# #    print(i)
# #    break
# #else:
# #    print("no break")

# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     print(i)
# else:
#     print("no break")

#string
str="apnacollege"
for i in str:
    print(i)

#
st="apnacollege"
for i in st:
    if i=="c":
        print("found",i)
        break
    print(i)
else:
    print("not found")