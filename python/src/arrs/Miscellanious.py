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
        for str in strs:
            if !str.startswith(str):
                



if __name__ == "__main__":
    print(longest_prefix(["abcd", "abbd", "abdy", "az"]))