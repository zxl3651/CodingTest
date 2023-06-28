def solution(my_string, is_prefix):
    answer = 0
    l = len(is_prefix)
    if my_string[:l] == is_prefix:
        answer = 1
    return answer