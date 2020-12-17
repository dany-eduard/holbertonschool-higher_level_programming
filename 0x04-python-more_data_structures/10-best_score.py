#!/usr/bin/python3
def best_score(a_dictionary):
        if a_dictionary:
                max = 0
                for key, value in a_dictionary.items():
                        if value > max:
                                max = value
                                b_key = key
                return b_key
        else:
                return None
