# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    case=""
    for i in s:
        if i.isupper():
            case+=i.lower()
        elif i.islower():
            case+=i.upper()
        else:
            case+=i
    return case

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)