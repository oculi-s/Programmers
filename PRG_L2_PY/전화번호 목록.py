def solution(phone_book):
    p = sorted(phone_book,reverse=True)
    while p:
        x = p.pop()
        for y in p:
            if y[:len(x)] == x:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))