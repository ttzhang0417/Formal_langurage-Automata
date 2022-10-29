def replace(P_dic, B, V):
    temp_list = []
    for C in P_dic[B]:
        if(C not in V):
            temp_list.append(C)
        else:
            C_list = replace(P_dic, C, V)
            for i in C_list:
                temp_list.append(i)
    return  temp_list
def del_singleness(V, T, S, P_dic):
    P_dic_new = {}
    for key, values in P_dic.items():
        for value in values:
            if(value not in V):
                if(key not in P_dic_new):
                    P_dic_new[key] = [value]
                else:   P_dic_new[key].append(value)
            else:
                value_new = replace(P_dic, value, V)
                for i in value_new:
                    if(key not in P_dic_new):
                        P_dic_new[key] = [i]
                    else:
                        P_dic_new[key].append(i)
    #   去重操作(去掉列表values里的重复)
    P_dic_new2 = {}
    for key,values in P_dic_new.items():
        values_new = list(set(values))
        P_dic_new2[key] = values_new
    return P_dic_new2