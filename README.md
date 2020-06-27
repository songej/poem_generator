# 윤동주풍 시 생성기
윤동주풍 시 생성기는 시작 단어와 총 단어수를 정해주면 윤동주 스타일로 시를 써주는 프로그램 입니다.

## Requirements
- Python
- Pandas
- Numpy
- Tensorflow
- Keras

## Installation
- [Anaconda](https://www.anaconda.com/) 설치
- Anaconda Prompt 실행
- Anaconda 업그레이드, Tensorflow 설치, Keras 설치 등의 다음 명령어 실행
```bash
conda update -n base conda
conda update --all
python -m pip install --upgrade pip
conda install tensorflow
conda install keras
```

## Execution
- 파이썬 코드 실행
```python
python poem_generator.py
```
- Epoch 200/200 이 될 때까지 학습 대기
- 어떤 단어로 시를 시작할 것인지 단어 입력
- 몇 단어로 시를 쓸 것인지 숫자 입력
- 윤동주풍 시 생성 결과 확인

## Sample Output
```
'나는' 단어로 시작하는 24단어의 윤동주풍 시 생성 예제
나는 이마에 땀을 흘려야겠다 여미고 화단에서 금잔화 내려 슬픈 것처럼 안에까지 눈이 내리는 것일까 정말 너는 잃어버린 역사 처럼 홀홀이 가는 것이냐 떠나기 전에 일러둘 말이
```
```
'그리워서' 단어로 시작하는 24단어의 윤동주풍 시 생성 예제
그리워서 돌과 돌과 돌이 끝없이 연달아 언덕 못할 마음으로 금잔화 한 포기를 따 가슴에 꽂고 병실 안으로 사라진다 나는 그 여자의 건강이 아니 내 건강도
```
```
윤동주풍 시 생성기가 몇 단어로 시를 쓸 것인지 숫자를 입력해주세요.
24
윤동주풍 시 생성기가 어느 단어로 시를 시작할 것인지 단어를 입력해주세요.
사랑
'사랑' 단어로 시작하는 24단어의 윤동주풍 시 생성 예제
사랑 돌과 돌과 돌이 끝없이 연달아 언덕 못할 마음으로 금잔화 한 포기를 따 가슴에 꽂고 병실 안으로 사라진다 나는 그 여자의 건강이 아니 내 건강도
```
## Contributor
- 송은정

## License
[MIT](https://choosealicense.com/licenses/mit/)
