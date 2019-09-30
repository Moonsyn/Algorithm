def solution(priorities, location):
    count = 1
    while True:
        switch = False
        front = priorities[0]
        for i in priorities:
            if front < i:
                priorities.remove(front)
                priorities.append(front)
                switch = True
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1
                break
        if switch == False:
            if location == 0:
                return count
            else:
                priorities.remove(front)
                location -= 1
                count += 1