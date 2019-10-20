#The link to the problem is https://www.hackerrank.com/challenges/nested-list/problem
names = []
scores = []
res = []
for _ in range(int(input())):
    name = input()
    names.append(str(name))
    score = float(input())
    scores.append(score)
min_ele = min(scores)
for i in range(len(scores)):
    if(scores[i] == min_ele):
        scores[i] = 9999
min_ele = min(scores)
for i in range(len(scores)):
    if(scores[i] == min_ele):
        res.append(names[i])
res = sorted(res)
for name  in res:
    print(name)
