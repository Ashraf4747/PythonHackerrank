N = int(input())
ls = []
for i in range(N):
    command = input().split()
    arg = command[1:]
    if command[0] == 'print':
        print(ls)
    else :
        cmd = command[0]+'('+",".join(arg)+')'
        eval('ls.'+cmd)
        print(ls)
