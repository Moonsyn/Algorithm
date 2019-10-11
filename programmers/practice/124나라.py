def solution(n):
    answer = ''
    insoo = []
    while n >= 3:
        namerge = n % 3
        insoo.insert(0,namerge)
        n = (int)(n/3)
    insoo.insert(0,n)
    for i in range(len(insoo)-1,-1,-1):
        if (insoo[i] == 0 or insoo[i] == -1) and i != 0:
            if insoo[i] == 0:
                insoo[i] = 4
            elif insoo[i] == -1:
                insoo[i] = 2

            insoo[i-1] -= 1
        if insoo[i] != 0:
            answer = str(insoo[i]) + answer
   
    return answer

print(solution(345))
print(solution(100000000))

