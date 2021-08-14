import time
N = 5000

def solution(k, room_number):
    M = [0]+[1]*k
    T = list(range(1,k+1))
    for i,n in enumerate(room_number):
        if M[n]:
            M[n] = 0
        else:
            while not M[T[n]]:
                T[n] += 1
            M[T[n]] = 0
            room_number[i] = T[n]
    return room_number

s = time.time()
S = solution(N, [1]*N)
print(time.time()-s)

def solution(k, room_number):
    M = [0]+[1]*k
    T = list(range(1,k+1))
    N = []
    for n in room_number:
        if M[n]:
            M[n] = 0
            N.append(n)
        else:
            while not M[T[n]]:
                T[n] += 1
            M[T[n]] = 0
            N.append(T[n])
    return N

s = time.time()
S = solution(N, [1]*N)
print(time.time()-s)

# def solution(k, room_number):
#     N = []
#     M = room_number[0]
#     for n in room_number:
#         if n not in N:
#             N.append(n)
#             M = max(n,M)
#         else:
#             for x in range(n,k+1):
#                 if x not in N:
#                     N.append(x)
#                     break
#             else:
#                 N.append(M+1)
#                 M += 1
#     return N

# s = time.time()
# solution(N, [1]*N)
# print(time.time()-s)