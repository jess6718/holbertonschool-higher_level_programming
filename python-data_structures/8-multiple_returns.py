#!/usr/bin/python3
def multiple_returns(sentence):
    result = (len(sentence), sentence[0])
    if len(sentence) == 0:
        result = (0, None)
    return result
