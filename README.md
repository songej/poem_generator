# 윤동주체 시 생성기
윤동주체 시 생성기는 시작 단어와 총 단어수를 정해주면 윤동주 문체로 시를 써주는 프로그램 이다.

## Features
many-to-one 구조의 RNN을 활용하여 문맥을 반영해서 텍스트를 생성하는 모델을 통해 윤동주체 시 생성기를 구현하였다.
학습 데이터는 윤동주 시인의 유고 시집인 '하늘과 바람과 별과 시'의 1941년 모음인 19편의 시이다.
윤동주 시인은 사망한지 50년이 지났으므로 윤동주 시인의 시에 대한 저작재산권은 소멸되었고, 동일성을 유지한 상태로 데이터를 활용하는 경우에는 법적인 문제가 발생되지 않는다.
poem.csv 파일에 저장되어 있는 시 제목 및 본문 데이터는 총 223행이다.
모델이 문맥을 학습하기 위해서는, 전체 문장의 단어들을 모두 고려하여 데이터를 재구성해야 한다.
이를 위해 재구성된 단어 집합의 크기는 총 794개이다.
가장 긴 샘플의 길이는 76이고, 0을 사용하여 모든 샘플들의 길이를 가장 긴 샘플 크기에 맞춰준다.
데이터에 대한 원핫인코딩을 수행한 후 모델을 설계하여 적용하였다.
적용된 모델은 각 단어의 임베딩 벡터가 10차원이고 128의 은닉 상태 크기를 가지는 LSTM 모델이다.
모델의 예측 결과를 알아보기 위해 문장을 생성하는 함수를 만들었다.
사용자가 어떤 단어로 시를 시작할 것인지 단어를 입력하고, 몇 단어로 시를 쓸 것인지 숫자를 입력하면
이에 맞는 윤동주체 시 생성 결과를 출력해준다.

## Requirements
- Python + Pandas + Numpy
- Tensorflow + Keras

## Installation
- [Anaconda](https://www.anaconda.com/) 설치
- Anaconda Prompt 실행
- Anaconda 업그레이드, Tensorflow 설치, Keras 설치 등의 다음 명령어 실행
```
conda update -n base conda
conda update --all
python -m pip install --upgrade pip
conda install tensorflow
conda install keras
```

## Execution
- 파이썬 코드 실행
```
python poem_generator.py
```
- Epoch 200/200 이 될 때까지 학습 대기
- 어떤 단어로 시를 시작할 것인지 단어 입력
- 몇 단어로 시를 쓸 것인지 숫자 입력
- 윤동주체 시 생성 결과 확인

## Sample Output
```
윤동주체 시 생성기가 어떤 단어로 시를 시작할 것인지 단어를 입력해주세요.
사랑
윤동주체 시 생성기가 몇 단어로 시를 쓸 것인지 숫자를 입력해주세요.
24
'사랑' 단어로 시작하는 총 24 단어의 윤동주체 시 생성 예제
사랑 돌과 돌과 돌이 끝없이 연달아 언덕 못할 마음으로 금잔화 한 포기를 따 가슴에 꽂고 병실 안으로 사라진다 나는 그 여자의 건강이 아니 내 건강도
```
```
'나는' 단어로 시작하는 총 24 단어의 윤동주체 시 생성 예제
나는 이마에 땀을 흘려야겠다 여미고 화단에서 금잔화 내려 슬픈 것처럼 안에까지 눈이 내리는 것일까 정말 너는 잃어버린 역사 처럼 홀홀이 가는 것이냐 떠나기 전에 일러둘 말이
```
```
'그리워서' 단어로 시작하는 총 24 단어의 윤동주체 시 생성 예제
그리워서 가거라 많은 별빛이 내린 언덕 위에 눈을 감으면 불을 끄옵니다 가슴에 꽂고 병실 안으로 의사는 젊은이의 병을 모른다 나한테는 병이 없다고 한다 이 지나친
```

## License
[MIT](https://choosealicense.com/licenses/mit/) © [송은정](http://songej.com/)
