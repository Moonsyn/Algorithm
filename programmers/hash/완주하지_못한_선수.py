def solution(participant, completion):
    answer = ""
    length = len(participant)
    for i in participant:
        if i in completion:
            participant.remove(i)
            completion.remove(i)
        else:
            answer = i
    return answer

print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))