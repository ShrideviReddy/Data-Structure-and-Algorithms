def happy_number(num):
    visit = set()
    while num not in visit:
        visit.add(num)
        num = sumofsquares(num)
        if num == 1:
            return True
    return False

def sumofsquares(n):
    output = 0
    while n :
        digit = n%10
        digit = digit ** 2
        output+=digit
        n = n //10
    return output

print(happy_number(19))
