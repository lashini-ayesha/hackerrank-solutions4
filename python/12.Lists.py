if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(N):
        line=[]
        line = input().split()
        command= line[0]
        if command=="insert":
             list1.insert(int(line[1]),int(line[2]))
        elif command=="print":
             print(list1)
        elif command=="remove":
             list1.remove(int(line[1]))
        elif command=="append":
             list1.append(int(line[1]))
        elif command=='pop':
             list1.pop()
        elif command=="reverse":
             list1.reverse()
        elif command=="sort":
             list1.sort()
