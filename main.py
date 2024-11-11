import copy
from math import log2

def Different(lst1, lst2):
    Counter = 0
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            Counter += 1
    return Counter

def IndexDifferent(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return i

#the original function
#func = [0,0,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1]
func = [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]

#number of variables
Razr = int(log2(len(func)))


list_ = []
for i in range(len(func)):
    list_.append([func[i], list(map(int, bin(i)[2:]))])
    if len(list_[i][1]) != 5:
        while len(list_[i][1]) != 5:
            list_[i][1].insert(0, 0)

dict_ = dict()

for k in range(Razr+1):
    dict_[k] = []

all_need_nums = []

for i in range(Razr+1):
    for j in list_:
        if j[1].count(1) == i:
            if j[0] == 1:
                all_need_nums.append(j[1])
                dict_[i].append(j[1])

SecondDict = dict()
SecondDict[0] = copy.deepcopy(dict_)
SimpleElements = []

for i in range(1,Razr + 1):
    SecondDict[i] = dict()
    NotSimpleElements = []

    for k in range(Razr+1):
        SecondDict[i][k] = []

    for key, value in SecondDict[i-1].items():
        for j in value:
            if (key + 1) in SecondDict[i-1]:
                for k in SecondDict[i-1][key + 1]:
                    if Different(j, k) == 1:
                        if j not in NotSimpleElements:
                            NotSimpleElements.append(j)
                        if k not in NotSimpleElements:
                            NotSimpleElements.append(k)
                        ind = IndexDifferent(j, k)
                        new_j = j.copy()
                        new_j[ind] = "-"
                        SecondDict[i][j.count(1)].append(new_j)

    for value in SecondDict[i-1].values():
        for j in value:
            if j not in NotSimpleElements:
                SimpleElements.append(j)

Special = []

for i in SimpleElements:
    if i not in Special:
        Special.append(i)

#print(SecondDict)
#print(NotSimpleElements)
print("simple implicants: ", Special)
#print(all_need_nums)


