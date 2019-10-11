num = (int)(input())
def dp(length, start, jump_count):
    can_go = [start+1, start, start-1]
    for i in can_go:
        if length - i > 0:
             length -= i
             dp(length, i, jump_count+1)
        elif length == i:
            return jump_count + 1

for i in range(num):
    points = input().split(" ")
    start_point = (int)(points[0])
    end_point = (int)(points[1])
    length = end_point - start_point -2
    start_length = 1
    jump = dp(length, start_length, 2)
    print(jump)




