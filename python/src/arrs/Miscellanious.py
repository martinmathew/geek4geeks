def longest_prefix(strs):
    index = 0

    prefix = ""
    for index in range(len(min(strs,key=len))):
        chr = strs[0][index]
        for i in range(len(strs)):
            if strs[i][index] != chr:
                return prefix


        prefix = prefix + chr
    return prefix


def lp_bs(strs,start,end):
    if start < end:
        str = strs[0][start:end]
        for str1 in strs:
            if str1.startswith(str) is False:
                mid = int((start+end)/2)
                return lp_bs(strs,start,mid)
        mid = int((start+end)/2)
        return str+lp_bs(strs,mid+1,end)
    else:
        return ""



if __name__ == "__main__":
    print(lp_bs(["abcd", "abbd", "abdy", "abc"],0,2))