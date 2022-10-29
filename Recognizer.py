from NPDA import *
def recognize(input_str, Delta, z, q0, F):
    # 准备工作
    input_list = list(input_str)
    input_now = 'ε'         # 指向当前输入字符
    stack = []               # 下推栈
    stack.append(z)          # 初始字符入栈
    temp_stack = []          # 临时栈
    q_now = q0               # 当前状态
    stack_top = z            # 栈顶符号
    Delta_now = ''           # 当前的转移函数字符串，格式为‘当前状态，输入符号，栈顶符号’

    while (q_now != F):      # 当前状态非终止状态

        Delta_now = q_now + ',' + input_now + ',' + stack_top
        print(Delta_now)

        if (Delta_now in Delta.keys()):
            values = Delta[Delta_now]

            if len(stack) == 0:
                continue
            else:
                stack.pop(len(stack)-1)
                # 栈顶元素出栈

            transfer_list = values.split('|')
            trans_target = transfer_list[0]         # 选择δ={(p1, A),(p1, B)}中的(p1, A)进行转移
            temp_str = trans_target.split(',')[1]
            temp_stack = list(temp_str)

            # 入栈
            i = len(temp_stack)-1      # 字符串AB*BC从右向左依次入栈
            while (i >= 0):
                if(temp_stack[i] == 'ε'):
                    i = i - 1
                elif (temp_stack[i] == '*' or temp_stack[i] == '+' or temp_stack[i] == "'"):
                    s = temp_stack[i-1] + temp_stack[i]
                    stack.append(s)         # 入栈
                    i = i - 2
                else:
                    stack.append(temp_stack[i])
                    i = i - 1

            temp_stack.clear()
            # 更改Delta_now
            q_now = trans_target.split(',')[0]
            if len(input_list) == 0:
                stack_top = stack[len(stack) - 1]
                input_now = 'ε'
                continue
            else:
                input_now = input_list[0]
                input_list.pop(0)
                stack_top = stack[len(stack)-1]
        else:
            break

    print(stack)
    if(q_now == F and stack[0] == z):
        print("接受")
    elif (q_now != F):
        print("不接受")
    else:
        print("NPDA构造错误，请检查")
input_str = 'bc'        # bc or c
Q, Sigma, Gamma, Delta, q0, z, F = readNPDA()
print("输入字符串为:{}".format(input_str))
recognize(input_str, Delta, z, q0, F)

