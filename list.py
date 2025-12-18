if __name__ == '__main__':
    N = int(input())
    lst1 = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            lst1.insert(int(command[1]), int(command[2]))
        if command[0] == "print":
            print(lst1)
        if command[0] == "remove":
            lst1.remove(int(command[1]))
        if command[0] == "append":
            lst1.append(int(command[1]))
        if command[0] == "sort":
            lst1.sort()
        if command[0] == "pop":
            lst1.pop()
        if command[0] == "reverse":
            lst1.reverse()
        
            

    
