def hanoi(disks, source, destination, auxiliary, cnt = 1):
    if disks == 1:
        return cnt + 1
    cnt = hanoi(disks - 1, source, auxiliary, destination, cnt)
    return hanoi(disks - 1, destination, source, auxiliary, cnt + 1)

disk = int(input())
total = hanoi(disk, 'A', 'B', 'C')

print(total-1)
#print(2**disk - 1)
