# 1․

import math
def f(r, alpha):
    alpha.d = alpha * (180 / math.pi)
    return (math.pi * r ** 2) * alpha.d / 360

# 3.

def l(word):
    max_word = max(len(i) for i in word)
    return [i for i in word if len(i) == max_word]