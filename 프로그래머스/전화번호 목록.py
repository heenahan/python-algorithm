def solution(phone_book):
    phone_book.sort(key=len) # 길이가 작은 전화번호가 앞에 옴 O(nlogn)
    length = [len(phone_book[0])]
    # 빠르게 match -> O(1)
    phone_book = set(phone_book)
    # O(n)
    for phone_num in phone_book:
        # 이전보다 더 긴 문자열이 오면 추가
        if len(phone_num) > length[len(length) - 1]:
            length.append(len(phone_num))
        index = 0
        # 중복된 전화번호가 없다 -> 자신보다 작은 길이의 전화번호만 match
        # 길이가 커 봤자 20이므로 무시
        while len(phone_num) > length[index]:
            if phone_num[:length[index]] in phone_book:
                return False
            index += 1
    return True