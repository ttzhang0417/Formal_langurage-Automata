'''
消除无用符号
'''
# 判断字符串a中的每个字符是否都在列表N中，都在返回True
def is_contained(a, N, V):
    i = 0
    # 考虑有A+这类符号的情况
    while(i < len(a)):
        if a[i] not in V:
            i = i + 1
            continue
        else:
            if(i+1<len(a) and a[i+1]=='+'):
                temp = a[i]+'+'
                if(temp not in N):
                    return False
                else:
                    i = i + 2   #跳过+号
            else:
                if(a[i] not in N):
                    return False
                else:
                    i = i + 1
    return True
# 判断字符串a中是否存在字符在列表NM中，存在则返回True
def has_contained(a, NM, V):
    i = 0
    # 考虑有A+这类符号的情况
    while (i < len(a)):
        if a[i] not in V:
            i = i + 1
            continue
        else:
            if (i+1 <len(a) and a[i + 1] == '+'):
                temp = a[i] + '+'
                if (temp in NM):
                    return True
                else:
                    i = i + 2  # 跳过+号
            else:
                if (a[i] in NM):
                    return True
                else:
                    i = i + 1
    return False
# 字符串转列表，eg. 'aBcA+'转化为['a', 'B', 'c', 'A+']
def strToList(str, T):
    i = 0
    str_list = []
    while(i < len(str)):
        if(str[i] in T):
            str_list.append(str[i])
            i = i + 1
        else:
            if(str[i] == 'ε'):
                str_list.append(str[i])
                i = i + 1
            else:
                if(i+1 < len(str) and str[i+1] == '+'):
                    str_list.append(str[i]+'+')
                    i = i + 2
                else:
                    str_list.append(str[i])
                    i = i + 1
    return str_list
def del_useless(V, T, S, P_dict):
    #   计算“产生的”符号集N：每个T中的符号都是产生的，若A→a∈P且a中符号都是产生的，则A是产生的
    V_temp = list(V)
    N = []
    for i in T:
        N.append(i)
    for i in range(len(V)):
        for j in V_temp:  # j是['S', 'A', 'B', 'C', 'D', 'E']中的一个元素
            flag = False
            for a in P_dict[j]:  # 若j是S,则a是dic[s]中的一个元素,即['0', '0A', 'E']中的一个元素
                if (is_contained(a, N, V)):  # 若a中的每个符号都属于N
                    V_temp.remove(j)
                    N.append(j)
                    flag = True
                    break
            if (flag):
                break
    print("产生的符号集N：", N)
    #   2、计算“可达的”符号集M：开始符号S是可达的，A→a∈P且A是可达的，则a中的符号都是可达的。
    M = []
    M.append(S[0])
    visited = []

    def Reach(begin):
        visited.append(begin)
        for value in P_dict[begin]:
            value_list = strToList(value, T)
            for item in value_list:
                if(item not in M and item != 'ε'):
                    M.append(item)
                # 若item是非终结符且item未被遍历过
                if(item not in T and item not in visited and item !='ε'):
                    Reach(item)
    Reach(S[0])
    print("可达的符号集M：", M)
    #   3、计算不可产生或者不可达的集合NM，消除P中含有NM的式子
    NM = []
    Q = []  # Q是V和T的并集
    for i in T:
        Q.append(i)
    for i in V:
        Q.append(i)
    for i in Q:
        if (i in N and i in M):
            continue
        else:
            NM.append(i)
    print("无用符号集NM：", NM)
    # 消除无用符号，字典转列表（字典无法边遍历边删除）
    data = P_dict.items()
    P_list = list(data)
    P_dict_new = {}
    T_new = list(T)
    for i in P_list:
        if (i[0] in NM):
            continue
        else:
            for j in i[1]:
                if (has_contained(j, NM, V) == False):
                    key = i[0]
                    if (i[0] in P_dict_new):
                        P_dict_new[key].append(j)
                    else:
                        temp = []
                        temp.append(j)
                        P_dict_new[str(key)] = temp
    index = len(V)-1
    while(index >= 0):
        if V[index] in NM:
            V.pop(index)
        index = index -1
    # 更新T
    T_new = set()
    for key,values in P_dict_new.items():
        for value in values:
            value_list = strToList(value, T)
            for i in value_list:
                if (i in T):
                    T_new.add(i)
    T_new = list(T_new)
    return P_dict_new, V, T_new
