import re


class Name:

    @staticmethod
    def count_characters(s):
        all_freq = {}
        for i in s:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
        print(all_freq)
        return all_freq

    @staticmethod
    def count_words(s):
        str = s.split()
        str2 = []
        for i in str:
            if i not in str2:
                str2.append(i)
        dic = {}
        for i in range(0, len(str2)):
            dic[str2[i]] = str.count(str2[i])
        print(dic)


Name.count_characters("Hello world")
Name.count_words("Hello world" )
