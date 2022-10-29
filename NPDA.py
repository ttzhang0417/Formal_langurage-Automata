import re
def write_NPDA( Q, Sigma, Gamma, Delta, q0, z, F):
    path = r'NPDA.txt'
    f = open(path, 'w+', encoding='utf-8')
    f.write("Q = {")
    for i in range(len(Q)):
        f.write(Q[i])
        if(i != len(Q)-1):
            f.write(", ")
    f.write("}\n")
    f.write("∑ = {")
    for i in range(len(Sigma)):
        f.write(Sigma[i])
        if (i != len(Sigma) - 1):
            f.write(", ")
    f.write("}\n")
    f.write("Γ = {")
    for i in range(len(Gamma)):
        f.write(Gamma[i])
        if (i != len(Gamma) - 1):
            f.write(", ")
    f.write("}\n")
    f.write("δ={\n")
    for key, values in Delta.items():
        f.write("(" + key + ")")
        f.write("={")
        value_list = values.split("|")
        for i in range(len(value_list)):
            f.write(value_list[i])
            if (i != len(value_list) - 1):
                f.write("|")
        f.write("}\n")
    f.write("}\n")
    f.write("q0 = " + q0 + '\n')
    f.write("z = " + z + "\n")
    f.write("F = " + F)
    f.close()
def readNPDA():
    f = open('NPDA.txt',  encoding="utf-8")
    lines = f.readlines()
    Q = []
    Sigma = []
    Gamma = []
    Delta = {}
    line = re.findall(r"{(.*?)}", lines[0])[0]  # 取 ｛｝之间内容
    line = str(line).replace(" ", "")  # 去除空格
    for i in line.split(","):  # 以逗号分隔
        Q.append(i)
    line = re.findall(r"{(.*?)}", lines[1])[0]
    line = str(line).replace(" ", "")
    for i in line.split(","):
        Sigma.append(i)
    line = re.findall(r"{(.*?)}", lines[2])[0]
    line = str(line).replace(" ", "")
    for i in line.split(","):
        Gamma.append(i)
    start = 0
    end = 0
    for i in range(3, len(lines)):
        if(lines[i] == 'δ={\n'):
            start = i
        if(lines[i] == '}\n'):
            end = i
            break
    for index in range(start+1, end):
        line = lines[index]
        line = line.replace("\n",'')
        l_list = line.split("=")
        left = l_list[0]
        right = l_list[1]
        left = left.replace("(","")
        left = left.replace(")","")
        right = right.replace("{", "")
        right = right.replace("}", "")
        Delta[left] = right
    q0 = "q0"
    z = "z"
    F = "q2"
    f.close()
    return Q, Sigma, Gamma, Delta, q0, z, F
def toNPDA(Path):
    f = open(Path, encoding="utf-8")
    lines = f.readlines()
    M = ["Q", "∑", "Γ", "δ", "q0", "z", "F"]
    Q = ["q0", "q1", "q2"]
    Sigma = []
    Gamma = []
    q0 = "q0"
    z = "z"
    F = "q2"
    Delta = {}

    for line in lines:
        for i in line:
            if i.islower():
                if i not in Sigma:
                    Sigma.append(i)

    for line in lines:
        Gamma.append(line.split("-")[0])

    Gamma.append("z")

    print("M:{}".format(M))

    print("Q:{}".format(Q))
    print("∑:{}".format(Sigma))
    print("Γ:{}".format(Gamma))

    print("q0:{}".format(q0))
    print("z:{}".format(z))
    print("F:{}".format(F))

    Delta['q0,ε,z'] = 'q1,Sz'
    Delta['q1,ε,z'] = 'q2,z'

    for line in lines:
        gamma_opt = line.split('->')[0]
        line_right = line.split('->')[1].strip()
        for x in line_right.split('|'):
            sigma_opt = x[0]
            q_opt = 'q1'
            if len(x) == 1:
                stack_opt = 'ε'
            else:
                stack_opt = x.replace(x[0], '')

            key_opt = q_opt + ',' + sigma_opt + ',' + gamma_opt
            value_opt = q_opt + ',' + stack_opt

            if key_opt not in Delta.keys():
                Delta[key_opt] = value_opt
            else:
                old_value = Delta[key_opt]
                value_opt = old_value + '|' + value_opt
                Delta.update({key_opt: value_opt})
    print("δ:{}".format(Delta))
    write_NPDA(Q, Sigma, Gamma, Delta, q0, z, F)