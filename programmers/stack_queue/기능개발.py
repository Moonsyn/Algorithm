def solution(progresses, speeds):
    num = len(progresses)
    day = [0 for i in range(num)]
    for i in range(num):
        if((100-progresses[i]) % speeds[i] == 0):
            day[i] = (int)((100 - progresses[i]) / speeds[i])
        else:
            day[i] = (int)((100 - progresses[i]) / speeds[i]) + 1
    answer = []
    index = 0
    while index < num:
        getsoo = 1
        baepo = day[index]
        for j in range(index+1, num):
            if day[j] <= baepo:
                getsoo += 1
            else:
                break
        answer.append(getsoo)
        index += getsoo
        
    return answer

print(solution([93,30,55], [1,30,5]))
print(solution(	[70, 27, 50, 97, 50], [1, 2, 3, 4, 5]))