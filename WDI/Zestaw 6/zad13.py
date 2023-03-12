def solve(num):
    def recur(num, val=1, tab=[]):
        if num - val == 0:
            if not tab or val >= tab[-1]:
                tab += [val]
                print(tab)
            return
        #odcinam
        if not tab or val >= tab[-1]:
            recur(num - val, 1, tab + [val])
        #przedluzam
        recur(num, val + 1, tab)
    recur(num)

#solve(5)


def solve2(num):
    def recur(num, tab=[]):
        if num == 0:
            print(tab)
            return
        
        prev_val = tab[-1] if tab else 1

        for val in range(prev_val, num + 1):
            recur(num - val, tab + [val])
        
    recur(num)

solve2(5)