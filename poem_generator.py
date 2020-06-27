import pandas as pd
from string import punctuation
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from tensorflow.keras.utils import to_categorical

df=pd.read_csv('poem.csv')

text = []
text.extend(list(df.poem.values))

t = Tokenizer()
t.fit_on_texts(text)
vocab_size = len(t.word_index) + 1

sequences = list()

for line in text:
    encoded = t.texts_to_sequences([line])[0]
    for i in range(1, len(encoded)):
        sequence = encoded[:i+1]
        sequences.append(sequence)

index_to_word={}
for key, value in t.word_index.items():
    index_to_word[value] = key

max_len=max(len(l) for l in sequences)

sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')

sequences = np.array(sequences)
X = sequences[:,:-1]
Y = sequences[:,-1]

Y = to_categorical(Y, num_classes=vocab_size)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM

model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_len-1))
model.add(LSTM(128))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=200, verbose=2)

def sentence_generation(model, t, current_word, n):
    init_word = current_word
    sentence = ''
    for _ in range(n):
        encoded = t.texts_to_sequences([current_word])[0]
        encoded = pad_sequences([encoded], maxlen=75, padding='pre')
        result = model.predict_classes(encoded, verbose=0)
        for word, index in t.word_index.items(): 
            if index == result:
                break
        current_word = current_word + ' '  + word
        sentence = sentence + ' ' + word
    sentence = init_word + sentence
    return sentence

print("'나는' 단어로 시작하는 총 24 단어의 윤동주체 시 생성 예제")
print(sentence_generation(model, t, '나는', 24))

print("'그리워서' 단어로 시작하는 총 24 단어의 윤동주체 시 생성 예제")
print(sentence_generation(model, t, '그리워서', 24))

print('윤동주체 시 생성기가 어떤 단어로 시를 시작할 것인지 단어를 입력해주세요.')
poem_word_start=str(input())

print('윤동주체 시 생성기가 몇 단어로 시를 쓸 것인지 숫자를 입력해주세요.')
poem_word_count=int(input())

print(poem_word_start, '단어로 시작하는 총', poem_word_count, '단어의 윤동주체 시 생성 예제')
print(sentence_generation(model, t, poem_word_start, poem_word_count))
