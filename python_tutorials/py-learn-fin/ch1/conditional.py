age=int(input("enter your age: "))
if age>=18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")

#marks
marks=int(input("enter your marks: "))
if marks>90:
    print("O grade")
elif marks>=80 and marks<=90:
    print("A grade")
elif marks>=70 and marks<=79:
    print("B grade")
elif marks>=60 and marks<=69:
    print("C grade")
elif marks>=50 and marks<=59:
    print("D grade")
else:
    print("fail")

#lights
light=input("enter the light: ")
if light=="red":
    print("stop")
elif light=="yellow":
    print("ready")
elif light=="green":
    print("go")
else:
    print("broken")