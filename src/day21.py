from aocd import lines
from parse import parse
import numpy as np


word1 = np.array(list("abcdefgh"))
word2 = np.array(list("fbgdceah"))


for line in lines:
    try:
        i1, i2 = parse("swap position {:d} with position {:d}", line)
        word1[i1], word1[i2] = word1[i2], word1[i1]
        continue
    except:
        pass

    try:
        c1, c2 = parse("swap letter {:l} with letter {:l}", line)
        i1, i2 = list(word1).index(c1), list(word1).index(c2)
        word1[i1], word1[i2] = word1[i2], word1[i1]
        continue
    except:
        pass

    try:
        dir, steps, _ = parse("rotate {:l} {:d} {:l}", line)
        word1 = np.roll(word1, steps if dir == "right" else -steps)
        continue
    except:
        pass

    try:
        i1, i2 = parse("move position {:d} to position {:d}", line)
        tmp = word1[i1]
        if i1 < i2:
            word1[i1:i2] = word1[i1 + 1 : i2 + 1]
        else:
            word1[i2 + 1 : i1 + 1] = word1[i2:i1]
        word1[i2] = tmp
        continue
    except:
        pass

    try:
        (c,) = parse("rotate based on position of letter {:l}", line)
        i = list(word1).index(c)
        word1 = np.roll(word1, i + 1 + (i >= 4))
        continue
    except:
        pass

    try:
        i1, i2 = parse("reverse positions {:d} through {:d}", line)
        word1[i1 : i2 + 1] = list(reversed(word1[i1 : i2 + 1]))
        continue
    except Exception as e:
        pass

    raise ValueError


for line in reversed(lines):
    try:
        i1, i2 = parse("swap position {:d} with position {:d}", line)
        word2[i1], word2[i2] = word2[i2], word2[i1]
        continue
    except:
        pass

    try:
        c1, c2 = parse("swap letter {:l} with letter {:l}", line)
        i1, i2 = list(word2).index(c1), list(word2).index(c2)
        word2[i1], word2[i2] = word2[i2], word2[i1]
        continue
    except:
        pass

    try:
        dir, steps, _ = parse("rotate {:l} {:d} {:l}", line)
        word2 = np.roll(word2, steps if dir == "left" else -steps)
        continue
    except:
        pass

    try:
        i2, i1 = parse("move position {:d} to position {:d}", line)
        tmp = word2[i1]
        if i1 < i2:
            word2[i1:i2] = word2[i1 + 1 : i2 + 1]
        else:
            word2[i2 + 1 : i1 + 1] = word2[i2:i1]
        word2[i2] = tmp
        continue
    except:
        pass

    try:
        (c,) = parse("rotate based on position of letter {:l}", line)
        i = list(word2).index(c)
        rots = [7, 7, 2, 6, 1, 5, 0, 4]
        word2 = np.roll(word2, rots[i])
        continue
    except:
        pass

    try:
        i1, i2 = parse("reverse positions {:d} through {:d}", line)
        word2[i1 : i2 + 1] = list(reversed(word2[i1 : i2 + 1]))
        continue
    except Exception as e:
        pass


p1 = "".join(word1)
p2 = "".join(word2)
