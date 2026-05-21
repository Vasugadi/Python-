class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def calc_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"your avg score is:",sum/3)

s1=Students("sai",[90,80,70])
s2=Students("sai1",[90,80,70])
s1.calc_avg()
s2.calc_avg()
s1.name="hania"
s1.calc_avg()