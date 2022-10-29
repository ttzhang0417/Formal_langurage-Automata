# 字典转列表
def dictTolist(P_dict):
    data = P_dict.items()
    P_list = list(data)
    return P_list
def del_indirectLeft(V, T, S, P_dict):
    P_list = dictTolist(P_dict)
    P_list_new = list(P_list)
    for i in range(len(V)):
        for j in range(0, i):
            # 遍历所有V[i]的产生式
            right = P_list[i][1]
            left = P_list[j][0]
            index = 0
            length = len(right)
            while (index<length):
                # 若V[i]的产生式右部首字母value[0]为V[j], 将首字母V[j]替换为V[j]的右部
                if(right[index][0] == left):
                    temp_i = str(right[index])  # Sa
                    temp_insert = list(P_list[j][1])   # ['Qc','c']
                    temp = []
                    count = 0
                    right.pop(index)
                    for c in temp_insert:
                        right.insert(index, temp_i.replace(left, c, 1))
                index = index + 1
    P_dictnew = {}
    for items in P_list:
        key = items[0]
        values = items[1]
        P_dictnew[key] = values
    return P_dictnew
def del_directLeft(V, T, S, P_dict):
    P_list = dictTolist(P_dict)
    P_list_new = []
    for item in P_list:
        left =  item[0]
        right = item[1]
        upper = []
        lower = []
        temp1 = []
        temp2 = []
        for value in right:
            if(value[0] == left):
                upper.append(value)
            else:    lower.append(value)
        if(len(upper)==0):      # 该式中无直接左递归
            P_list_new.append(item)
            continue
        else:
            V.append(left+'+')
            if(len(lower)==0):  # A->Aa的情况，此时len(lower)=0
                temp1.append(left+'+')
            else:
                for value in lower:
                    temp1.append(value+left+'+')
            for value in upper:
                value_list = list(value)
                value_list.pop(0)
                s = ''
                for j in value_list:
                    s = s + j
                temp2.append(s+left+'+')
            temp2.append('ε')
            temp3 = []
            temp3.append(left)
            temp3.append(temp1)
            temp4 = []
            temp4.append(left+'+')
            temp4.append(temp2)
            P_list_new.append(temp3)
            P_list_new.append(temp4)
    P_dict_new = {}
    for items in P_list_new:
        key = items[0]
        values = items[1]
        P_dict_new[key] = values
    return P_dict_new, V
