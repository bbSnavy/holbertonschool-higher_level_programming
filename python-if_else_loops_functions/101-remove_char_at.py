#!/usr/bin/python3
def remove_char_at(str, n):
    return ''.join([str[i] for i, _ in enumerate(str) if i != n])
