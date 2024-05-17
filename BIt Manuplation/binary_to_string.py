"""
Binary to String : Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary with at most 32 characters,
print "ERROR:'
"""


def binary_to_string(num):
    if num >= 1 or num <= 0:
        return "ERROR"
    binary = ['.']

    while num > 0:
        if len(binary) >= 32:
            return "ERROR"

        r = num * 2
        if r >= 1:
            binary.append('1')
            num = r - 1
        else:
            binary.append('0')
            num = r

    return ''.join(binary)


def binary_to_string2(num):
    if num >= 1 or num <= 0:
        return "ERROR"
    binary = ['.']

    frac = 0.5
    while num > 0:
        if len(binary) >= 32:
            return "ERROR"
        if num >= frac:
            binary.append('1')
            num -= frac
        else:
            binary.append('0')
        frac /= 2

    return ''.join(binary)


if __name__ == "__main__":
    print(binary_to_string(0.75))
    print(binary_to_string2(0.75))
