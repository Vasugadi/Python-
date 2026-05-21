#type conversion --- intrepreter does 
#type casting  --- manually 
#type conversion
a=2
b=4.25
sum=a+b
print(sum) # float is superior to int   

#type casting
a=2
b="3"
#sum=a+b
#print(sum) # error
sum=str(a)+b 
print(sum) # string is superior to int
  #or
sum=a+int(b) 
print(sum)