def solution(N, number):
    m = []
    for q,v in zip([number,number*N],[0,1]):
        for x in [11111,1111,111,11,1]:
            if q >= N * x:
                while q // (N * x) > N:
                    v += 1
                    q //= N * x
                v += q // (N * x) * len(str(x))
                q %= N * x
        v += 2 * q
        m.append(v)
    v = min(m)
    return v * (v < 9) or -1

# print(solution(5,12),4)
# print(solution(2,11),3)
# print(solution(5,5),1)
# print(solution(5,10),2)
# print(solution(5,31168),-1)
print(solution(1,1121),7)
print(solution(5,1010),7)
print(solution(3,4),3)
print(solution(5,5555),4)
print(solution(5,5550),5)
print(solution(5,20),3)
print(solution(5,30),3)
print(solution(6,65),4)
print(solution(5,2),3)
print(solution(5,4),3)
print(solution(1,1),1)
print(solution(1,11),2)
print(solution(1,111),3)
print(solution(1,1111),4)
print(solution(1,11111),5)
print(solution(7,7776),6)
print(solution(7,7784),5)
print(solution(2,22222),5)
print(solution(2,22223),7)
print(solution(2,22224),6)
print(solution(2,11111),6)
print(solution(2,11),3)
print(solution(2,111),4)
print(solution(2,1111),5)
print(solution(9,36),4)
print(solution(9,37),6)
print(solution(9,72),3)
print(solution(3,18),3)
print(solution(2,1),2)
print(solution(4,17),4)