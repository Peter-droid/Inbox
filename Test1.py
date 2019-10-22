import os
import re
path = r'C:\Users\12586\Documents\test' #文件在我的电脑上的地址
os.chdir(path)
text1 = open('test1.txt', 'r')
text2 = open('test2.txt', 'r')
list1 = text1.read()
list2 = text2.read()
def count(list):
    Times = []
    Objects = []
    list = re.split(r'[,."\s]', list)
    iteration_list = set(list)
    for i in iteration_list:
        Times.append(list.count(i))
        Objects.append(i)
    Unsorted_result = dict(zip(Objects, Times))
    Sorted_result = sorted(Unsorted_result.items(), key = lambda x:(x[1], x[0]), reverse = True)
    while(True):
        key = input("""Do you want to see the whole result or top ten results?
        Enter \"Yes\" or \"No\" please:""")
        if key == "Yes":
            print(Sorted_result)
            break
        elif key == "No":
            for i in range(0, 10):
                print(Sorted_result[i])
            break
        else:
            print("I only accept \"Yes\" or \"No\", please enter again.")

count(list1)
count(list2)
