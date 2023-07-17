def solution(skill, skill_trees):
    answer = 0
    arr = [[] for _ in range(len(skill_trees))]
    for i in range(len(skill_trees)):
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                arr[i].append(skill.index(skill_trees[i][j]))
    print(arr)
    for i in arr:
        flag = 1
        index = 0
        for j in i:
            if j != index:
                flag = 0
                break
            index += 1
        if flag:
            answer += 1
    return answer