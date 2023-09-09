
if __name__ == '__main__':
    l=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        l.append([score, name])
    l.sort()        # sorts by the first item of child lists by default
    first = l[0][0]
    for i in range(1, n):
        if l[i][0] != first:
            j=i
            while j < n and l[i][0] == l[j][0]:
                print(l[j][1])
                j+=1
            break
