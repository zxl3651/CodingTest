def solution(players, callings):
    dic = {n:i for i,n in enumerate(players)}
    for i in callings:
        index = dic[i]
        players[index-1], players[index] = players[index], players[index-1]
        dic[players[index]] = index
        dic[players[index - 1]] = index - 1
    return players