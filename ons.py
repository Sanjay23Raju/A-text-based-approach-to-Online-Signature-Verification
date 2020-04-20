import numpy as np

file1 = open(r"C:\Users\admin\PycharmProjects\OS\Task 2\U3S10.TXT", "r")
file2 = open(r"C:\Users\admin\PycharmProjects\OS\Task 2\U3S20.TXT", "r")
lines1 = file1.readlines()
lines2 = file2.readlines()
lines1.pop(0)
lines2.pop(0)
# print(lines1)
# print(lines2)
xs1 = []; ys1 = []; az1 = []; al1 = []; pr1 = []
xs2 = []; ys2 = []; az2 = []; al2 = []; pr2 = []

for value1 in lines1:
    # print(value1.split(' '))
    xs1.append(value1.split(' ')[0])
    ys1.append(value1.split(' ')[1])
    az1.append(value1.split(' ')[4])
    al1.append(value1.split(' ')[5])
    pr1.append(value1.split(' ')[6])

for value2 in lines2:
    # print(value1.split(' '))
    xs2.append(value2.split(' ')[0])
    ys2.append(value2.split(' ')[1])
    az2.append(value2.split(' ')[4])
    al2.append(value2.split(' ')[5])
    pr2.append(value2.split(' ')[6])

# print(xs1); print(ys1); print(az1); print(al1); print(pr1)
# print(xs2); print(ys2); print(az2); print(al2); print(pr2)

xExtrema1 = []
yExtrema1 = []
zExtrema1 = []
lExtrema1 = []
pExtrema1 = []
xExtrema2 = []
yExtrema2 = []
zExtrema2 = []
lExtrema2 = []
pExtrema2 = []

for i in range(len(xs1)):
    if i == 0:
        if xs1[i] > xs1[i + 1]:
            xExtrema1.append("b")
        elif xs1[i] < xs1[i + 1]:
            xExtrema1.append("a")
        else:
            # pass
            xExtrema1.append("0")
    elif i == len(xs1) - 1:
        if xs1[i] > xs1[i - 1]:
            xExtrema1.append("b")
        elif xs1[i] < xs1[i - 1]:
            xExtrema1.append("a")
        else:
            # pass
            xExtrema1.append("0")
    else:
        if xs1[i] >= xs1[i - 1] and xs1[i] >= xs1[i + 1]:
            xExtrema1.append("b")
        elif xs1[i] <= xs1[i - 1] and xs1[i] <= xs1[i + 1]:
            xExtrema1.append("a")
        else:
            # pass
            xExtrema1.append("0")
print(xExtrema1)

for i in range(len(ys1)):
    if i == 0:
        if ys1[i] > ys1[i + 1]:
            yExtrema1.append("d")
        elif ys1[i] < ys1[i + 1]:
            yExtrema1.append("c")
        else:
            # pass
            yExtrema1.append("0")
    elif i == len(ys1) - 1:
        if ys1[i] > ys1[i - 1]:
            yExtrema1.append("d")
        elif ys1[i] < ys1[i - 1]:
            yExtrema1.append("c")
        else:
            # pass
            yExtrema1.append("0")
    else:
        if ys1[i] >= ys1[i - 1] and ys1[i] >= ys1[i + 1]:
            yExtrema1.append("d")
        elif ys1[i] <= ys1[i - 1] and ys1[i] <= ys1[i + 1]:
            yExtrema1.append("c")
        else:
            # pass
            yExtrema1.append("0")
print(yExtrema1)

for i in range(len(az1)):
    if i == 0:
        if az1[i] > az1[i + 1]:
            zExtrema1.append("f")
        elif az1[i] < az1[i + 1]:
            zExtrema1.append("e")
        else:
            # pass
            zExtrema1.append("0")
    elif i == len(az1) - 1:
        if az1[i] > az1[i - 1]:
            zExtrema1.append("f")
        elif az1[i] < az1[i - 1]:
            zExtrema1.append("e")
        else:
            # pass
            zExtrema1.append("0")
    else:
        if az1[i] >= az1[i - 1] and az1[i] >= az1[i + 1]:
            zExtrema1.append("f")
        elif az1[i] <= az1[i - 1] and az1[i] <= az1[i + 1]:
            zExtrema1.append("e")
        else:
            # pass
            zExtrema1.append("0")
print(zExtrema1)

for i in range(len(al1)):
    if i == 0:
        if al1[i] > al1[i + 1]:
            lExtrema1.append("h")
        elif al1[i] < al1[i + 1]:
            lExtrema1.append("g")
        else:
            # pass
            lExtrema1.append("0")
    elif i == len(al1) - 1:
        if al1[i] > al1[i - 1]:
            lExtrema1.append("h")
        elif al1[i] < al1[i - 1]:
            lExtrema1.append("g")
        else:
            # pass
            lExtrema1.append("0")
    else:
        if al1[i] >= al1[i - 1] and al1[i] >= al1[i + 1]:
            lExtrema1.append("h")
        elif al1[i] <= al1[i - 1] and al1[i] <= al1[i + 1]:
            lExtrema1.append("g")
        else:
            # pass
            lExtrema1.append("0")
print(lExtrema1)

for i in range(len(pr1)):
    if i == 0:
        if pr1[i] > pr1[i + 1]:
            pExtrema1.append("j")
        elif pr1[i] < pr1[i + 1]:
            pExtrema1.append("i")
        else:
            # pass
            pExtrema1.append("0")
    elif i == len(pr1) - 1:
        if pr1[i] > pr1[i - 1]:
            pExtrema1.append("j")
        elif pr1[i] < pr1[i - 1]:
            pExtrema1.append("i")
        else:
            # pass
            pExtrema1.append("0")
    else:
        if pr1[i] >= pr1[i - 1] and pr1[i] >= pr1[i + 1]:
            pExtrema1.append("j")
        elif pr1[i] <= pr1[i - 1] and pr1[i] <= pr1[i + 1]:
            pExtrema1.append("i")
        else:
            # pass
            pExtrema1.append("0")
print(pExtrema1)

for i in range(len(xs2)):
    if i == 0:
        if xs2[i] > xs2[i + 1]:
            xExtrema2.append("b")
        elif xs2[i] < xs2[i + 1]:
            xExtrema2.append("a")
        else:
            # pass
            xExtrema2.append("0")
    elif i == len(xs2) - 1:
        if xs2[i] > xs2[i - 1]:
            xExtrema2.append("b")
        elif xs2[i] < xs2[i - 1]:
            xExtrema2.append("a")
        else:
            # pass
            xExtrema2.append("0")
    else:
        if xs2[i] >= xs2[i - 1] and xs2[i] >= xs2[i + 1]:
            xExtrema2.append("b")
        elif xs2[i] <= xs2[i - 1] and xs2[i] <= xs2[i + 1]:
            xExtrema2.append("a")
        else:
            # pass
            xExtrema2.append("0")
# print(xExtrema2)

for i in range(len(ys2)):
    if i == 0:
        if ys2[i] > ys2[i + 1]:
            yExtrema2.append("d")
        elif ys2[i] < ys2[i + 1]:
            yExtrema2.append("c")
        else:
            # pass
            yExtrema2.append("0")
    elif i == len(ys2) - 1:
        if ys2[i] > ys2[i - 1]:
            yExtrema2.append("d")
        elif ys2[i] < ys2[i - 1]:
            yExtrema2.append("c")
        else:
            # pass
            yExtrema2.append("0")
    else:
        if ys2[i] >= ys2[i - 1] and ys2[i] >= ys2[i + 1]:
            yExtrema2.append("d")
        elif ys2[i] <= ys2[i - 1] and ys2[i] <= ys2[i + 1]:
            yExtrema2.append("c")
        else:
            # pass
            yExtrema2.append("0")
# print(yExtrema2)

for i in range(len(az2)):
    if i == 0:
        if az2[i] > az2[i + 1]:
            zExtrema2.append("f")
        elif az2[i] < az2[i + 1]:
            zExtrema2.append("e")
        else:
            # pass
            zExtrema2.append("0")
    elif i == len(az2) - 1:
        if az2[i] > az2[i - 1]:
            zExtrema2.append("f")
        elif az2[i] < az2[i - 1]:
            zExtrema2.append("e")
        else:
            # pass
            zExtrema2.append("0")
    else:
        if az2[i] >= az2[i - 1] and az2[i] >= az2[i + 1]:
            zExtrema2.append("f")
        elif az2[i] <= az2[i - 1] and az2[i] <= az2[i + 1]:
            zExtrema2.append("e")
        else:
            # pass
            zExtrema2.append("0")
# print(zExtrema2)

for i in range(len(al2)):
    if i == 0:
        if al2[i] > al2[i + 1]:
            lExtrema2.append("h")
        elif al2[i] < al2[i + 1]:
            lExtrema2.append("g")
        else:
            # pass
            lExtrema2.append("0")
    elif i == len(al2) - 1:
        if al2[i] > al2[i - 1]:
            lExtrema2.append("h")
        elif al2[i] < al2[i - 1]:
            lExtrema2.append("g")
        else:
            # pass
            lExtrema2.append("0")
    else:
        if al2[i] >= al2[i - 1] and al2[i] >= al2[i + 1]:
            lExtrema2.append("h")
        elif al2[i] <= al2[i - 1] and al2[i] <= al2[i + 1]:
            lExtrema2.append("g")
        else:
            # pass
            lExtrema2.append("0")
# print(lExtrema2)

for i in range(len(pr2)):
    if i == 0:
        if pr2[i] > pr2[i + 1]:
            pExtrema2.append("j")
        elif pr2[i] < pr2[i + 1]:
            pExtrema2.append("i")
        else:
            # pass
            pExtrema2.append("0")
    elif i == len(pr2) - 1:
        if pr2[i] > pr2[i - 1]:
            pExtrema2.append("j")
        elif pr2[i] < pr2[i - 1]:
            pExtrema2.append("i")
        else:
            # pass
            pExtrema2.append("0")
    else:
        if pr2[i] >= pr2[i - 1] and pr2[i] >= pr2[i + 1]:
            pExtrema2.append("j")
        elif pr2[i] <= pr2[i - 1] and pr2[i] <= pr2[i + 1]:
            pExtrema2.append("i")
        else:
            # pass
            pExtrema2.append("0")
# print(pExtrema2)

S1 = []

for i in range(len(xExtrema1)):
    res1 = " "
    if xExtrema1[i] != "0":
        res1 = res1 + xExtrema1[i]
        # S1.append(res1)
    if yExtrema1[i] != "0":
        res1 = res1 + yExtrema1[i]
        # S1.append(res1)
    if zExtrema1[i] != "0":
        res1 = res1 + zExtrema1[i]
        # S1.append(res1)
    if lExtrema1[i] != "0":
        res1 = res1 + lExtrema1[i]
        # S1.append(res1)
    if pExtrema1[i] != "0":
        res1 = res1 + pExtrema1[i]
    if res1 != " ":
        S1.append(res1)
print(S1)

S2 = []

for i in range(len(xExtrema2)):
    res2 = " "
    if xExtrema2[i] != "0":
        res2 = res2 + xExtrema2[i]
        # S2.append(res2)
    if yExtrema2[i] != "0":
        res2 = res2 + yExtrema2[i]
        # S2.append(res2)
    if zExtrema2[i] != "0":
        res2 = res2 + zExtrema2[i]
        # S2.append(res2)
    if lExtrema2[i] != "0":
        res2 = res2 + lExtrema2[i]
        # S2.append(res2)
    if pExtrema2[i] != "0":
        res2 = res2 + pExtrema2[i]
    if res2 != " ":
        S2.append(res2)
# print(S2)


def MED(S1, S2):
    matrix = np.zeros((len(S1) + 1, len(S2) + 1), dtype=np.int)
    for i in range(len(S1) + 1):
        for j in range(len(S2) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                matrix[i][j] = min(matrix[i][j - 1] + 1,
                                   matrix[i - 1][j] + 1,
                                   matrix[i - 1][j - 1] + 2 if S1[i - 1] != S2[j - 1] else matrix[i - 1][j - 1] + 0)
    return matrix[len(S1)][len(S2)]


# print(MED(S1, S2))
# norm = MED(S1, S2) / length
# print(norm)


def editDistDP(S1, S2):
    dp = [[0 for x in range(len(S2) + 1)] for x in range(len(S1) + 1)]
    for i in range(len(S1) + 1):
        for j in range(len(S2) + 1):
            if i == j == 0:
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + len(S2[j - 1])
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + len(S1[i - 1])
            else:
                dp[i][j] = min(dp[i][j - 1] + len(S2[j - 1]),
                               dp[i - 1][j] + len(S1[i - 1]),
                               dp[i - 1][j - 1] + MED(S1[i - 1], S2[j - 1]))

    return dp[len(S1)][len(S2)]


print(editDistDP(S1, S2))
length = len(S1) + len(S2)
norm1 = editDistDP(S1, S2) / length
print(norm1)
