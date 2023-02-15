from random import randint as RI

def my_bot(n: int) -> int:
    if n > 28:
        for i in range(28, 0, -1):
            if (n - i) %28 != 0 and n-i > 28 :
                return i
        else:
            return RI(1,28)
    else:
        return n