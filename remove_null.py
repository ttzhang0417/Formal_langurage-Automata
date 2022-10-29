from remove_useless import strToList
# 判断value中所有符号都包含在V0中
def all_null(value, V0):
    for i in value:
        if i not in V0:
            return False
    return True
# 判断value中存在符号包含在V0中
def has_null(value, V0):
    for i in value:
        if i in V0:
            return True
    return False
def del_null(V, T, S, P_dic):
    V0 = ['ε']
    P0 = []
    #   求V0，V0={A属于V，且A能在有限步推出ε}
    for i in V:
        for j in V:
            flag = False
            if j in V0:
                continue
            else:
                values = P_dic[j]
                for value in values:
                    value_list = strToList(value, T)
                    if(all_null(value, V0)):
                        flag = True
                        V0.append(j)
                        break
            if(flag):   break
    #   消除ε产生式
    P_dic_new = {}
    for key, values in P_dic.items():
        for value in values:
            temp_str = value[:]
            v_list = strToList(value, T)
            if(has_null(v_list, V0)):
                if(value == 'ε'):
                    continue
                for i in range(len(v_list)):
                    if(v_list[i] in V0):
                        # 以本身替代
                        if(key not in P_dic_new):
                            P_dic_new[key] = [temp_str]
                        else:
                            P_dic_new[key].append(temp_str)
                        # 以空替代
                        v_list_temp = list(v_list)
                        v_list_temp.pop(i)
                        #   考虑A->B，B->ε的情况
                        if(len(v_list_temp) != 0):
                            str_del = ''.join(v_list_temp)
                            P_dic_new[key].append(str_del)
            elif (key in V0):
                if(value == 'ε'):
                    continue
                else:
                    if(key not in P_dic_new):
                        P_dic_new[key] = [temp_str]
                    else:
                        P_dic_new[key].append(temp_str)
            else:
                if (key not in P_dic_new):
                    P_dic_new[key] = [temp_str]
                else:
                    P_dic_new[key].append(temp_str)
    #   去除values中重复的部分
    P_dic_new2 = {}
    for key, value in P_dic_new.items():
        values = list(set(value))
        P_dic_new2[key] = values
    return P_dic_new2




