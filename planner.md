# 🎖️ Army Dev Growth Plan: 18-Week Zero to Hero

> **목표:** 전역 전까지 CS 기초 완성, 코딩 테스트 빈출 패턴 자동화, ML 프로젝트 포트폴리오 1건 확보
> **철학:** "고정이 성과를 만든다." (매일 똑같은 2시간 루틴)

---

## 📅 1. Daily Routine (2시간 고정)

**규칙:** 타이머 필수. 고민할 시간 없이 기계적으로 수행.

| 시간 | 활동 (Section) | 세부 내용 (Action Item) |
| :--- | :--- | :--- |
| **10분** | 🔄 **DSA 복습** | 전날 오답 1개 재풀이 (해설 X, 로직 주석만이라도 작성) |
| **45분** | 🧩 **DSA 메인** | 오늘 할당된 문제 1개 풀이 (**타이머 준수**) |
| **15분** | 📝 **DSA 회고** | 시간복잡도, 엣지케이스, 모범 답안 비교 정리 |
| **40분** | 📚 **CS / Math** | 요일별 주제 학습 (개념 20분 + 예제/적용 20분) |
| **10분** | 🗣️ **English** | 오늘 푼 문제/개념 영어로 60초 설명 (**녹음 파일 저장**) |

---

## 🗓️ 2. Weekly Schedule (요일별 주제)

| 요일 | DSA (70분) | CS/Math (40분) | 핵심 키워드 |
| :--- | :--- | :--- | :--- |
| **월** | 문제 풀이 | 🖥️ **OS** | 프로세스/스레드, 스케줄링, 동기화, 메모리 |
| **화** | 문제 풀이 | 🌐 **네트워크** | HTTP/HTTPS, TCP/IP, 핸드셰이킹, DNS |
| **수** | 문제 풀이 | 💾 **DB** | SQL, 인덱스, 정규화, 트랜잭션, NoSQL |
| **목** | 문제 풀이 | 📐 **선형대수** | 벡터, 행렬, 내적(유사도), 고유값 |
| **금** | 문제 풀이 | 🎲 **확률/통계** | 분포, 기댓값, 베이즈 정리, 가설검정 |
| **토** | **오답/리팩토링** | 🏗️ **시스템 디자인** | 주간 요약 정리 + 시스템 설계 기초 |
| **일** | **휴식** | 🛌 **Rest** | 번아웃 방지 완전 휴식 |

---

## 🗺️ 3. 18-Week Roadmap

### **Phase 1: 기초 체력 & 패턴 자동화 (Week 1 ~ 6)**
*목표: 문제만 보면 유형이 바로 떠오르는 상태 ("자동화")*

- [ ] **Week 1: Array & Hash Map**
    - DSA: Two Sum, Group Anagrams
    - CS: OS(프로세스 vs 스레드), Net(HTTP 구조), DB(인덱스 기초)
- [ ] **Week 2: Two Pointers & Sliding Window**
    - DSA: Valid Palindrome, 3Sum
    - Math: 벡터/행렬 기초, 평균/분산/표준편차
- [ ] **Week 3: Stack & Queue**
    - DSA: Valid Parentheses, Daily Temperatures
    - CS: OS(스케줄링), Net(TCP/UDP), DB(SQL 기초)
- [ ] **Week 4: Binary Search (이분탐색)**
    - DSA: Search in Rotated Array
    - Math: 내적(Dot Product), 조건부 확률
- [ ] **Week 5: Sorting & Greedy**
    - DSA: Merge Intervals, Top K Elements
    - CS: OS(컨텍스트 스위칭), Net(OSI 7계층), DB(정규화)
- [ ] **Week 6: Backtracking (재귀 기초)**
    - DSA: Permutations, Subsets
    - Math: 역행렬, 정규분포(Z-score)

### **Phase 2: 심화 & 시스템 디자인 (Week 7 ~ 13)**
*목표: 논리적 사고 확장 및 아키텍처 설계 능력 배양*

- [ ] **Week 7: Tree (BFS/DFS)**
    - DSA: Max Depth, Invert Tree
    - CS: OS(동기화/Mutex), Net(DNS), DB(트랜잭션 ACID)
- [ ] **Week 8: BST & Heap**
    - DSA: Validate BST, Kth Largest Element
    - Math: 고유값(Eigenvalue), 베이즈 정리
- [ ] **Week 9: Graph (General)**
    - DSA: Number of Islands, Clone Graph
    - CS: OS(데드락), Net(HTTPS/SSL), DB(NoSQL)
- [ ] **Week 10: Graph (Advanced)**
    - DSA: Dijkstra, Topological Sort, Union-Find
    - Math: 선형 변환, 가설 검정(P-value)
- [ ] **Week 11: DP (1D - 기초)**
    - DSA: Climbing Stairs, Coin Change
    - System: **URL Shortener** 설계 (Base62, Key 생성)
- [ ] **Week 12: DP (2D / Grid)**
    - DSA: Unique Paths, LCS
    - System: **Rate Limiter** 설계 (Token Bucket, Redis)
- [ ] **Week 13: Review & Mix**
    - DSA: 오답률 높은 유형 집중 공략
    - System: **News Feed** 설계 (Fan-out 전략)

### **Phase 3: ML 프로젝트 & 프로덕션 (Week 14 ~ 18)**
*목표: End-to-End 서비스 배포 및 포트폴리오 완성*

- [ ] **Week 14: Data & Preprocessing**
    - 주제 선정 (Kaggle 데이터 권장 - 집값, 분류 등)
    - EDA (시각화) 및 전처리 (결측치, 스케일링)
- [ ] **Week 15: Modeling & Training**
    - Baseline 모델 학습 (Logistic/Tree)
    - 모델 고도화 (XGBoost/LightGBM) 및 튜닝
- [ ] **Week 16: Evaluation & Analysis**
    - 평가지표 확인 (F1-score, RMSE)
    - **에러 분석** (Why?) 및 최종 모델 저장(.pkl)
- [ ] **Week 17: Serving (API)**
    - FastAPI 프로젝트 생성
    - `/predict` API 구현 및 간단한 UI 연결
- [ ] **Week 18: Deploy & Documentation**
    - Docker 컨테이너화
    - GitHub **README(영문)** 작성 및 데모 영상 녹화

---

## 💡 Success Tips

1.  **DSA 복습 10분 제한:** 못 풀었으면 로직만 주석으로 적고 넘어가라. (주말에 보충)
2.  **수학은 코드로:** 공식을 외우지 말고 Python(`numpy`)으로 쳐서 결과값을 확인하라.
3.  **프로젝트 범위 제한:** 데이터 수집(크롤링)에 시간 쓰지 말고, 모델링과 서빙(Serving) 파이프라인 구축에 집중하라.