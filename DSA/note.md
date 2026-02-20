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

# 재귀함수의 실행 흐름: 부메랑의 법칙 

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

# 파이썬 변수 참조와 메모리 동작 원리 (LeetCode 25 해설)

이 문서는 LeetCode 25번 *Reverse Nodes in k-Group* 문제 풀이 중, `dummy`와 `groupPrev` 포인터의 동작 원리와 메모리 참조(Reference) 개념을 정리한 내용입니다.

## 1. 핵심 개념: 변수는 '이름표'다

파이썬의 변수는 값을 저장하는 상자가 아니라, 객체가 저장된 메모리 주소를 가리키는 **이름표(Reference)**입니다.

- **할당 (`=`):** 이름표를 붙이는 행위 (어떤 대상을 가리킬지 정함)
- **속성 변경 (`.next =`):** 이름표가 붙은 **대상(객체)**의 내부를 수정하는 행위

## 2. 코드 단계별 메모리 변화 분석

### 단계 1: 초기화 (동기화 상태)
두 변수가 같은 객체를 가리키는 상황입니다. 이를 **Aliasing(별칭)**이라고 합니다.

```python
dummy = ListNode(0)      # 0x100 번지에 노드 생성
groupPrev = dummy        # dummy가 가리키는 주소를 groupPrev도 공유

# 이진 트리 뒤집기(Invert Binary Tree) 알고리즘 비교

이 문서는 이진 트리를 좌우 반전시키는 세 가지 주요 접근 방식(**Queue, Stack, Recursion**)의 동작 원리, 코드, 그리고 장단점을 비교 분석합니다.

---

## 1. 한 눈에 보는 비교 (Summary)

모든 방식의 **시간 복잡도는 $O(N)$** 으로 동일합니다. (모든 노드를 한 번씩 방문해야 하기 때문)
차이점은 **공간 복잡도(메모리 사용 패턴)**와 **방문 순서**에 있습니다.

| 특징 | **1. Queue (BFS)** | **2. Stack (Iterative DFS)** | **3. Recursive (DFS)** |
| :--- | :--- | :--- | :--- |
| **탐색 방식** | **너비 우선 (BFS)**<br>위층부터 가로로 훑음 | **깊이 우선 (DFS)**<br>한쪽 끝까지 파고듦 | **깊이 우선 (DFS)**<br>시스템 콜 스택 이용 |
| **자료구조** | `deque` (FIFO) | `list` (LIFO) | System Call Stack |
| **공간 복잡도** | $O(w)$ (트리의 **최대 너비**) | $O(h)$ (트리의 **높이**) | $O(h)$ (트리의 **높이**) |
| **메모리 위험** | 트리가 **뚱뚱할 때** (Wide) 불리 | 트리가 **깊을 때** (Deep) 불리 | 트리가 **매우 깊을 때**<br>(RecursionError 위험) |
| **코드 특징** | `popleft()` 사용 | `pop()` 사용 | 코드가 가장 간결함 |

---

## 2. 상세 분석 및 코드

### ① Queue 방식 (BFS: 너비 우선 탐색)
**"위에서부터 한 줄씩, 층별로 처리한다."**

* **동작:** 큐(Queue)를 사용하여 먼저 들어온 노드를 먼저 처리(FIFO)합니다.
* **장점:** 직관적이며, 트리의 깊이가 깊어도 스택 오버플로우가 발생하지 않습니다.
* **단점:** 트리의 너비가 넓을수록(Full Binary Tree 등) 큐에 저장되는 노드가 많아져 메모리를 많이 사용합니다.

from collections import deque

def invertTree(root):
    if not root:
        return None
        
    queue = deque([root])
    
    while queue:
        node = queue.popleft()  # 앞에서 꺼냄 (FIFO)
        
        # 자식 노드 교환 (Swap)
        node.left, node.right = node.right, node.left
        
        # 다음 층의 자식들을 대기열에 등록
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
            
    return root

# 구분,영어 명칭,순서 (공식),처리(Visit) 시점,주요 특징
# 전위 순회,Preorder,Root → Left → Right,노드에 도착하자마자,트리의 구조를 파악하거나 복사할 때 사용
# 중위 순회,Inorder,Left → Root → Right,왼쪽 자식을 다 보고 돌아와서,BST에서 값을 오름차순으로 가져올 때 사용

    # 전위 순회 (Preorder)
def preorder(node):
    if not node: return
    
    print(node.val)      # 1. 나부터 처리 ("Pre")
    preorder(node.left)  # 2. 왼쪽
    preorder(node.right) # 3. 오른쪽

# 중위 순회 (Inorder)
def inorder(node):
    if not node: return
    
    inorder(node.left)   # 1. 왼쪽
    print(node.val)      # 2. 돌아와서 나 처리 ("In")
    inorder(node.right)  # 3. 오른쪽