N = int(input())
ls = list()
for loop in range (N):
        command = input().split()
        cmd = command[0]
        if cmd == 'insert':
                position = int(command[1])
                value = int(command[2])
                ls.insert(position,value)
        elif cmd == 'remove':
                element = int (command[1])
                ls.remove(element)
        elif cmd == 'append':
                element = int(command [1])
                ls.append(element)
        elif cmd == 'sort':
                ls.sort()
        elif cmd == 'pop':
                ls.pop()
        elif cmd == 'reverse':
                ls.reverse()
        elif cmd == 'print':
                print(ls)
