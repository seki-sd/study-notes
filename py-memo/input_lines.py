# -*- coding: utf-8 -*-

def input_lines():
    stopword = ''
    input_list = []
    for line in iter(input, stopword):
        input_list.append(line)
    return input_list