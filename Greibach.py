from remove_left import dictTolist
from remove_useless import strToList
def beginLower(V, T, S, P_dict,):
    P_list = dictTolist(P_dict)
    for i in range(len(P_dict)):
        left = P_list[i][0]
        right = P_list[i][1]
        j = 0
        while (j < len(P_list[i][1])):
            # 非终结符打头
            if(right[j][0] not in T):
                if(right[j][1] == '+'):
                    upper = right[j][0]+'+'
                else:
                    upper = right[j][0]
                temp = right[j]
                right2 = P_dict[upper]
                temp_list = []
                for r in right2:
                    temp_list.append(temp.replace(upper, r, 1))
                P_list[i][1].remove(temp)
                for r in temp_list:
                    P_list[i][1].append(r)
            else:
                j = j + 1
        P_dict_new = {}
    for i in P_list:
         P_dict_new[i[0]] = i[1]
    return P_dict_new
def toGreibach(V, T, S, P_dict):
    P_dict_new = {}
    ref_dict = {}
    for key, values in P_dict.items():
        for value in values:
            value_list = strToList(value, T)
            for i in range(len(value_list)):
                if(value_list[i] in T and i!= 0):
                    left = value_list[i].upper() + '*'
                    ref_dict[left] = value_list[i]
                    value_list[i] = left
            if(key not in P_dict_new):
                P_dict_new[key] =[''.join(value_list)]
            else:
                P_dict_new[key].append(''.join(value_list))
    ref_list = dictTolist(ref_dict)
    for i in ref_list:
        P_dict_new[i[0]] = [i[1]]
    return P_dict_new



