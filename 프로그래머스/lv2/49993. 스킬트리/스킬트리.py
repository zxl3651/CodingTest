def solution(skill, skill_trees):
    """
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
    """
    answer=0
    for i in skill_trees:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            print(skillist)
            answer+=1
    return answer