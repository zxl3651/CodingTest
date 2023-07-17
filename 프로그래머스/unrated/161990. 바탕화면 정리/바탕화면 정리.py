def solution(wallpaper):
    answer = []
    num = [] #x축 값 저장
    top = [] #y축 값 저장
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if '#' == wallpaper[i][j]:
                num.append(j)
                top.append(i)
    answer.append(min(top))
    answer.append(min(num))
    answer.append(max(top)+1)
    answer.append(max(num)+1)
    return answer