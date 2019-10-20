#https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        cmd = input()
        cmd_list = cmd.split(" ")
        if(cmd_list[0] == "print"):
            print(L)
        elif(cmd_list[0] == "append"):
            L.append(int(cmd_list[1]))
        elif(cmd_list[0] == "sort"):
            L = sorted(L)
        elif(cmd_list[0] == "pop" and len(cmd_list)>0):
            L = L[0:len(L)-1]
        elif(cmd_list[0] == "remove"):
            L.remove(int(cmd_list[1]))
        elif(cmd_list[0] == "reverse"):
            L.reverse()
        else:
            L.insert(int(cmd_list[1]),int(cmd_list[2]))
