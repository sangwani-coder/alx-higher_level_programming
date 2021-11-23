#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = ""
    if !(sentence):
        first = None
    first = sentence[0]
    return(length, first)
