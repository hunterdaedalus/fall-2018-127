
def happy(s):
    if '_' not in s:
        for i in range(1,len(s)-1):
            if s[i] != s[i-1] and s[i] != s[i+1]:
                return False
        return True
    else:
        s = s.replace("_","")
        counts = {}
        for bug in s:
            # if bug in counts.keys():
            #     counts[bug] = counts[bug]+1
            # else:
            #     counts[bug]=1
            counts.setdefault(bug,0)
            counts[bug]=counts[bug]+1
        # if 1 in counts.values():
        #     return False
        # else:
        #     return True

        return 1 not in counts.values()

testcases = ["abcdea","abccde","aabbcccdd","abc_def","abc_ecdccdeba__","abc_abcd_abc_"]

for test in testcases:
    print(test)
    print(happy(test))
    

