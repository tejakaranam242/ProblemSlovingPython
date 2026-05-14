n = int(input())
seen = set()
previousTime = -1
for i in range(n):
    sender, reciever, time, amount = input().split()
    time = int(time)
    key = sender+'_'+reciever
    if key in seen:
        print("error duplication transaction")
        exit()
    seen.add(key)
    if previousTime!=-1 and (time-previousTime)>60:
        print("fraud")
        exit()
    previousTime = time
print("All transactions are valid")