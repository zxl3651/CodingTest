def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)-1): # -1을 하지않으면 list index 초과 발생
        tmp = phone_book[i+1][:len(phone_book[i])]
        if tmp == phone_book[i]:
            return False
    return True