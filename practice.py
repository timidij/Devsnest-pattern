# l = [1, 3, 2, 4, 2];
# r= (1, 3, 5, 6, 9, 0, 5);
# print(r[2]);
# x = r[0];
# l.sort()
# print(l[-1])
#

# # print(l.index(3))
# # print(l[l.index(3) : ])

def solve(M, N):
    # CODE HERE
    arr=[]
    for i in range(1,M,2):
        arr.append((i*".|.").center(N,"-"))
    arr.append("DEVSNEST!".center(N,"-"))
    for i in range(M-2,-1,-2):
        arr.append((i*".|.").center(N,"-"))
    return arr
cool= solve(5,9)
for i in cool:
    print(i)

