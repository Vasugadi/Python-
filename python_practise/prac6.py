class su:
    __name="hello"
    
    def __hello(self):  # 定义一个私有方法 __hello，接收一个 self 参数
        print("hello")  # 打印 "hello" 和 self.name 的值
        
    def display(self):
        self.__hello()
        print("name is:", self.__name)
s1=su()
s1.display()