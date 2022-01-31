import os
'''
class1 = open("class1.txt", "r")
for i in class1.readlines():
    os.system("cp Images/%s.tif class1/" % i.strip())
class1.close()

class2 = open("class2.txt", "r")
for i in class2.readlines():
    os.system("cp Images/%s.tif class2/" % i.strip())
class2.close()
'''
test = open("test.txt", "r")
for i in test.readlines():
    os.system("cp Images/%s.tif test/" % i.strip())
test.close()
