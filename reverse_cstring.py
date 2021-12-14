def rev_withslice(s):
    return s[::-1]

input_str= 'abcdef'

if __name__=="__main__":
    print('Reverse  c-string = \0', rev_withslice(input_str))
