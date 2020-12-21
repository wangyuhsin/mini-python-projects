"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_list = []


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        search = input('Find anagrams for: ')
        if search == EXIT:
            break
        else:
            find_anagrams(search)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dict_list.append(word)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    ans_lst = []
    count_lst = []
    ans = ''
    s_length = len(s)
    ans_index = []
    s_index = []
    for i in range(len(s)):
        s_index.append(i)
    print('Searching...')
    find_anagrams_helper(s, s_length, s_index, ans, ans_index, ans_lst, count_lst)
    print(sum(count_lst), 'anagrams:', ans_lst)


def find_anagrams_helper(s, s_length, s_index, ans, ans_index, ans_lst, count_lst):
    if len(ans_index) == s_length or has_prefix(ans) is False:
        if ans in dict_list and ans not in ans_lst:
            print('Found:', ans)
            ans_lst.append(ans)
            count_lst.append(1)
            print('Searching...')
    else:
        for ele in s_index:
            if ele not in ans_index:
                ans_index.append(ele)
                ans = ''
                for i in ans_index:
                    ans += s[i]
                find_anagrams_helper(s, s_length, s_index, ans, ans_index, ans_lst, count_lst)
                ans_index.pop()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return: boolean
    """
    for word in dict_list:
        if word.startswith(sub_s) is True:
            return True
    return False


if __name__ == '__main__':
    main()
