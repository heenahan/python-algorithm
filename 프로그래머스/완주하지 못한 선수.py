import collections

def solution(participant, completion):
    '''
    list in으로 조회 시 O(n)
    set, dict은 hash값으로 저장. 따라서 key로 조회 시 O(1)
    '''
    # 참가자 동명이인 존재하므로 counter -> O(n)
    counter = collections.Counter(participant)
    # 참가자 명단에서 완주자 지움 -> O(n)
    for name in completion:
        counter[name] -= 1
        if counter[name] == 0:
            del counter[name]
    # 참가자 명단에서 남은 한 사람이 완주하지 못한 선수
    answer = list(counter.keys())[0]
    return answer