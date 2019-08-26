import os


#获取相对路径

currentpath = os.path.realpath(__file__)  #获取当前路径
packagepath = os.path.dirname(currentpath) #获取当前路径的包名
projectpath = os.path.dirname(packagepath) #获取当前路径的project名
print(currentpath)
print(packagepath)
print(projectpath)
datapath = os.path.join(projectpath,"common","data.xlsx") #切换到project下其他包里的文件路径
print(datapath)