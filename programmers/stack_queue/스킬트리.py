def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        check = ""
        for j in i:
            if j in skill:
                check += j
                print(check)
        if skill.startswith(check):
            answer += 1
            
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))