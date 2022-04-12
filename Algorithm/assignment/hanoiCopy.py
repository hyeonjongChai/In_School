import sys
def find(num, k):

    while(k%4 == 0):
        k = k//4
    if num%2 == 1:
        if (k%2 == 1):
            if k%6 == 1:
                print('{} {}'.format(1,3))
            if k%6 == 3:
                print('{} {}'.format(3,2))
            if k%6 == 5:
                print('{} {}'.format(2,1))
        else:
            if k%12 == 2:
                print('{} {}'.format(1,2))
            if k%12 == 6:
                print('{} {}'.format(2,3))
            if k%12 == 10:
                print('{} {}'.format(3,1))
    if num%2 == 0:

        if k%2 == 1:

            if k%6 == 1:
                print('{} {}'.format(1,2))
            if k%6 == 3:
                print('{} {}'.format(2,3))
            if k%6 == 5:
                print('{} {}'.format(3,1))

        else:
            if k%12 == 2:
                print('{} {}'.format(1,3))
            if k%12 == 6:
                print('{} {}'.format(3,2))
            if k%12 == 10:
                print('{} {}'.format(2,1))


test_case = int(str(sys.stdin.readline().rstrip()))
for i in range(0, test_case):
    num_disks, confirm_count = map(int,sys.stdin.readline().split())
    find(num_disks,confirm_count)