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

if __name__ == "__main__":
    print(longest_prefix(["abcd", "abbd", "abdy", "az"]))