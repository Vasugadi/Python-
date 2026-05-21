marks={}
phy=int(input("enter the vakue of phys:"))
chem=int(input("enter the vakue of chem:"))
math=int(input("enter the vakue of math:"))

# marks["phy"]=phy
# marks["chem"]=chem
# marks["math"]=math

# print(marks)

marks.update({"phy":phy,"chem":chem,"math":math})

print(marks)

set={9,"9.0"}
print(set)
print(type(set))

s={("float",9.0),("int",9)}
print(s)