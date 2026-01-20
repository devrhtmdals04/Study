# How to make hashtable (dictionary) in python?
# 1. hashmap  = {}
# 2. hashmap = defaultdict(list) this dictionary is for list sryle value ex. {key=1, value=[0, 3, 6], key=2, value=[3, 6, 5]} this value can return hashmap.values(). result = [0, 3, 6], [3, 6, 5]

# How to get alphabet order index?
# ord(char) - ard('a') if char is 'b' it returns 1.

# How to make clean string?
# use upper() or lower() and isalnum() (is alphabet numeric?) clean_str = "".join(s.lower() for s in str if s.isalnum())

# checklist
# if you did 'tuple(list)' the 'list' doesn't tuplicated. do tupled = tuple(list) and use tupled, then, tupled will be tuble.

# why two-pointer neds sort? 
# 1. Avoid Duplications. use while comparison. 
# 2. Optimization pointing. if you need sum, if the diff is lower than you want, upper left pointer of sorted list, than you can get optimized pointer.

# make dictionary by Pythonic way: 'dict[key] = dict.get(key, default) + 1' this will make your code compact. by using this 

# How to sort dictionary by items?
# sorteddictbyitems = sorted(dict.items(), key = lambda x:x[1], reverse=True) this is Descending order, if you wand right order, use reverse=False.
# Or use this Pythonic method: dict.get(key, value)

# how to make index rule in two-dimention list?
# you have i, j for two-dimention list. each index can get 0~2 values. so you can product 3times one of then(particulary i).
# so, use '(i//3)*3 + (j//3)'.

# windiwsliding method. this method is related in two-pointer. only use left and right to check. you can check in-and-out of
# left and right value and move pointer. this can reduce time opacity O(n^2) tom O(n) but needs lot of understand of the problem.

# why use QUEUE instead of list? becouse of time opacity. when you need to pullout first element of list, the python list moves
# all of the later elements to zeroindex. so it spends O(nlogn). but the QUEUE just use QUEUE.popleft(). this requires O(1).
# How to use? 
# q = deque(), q.pop(), q.popleft(), q.append(), q.appendleft().

# when you want to get upper devision quotient. in X // Y you'll get integer quotient underred. then, you use (X + Y - 1) // Y.

# 재귀함수의 실행 흐름: 부메랑의 법칙 🪃

재귀함수는 단순히 반복하는 것이 아니라, **깊이 들어갔다가(Dive) 다시 거슬러 올라오는(Unwind)** "V"자 형태의 흐름을 가집니다. 코드의 위치에 따라 실행 순서가 정반대가 된다는 점이 핵심입니다.

## 1. 구조로 보는 실행 순서

재귀함수 내부는 **재귀 호출(Recursive Call)**을 기준으로 **'진입 구간'**과 **'복귀 구간'**으로 명확히 나뉩니다.

```python
def recursive_function(n):
    # [구역 A] 진입 구간 (Pre-processing)
    # 흐름: 정방향 (1 -> 2 -> 3 ...)
    # 설명: 함수가 호출되자마자 실행되는 코드
    print(f"들어감: {n}")

    # [분기점] 재귀 호출
    # 설명: 여기서 현재 함수는 '일시 정지(Pause)'하고, 
    #       다음 깊이의 함수가 끝날 때까지 대기합니다.
    if n < 3:
        recursive_function(n + 1)

    # [구역 B] 복귀 구간 (Post-processing)
    # 흐름: 역방향 (... 3 -> 2 -> 1)
    # 설명: 가장 깊은 곳에서 리턴되어 돌아오면서 실행되는 코드
    print(f"나옴: {n}")
```
# Python Dictionary와 시간 복잡도 분석

## 1. 핵심 요약
Python의 **딕셔너리(Dictionary)**는 내부적으로 **해시 테이블(Hash Table)** 구조를 사용합니다. 
따라서 데이터의 양(N)과 무관하게 **거의 모든 연산을 $O(1)$ (상수 시간)**에 처리할 수 있는 강력한 자료구조입니다.

## 2. `in` 연산자의 작동 원리 비교

### 리스트 (List) : $O(N)$
리스트는 데이터가 순서대로 나열된 아파트 우편함과 같습니다.
특정 데이터를 찾으려면 **첫 번째 칸부터 끝까지 순차적으로 확인(Linear Search)**해야 합니다.

* **비유:** "철수 있어요?"라고 101호부터 1000호까지 초인종을 다 눌러보는 것.