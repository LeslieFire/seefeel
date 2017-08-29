#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: leslie
# date: 2017-08-24
# email: 249893977@qq.com

from collections import defaultdict
import jieba
import os

STOP_WORDS_PATH = 'stop_words.txt'

_get_abs_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), path))

def stop_words():
    with open(_get_abs_path(STOP_WORDS_PATH), 'r') as file:
        words = [ line.strip() for line in file]
    return set(words)

stop_words = stop_words()
print('Loading {} stopwords. '.format(len(stop_words)))


def ngram_tokenizer_and_filter_stopwords(text, ngram = 2):
    return filter(lambda x: x not in stop_words and len(x) > 1, ngram_tokenizer(text, ngram))

def tokenize_and_filter_stopwords(text):
    if type(text) is str:
        return filter(lambda x: x not in stop_words , jieba.cut(text))
    else:
        return []


def bigram_tokenizer(text):
    words = list(jieba_tokenizer(text))
    rst = []
    if len(words) > 1:
        for i in range(len(words) - 1):
            rst.append(words[i] + words[i + 1])
    else:
        rst = words
            
    return rst


# 生成ngram, 建议最大5
def ngram_tokenizer(text, ngram = 2):
    words = list(jieba_tokenizer(text))
    rst = []
    rst.extend(words)
    
    for i in range(1, ngram):
        ngram = []
        for j in range(len(words) - i):
            gram_word = ""
            for k in range(i + 1):
                gram_word += words[j + k]
            ngram.append(gram_word)
            
        rst.extend(ngram)
    return rst



def jieba_tokenizer(text):
    return filter(lambda x: len(x.strip()) > 0 , jieba.cut(text))