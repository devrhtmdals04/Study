# 선형대수 학습 환경 (Python)

이 폴더는 **선형대수 개념 정리 + 손계산 검증 + 알고리즘 구현**을 한곳에서 하기 위한 최소 학습 환경입니다.

## 빠른 시작

- (패키지 설치 없이) 예제 실행: `python3 -m labs.lab01_vectors`
- (권장) 가상환경 만들기: `python3 -m venv .venv`

## 실행하기

```bash
python3 -m labs.lab01_vectors
python3 -m labs.lab02_linear_systems
python3 -m labs.lab03_inverse_det
```

## 시각화 (matplotlib)

이미지를 `outputs/`에 저장합니다.

```bash
make viz01   # 2D 벡터(u, v, 정사영)
make viz02   # 2x2 선형변환(그리드/단위원)
make viz03   # 3D 벡터
```

## 가상환경 + (권장) 실행 셋업

이 환경에서는 `$HOME`에 쓰기 권한이 없을 수 있어(`matplotlib`, `jupyter` 캐시/런타임 디렉토리) 아래 스크립트를 권장합니다.

```bash
source scripts/activate.sh
python -m labs.lab01_vectors
```

JupyterLab:

```bash
source scripts/activate.sh
jupyter lab
```

## 팁

- `la.solve(..., exact=True)`는 `Fraction` 기반으로 **정확 계산**(분수)로 RREF/해를 구합니다.
- 숫자(실수)를 다루는 실험은 `exact=False`(기본값)로 진행하세요.

## 폴더 구조

- `notes/`: 개념/정리 노트(마크다운)
- `labs/`: 개념을 실험하는 작은 실습 스크립트
- `la/`: 선형대수 기본 함수/알고리즘(의존성 없이 동작)

## (선택) 패키지 설치

시각화/수치계산/기호계산을 하고 싶다면 아래 패키지를 설치하면 좋습니다.

- `numpy`, `sympy`, `matplotlib`
- `jupyterlab` (노트북이 필요하면)

설치 명령(네트워크 필요):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

또는 `make venv`, `make install`을 사용해도 됩니다.
