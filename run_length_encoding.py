# Homework problem from university on Algorithms and Programming on Run-Length Encoding

def decode(s: str) -> str:
    if not s:
        return ''
    else:
        seq = ''
        number = ''
        for i in s:
            if not i.isnumeric(): # was if i.isalpha(), then remembered that spaces are also encoded
                if not number:
                    seq += i
                else:
                    seq += i * int(number)
                    number = ''
            else:
                number += i
    return seq
        


def encode(s: str) -> str:
    if not s:
        return ''
    else:
        seq = ''
        count = 0
        i_prev = s[0]
        for i in s:
            if i == i_prev:
                count += 1
            else:
                if count == 1:
                    seq = seq + i_prev
                else:
                    seq = seq + str(count) + i_prev
                i_prev = i
                count = 1
        if count == 1:
            seq = seq + i_prev
        else:
            seq = seq + str(count) + i_prev
        return seq
        # вышло немного по-франкенштейнски на мой взгляд, но фурычит\
            # обошлось без костылей
                # начинал с кодирования, чтобы разобрать как это работает,\
                    # с декодированием вышло попроще


# if __name__ == '__main__':
#     
#     s = 'WWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
#     print(encode(s))
#     print(decode(s))
#
#     print(decode("2 hs2q q2w2 "))
#     print(encode("zzz ZZ  zZ"))