with open("practice.txt", "w") as file:
    file.write("Hello World!")
    file.write("This is a test file.")
    file.write("I hope it works.")


with open("practice.txt", "r") as file:
    data=file.read()
    new_data=data.replace("test", "practice")
    print(new_data)
    word="learning"
    if(new_data.find(word)==-1):
        print("The word is not in the file.")
    else:
        print("The word is in the file.")


def check_for_line():
    word="learning"
    with open("practice.txt", "r") as file:
        data=file.readlines()
        for line in data:
            if(line.find(word)==-1):
                print("The word is not in the line.")
            else:
                print("The word is in the line.")

check_for_line()