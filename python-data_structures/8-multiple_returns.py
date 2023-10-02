#!/usr/bin/python3
def multiple_returns(sentence):
    result = (len(sentence), sentence[0])
    if sentence is None:
        result = (len(sentence), None)
    return result
