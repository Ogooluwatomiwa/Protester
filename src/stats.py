# stats.py
# Writing a program for statistics
import statistics as sta

def stats(x):
    mn = sta.mean(x)
    medi = sta.median(x)
    mod = sta.mode(x)
    assert x == mn
    assert x == medi
    assert x == mod
