def write_Greibach(P_dict):
    path = r'Greibach.txt'
    f = open(path, 'w+')
    for key in P_dict.keys():
        f.write(key + '->')
        for value in P_dict[key]:
            f.write(value)
            if list(P_dict[key]).index(value) < len(list(P_dict[key])) - 1:
                f.write('|')
        f.write(" \n")
    f.close()
    return 'Greibach.txt'




