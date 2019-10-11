def solution(n):
    temp = n
    count_temp_1 = 0
    count_n_1 = 0
    while temp >= 2:

        if temp % 2 == 1:
            count_temp_1 += 1

        temp = (int)(temp / 2)
    
    if temp == 1:
        count_temp_1 += 1

    while True:
        n += 1
        count_n_1 = 0
        temp = n
        while temp >= 2:
        
            if temp % 2 == 1:
                count_n_1 += 1

            temp = (int)(temp / 2)

        if temp == 1:
            count_n_1 += 1
        if count_n_1 == count_temp_1:
            return n

print(solution(78))
print(solution(15))
print(solution(315))
print(solution(123156))
print(bin(123156).count('1'))
print(bin(123160).count('1'))