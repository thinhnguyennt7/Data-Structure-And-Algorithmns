def Answer(str):
    holder = ""
    stack = []
    holder1 = ""
    i = 0
    total = 0

    while i < len(str):
        if str[i] not in "+-*/^":
            holder += str[i]
            i += 1
        else:
            stack.append(int(holder))
            if str[i] == '+':
                holder = ""
            elif str[i] == '-':
                holder = "-"
            i += 1


    stack.append(int(holder))
    # print("stack", stack)

    for j in stack:
        total += j

    print(total)


# print(Answer("30+50-20"))
Answer("30*10")
