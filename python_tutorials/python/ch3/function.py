# 1. concatenation
st1="hello"
st2=" world"
concat=st1+st2
print(concat)

# 2. string length
st="hello world"
length=len(st)
print(length)

# 3. string slicing
st="hello world"
sliced=st[0:5] #hello
print(sliced)

# 4. string replace
st="hello world"
replaced=st.replace("world","python") # world is instead of python
print(replaced)

#indexing
st="hello world"
index=st.index("o")
t=st[0]
print(index)

st[2]='b'#assagining is impossible in python

#slicing
#ste[starting:ending]#ending is not included

str="apna sapna"
print(str[0:3])#apn
print(str[0:5:2])#apn
print(str[5:len(str)])
print(str[5:])# sapna
print(str[:5])#apna
print(str[::2])#apnspn
#str[starting:ending:step]
str[-1:]
str[-5:-2]
str[-3:-1]

