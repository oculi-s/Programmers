def solution(enroll, referral, seller, amount):
    a = {x: y for x, y in zip(enroll, referral)}
    c = {x: 0 for x in enroll}
    
    for x, m in zip(seller,amount):
        m *= 100
        while x != '-' and m:
            c[x] += m - m//10
            m //= 10
            x = a[x]
    return list(c.values())

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary",
      "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary","young"], [12, 4, 2, 5, 10,2]))
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary",
#       "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
# print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary",
#       "edward", "mary", "mary", "jaimie", "edward"], ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4]))
