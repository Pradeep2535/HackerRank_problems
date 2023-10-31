'''
Read a given string, change the character at a given index and then print the modified string.
'''

def mutate_string(string, position, character):
    s=list(string)
    s[position]=character
    s="".join(s)
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
