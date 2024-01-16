# 베스트앨범
# 프로그래머스 코딩테스트 고득점 kit > 해시
# 1188 (+9)
# 딕셔너리 두개 만든다. 하나는 key가 장르명, value가 장르별재생횟수(int)이다. 하나는 key가 장르명, value가 [(노래의 재생횟수, 노래 고유번호), (노래의 재생횟수, 노래 고유번호)]이다. 
# 먼저 장르별 재생횟수를 value로 하는 딕셔너리를 재생횟수에 대해 내림차순으로 정렬한다.
# 장르의 순서는 정해졌고, 이제 각 장르 별 리스트를 각각 정렬해준다.
# 노래의 재생횟수를 기준으로 내림차순이며, 노래의 재생횟수가 같다면 노래의 고유번호를 기준으로 오름차순 정렬해준다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택하고 그 외에는 2개씩만 앨범에 담아야한다. 이를 고려하는 코드 추가

# 알아야 할 개념: dictionary 정렬
# dictionary.items()하면 dict_items([(key, value), (key, value), ...]) 이런 형태로 반환한다.
# 이를 이용해서 리스트처럼 정렬을 할 수 있다.
# value를 기준으로 정렬하고 싶다면, sorted() 메소드의 key 매개변수에 익명함수인 lambda 함수를 사용하여 정렬할 수 있다. 
# dic.items()의 경우 (key, value) 튜플 형태의 원소를 제공하기에 lambda에서 x[1]와 같은 방식으로 value 값을 지정할 수 있는 것이다. 
# 참고로, 이후에 딕셔너리 자료형처럼 써야할 일이 있다면 딕셔너리로 다시 변환해주어야한다.
# 딕셔너리 정렬은 sort 대신 sorted를 사용해야 한다.

# 아래 예시를 기억해두자.
# Value를 내림차순 후, Key를 오름차순하여 튜플 형태로 (Key, Value) 반환할 때
# dic = {'e': 1, 'a': 3, 'b': 5, 'c': 1, 'd': 2, }
# dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
# print(dic) #[('b', 5), ('a', 3), ('d', 2), ('c', 1), ('e', 1)]

dic = {'e': 1, 'a': 3, 'b': 5, 'c': 1, 'd': 2, }
dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(dic) #[('b', 5), ('a', 3), ('d', 2), ('c', 1), ('e', 1)]
from collections import defaultdict

def solution(genres, plays):
    answer = []
    d = defaultdict(list)
    play_cnt = defaultdict(int)
    N = len(plays)
    for i in range(N):
        d[genres[i]].append((plays[i], i))
        play_cnt[genres[i]] += plays[i]
    
    play_cnt = dict(sorted(play_cnt.items(), key = lambda x:x[1], reverse = True))
    
    for k in play_cnt.keys():
        d[k] = sorted(d[k], key = lambda x:(-1*x[0], x[1]))
        length = min(2, len(d[k]))
        for i in range(length):
            answer.append(d[k][i][1])
    return answer