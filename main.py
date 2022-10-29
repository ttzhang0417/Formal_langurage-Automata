import re
from remove_useless import del_useless
from remove_null import  del_null
from remove_singleness import del_singleness
from remove_left import  *
from Greibach import *
from write_Greibach import *
from NPDA import *

#读取file.txt, 共四行
f = open("file1.txt", encoding="utf-8")
lines = f.readlines()

#读取 V T P S，
V = []
T = []
P = []
S = []


line = re.findall(r"{(.*?)}", lines[0])[0]  # 取 ｛｝之间内容
line = str(line).replace(" ", "")   # 去除空格
for i in line.split(","): # 以逗号分隔
    V.append(i)


line = re.findall(r"{(.*?)}", lines[1])[0]
line = str(line).replace(" ", "")
for i in line.split(","):
    T.append(i)


line = re.findall(r"{(.*?)}", lines[2])[0]
line = str(line).replace(" ", "")
for i in line.split(","):
    P.append(i)


line = re.findall(r"{(.*?)}", lines[3])[0]
line = str(line).replace(" ", "")
for i in line.split(","):
    S.append(i)


# 将P中的式子用字典表示
P_left = []
P_right = []
P_dict = {}
# “->” 将产生式箭头左边放在P_left 里
for i in P:
    P_left.append(i.split("->")[0])
# “->” 将产生式箭头左边放在P_right 里
for i in P:
    P_right.append(i.split("->")[1])
for i in range(len(P)):
    P_dict[str(P_left[i])] = P_right[i].split("|")
print("V:", V)
print("T:", T)
print("S:", S)
print("P_dict:", P_dict)

P_dict, V, T = del_useless(V, T, S, P_dict)
print("消除无用符号后：", P_dict)
P_dict = del_null(V, T, S, P_dict)
print("消除空产生式后P_dict：", P_dict)
P_dict = del_singleness(V, T, S, P_dict)
print("消除单一产生式后P_dict：", P_dict)
P_dict = del_indirectLeft(V, T, S, P_dict)
print("消除间接左递归后:", P_dict)
P_dict, V= del_directLeft(V, T, S, P_dict)
print("消除直接左递归后：", P_dict)
P_dict,V, T = del_useless(V, T, S, P_dict)
print("消除无用符号后：", P_dict)
P_dict = del_null(V, T, S, P_dict)
print("消除空产生式后P_dict：", P_dict)
P_dict = beginLower(V, T, S, P_dict)
print("以终结符号打头P_dict：", P_dict)
P_dict = toGreibach(V, T, S, P_dict)
print("化为Greibach范式P_dict：", P_dict)
Path = write_Greibach(P_dict)
toNPDA(Path)
