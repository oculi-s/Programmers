# def solution(scoville, K):
#     t = set([x for x in scoville if x<=K])
#     s = set(range(1, K+1))
#     a = 0
#     while(t & s and len(t) > 1):
#         x = t.pop()+2*t.pop()
#         a += 1
#         if (x < K):
#             t.add(x)
#     t.add(x)
#     return -any(t & s) or a

# def solution(scoville, K):
#     t = [x for x in scoville if x < K]
#     m = [x for x in scoville if x >= K]
#     a = 0
#     while(len(t) > 1):
#         x = min(t)
#         t.remove(x)
#         y = min(t)
#         t.remove(y)
#         x += 2*y
#         a += 1
#         if (x < K):
#             t.append(x)
#     return a*(t[0] > K) or -1

# def solution(scoville, K):
#     t = sorted(scoville, reverse=True)
#     while(min(t) < K):
#         x = t.pop()+2*t.pop()
#         if (x < K):
#             for i,y in enumerate(t):
#                 if x > y:
#                     t.insert(i,x)
#                     break
#             if not x in t:
#                 t.append(x)
#         if (len(t) < 2):
#             break
#     if x > K:
#         t.append(x)
#     else:
#         t.remove(x)
#     if t:
#         return len(scoville) - len(t)
#     else:
#         return -1

# def solution(scoville, K):
#     t = set(scoville)
#     l = len(scoville)
#     x = t.pop()
#     while(x < K and t):
#         t |= {x+2*t.pop()}
#         x = t.pop()
#     n = len(t) + (x<K)
#     return (l - (len(t) or l)) or -1

# class c:
#     def __init__(self,s):
#         self.l = []
#         self.len = len(s)
#         s = sorted(s,reverse=True)
#         for x in s:
#             self.l.append(x)

#     def i(self,l):
#         a = self.l.pop() + 2 * self.l.pop()
#         for i in range(l - 2):
#             if self.l[i] <= a:
#                 self.l[i:i] = [a]
#         self.l.append(a)

# def solution(scoville, K):
#     t = c(scoville)
#     l = t.len
#     while(t.l[-1] < K and l - 1):
#         t.i(l)
#         l -= 1
#     n = (t.l.pop() >= K) + l - 1
#     l = scoville.__len__()
#     return (l - (n or l)) or -1

# def isort(s,a):
#     for i in range(len(s)):
#         if s[i] <= a:
#             s[i:i] = [a]
#             return s
#     return s + [a]

# def solution(scoville, K):
#     t = sorted(scoville,reverse=True)
#     l = len(t)
#     while(t[-1] < K and len(t)-1):
#         a = t.pop()+2*t.pop()
#         l -= 2
#         i = 0
#         while(i < l):
#             if t[i] < a:
#                 break
#             i += 1
#         t[i:i] = [a]
#         print(t)
#     n = (t.pop() >= K) + len(t)
#     l = len(scoville)
#     return (l - (n or l)) or -1

# def solution(scoville, K):
#     t = set(scoville)
#     x = t.pop()
#     while(x < K and t):
#         t.add(x+2*t.pop())
#         x = t.pop()
#     l = len(scoville)
#     n = (x >= K) + len(t)
#     return (l - (n or l)) or -1

# def i(self, d):
#     a = min(self)
#     self.remove(a)
#     b = min(self)
#     self.remove(b)
#     self += [a + 2*b]
#     return d - 1

# def solution(scoville, K):
#     t = scoville
#     l = scoville.__len__()
#     d = t.__len__()
#     while(min(t) < K and d - 1):
#         d = i(t,d)
#     n = (min(t) >= K) + d - 1
#     return (l - (n or l)) or -1

# def i(self,l):
#     a = self.pop() + 2 * self.pop()
#     for i in range(l - 1):
#         if self[i] <= a:
#             self[i:i] = [a]
#     self.append(a)

# def solution(scoville, K):
#     t = sorted(scoville, reverse=True)
#     l = t.__len__()
#     while(t[-1] < K and l - 1):
#         l -= 1
#         i(t,l)
#     n = (t.pop() >= K) + l - 1
#     l = scoville.__len__()
#     return (l - (n or l)) or -1

# def i(self,l):
#     a = self[0] + 2 * self[1]
#     del self[0]
#     del self[0]
#     for i in range(l - 1):
#         if self[i] > a:
#             self[i:i] = [a]
#             return
#     self.append(a)

# def solution(scoville, K):
#     t = sorted(scoville) + [0]
#     l = t.__len__()
#     for l in reversed(range(1,l)):
#         l -= 1
#         a = t[0] + 2 * t[1]
#         t = t[2:]
#         for i in range(l - 1):
#             if t[i] > a:
#                 break
#         t[i:i] = [a]
#         if t[0] >= K:
#             break
#         print(t)
#     n = (t.pop() >= K) + l - 1
#     l = scoville.__len__()
#     return (l - (n or l)) or -1

# from bisect import insort

# def solution(scoville, K):
#     t = sorted(scoville)
#     a = reversed(range(1,len(t)))
#     for l in a:
#         v = t.pop(0)+2*t.pop(0)
#         insort(t,v)
#         if t[0] >= K:
#             break
#     n = (t.pop() >= K) + l - 1
#     l = scoville.__len__()
#     return (l - (n or l)) or -1

import heapq

def solution(scoville, K):
    t = scoville
    heapq.heapify(t)
    l = len(t)
    while(t[0] < K and len(t) > 1):
        heapq.heappush(t,heapq.heappop(t)+2*heapq.heappop(t))
    n = (heapq.heappop(t) >= K) + len(t)
    return (l - (n or l)) or -1

print(solution([1, 2, 3, 9, 10, 12], 7)==2)
print(solution([1, 2, 7], 7)==2)
print(solution([1, 2], 6)==-1)
# print(solution([1, 1, 1], 4)== 2)
# print(solution([10, 10, 10, 10, 10], 100)== 4)
# print(solution([1, 2, 3, 9, 10, 12], 7)== 2)
# print(solution([0, 2, 3, 9, 10, 12], 7)== 2)
# print(solution([0, 0, 3, 9, 10, 12], 7)== 3)
# print(solution([0, 0, 0, 0], 7)== -1)
# print(solution([0, 0, 3, 9, 10, 12], 7000)== -1)
print(solution([0, 0, 3, 9, 10, 12], 0)== 0)
# print(solution([0, 0, 3, 9, 10, 12], 1)== 2)
# print(solution([0, 0], 0)== 0)
# print(solution([0, 0], 1)== -1)
# print(solution([1, 0], 1)== 1)