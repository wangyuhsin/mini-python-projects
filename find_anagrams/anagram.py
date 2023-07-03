"""
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant
"""

# Constants
FILE = "dictionary.txt"  # This is the filename of an English dictionary
EXIT = "-1"  # Controls when to stop the loop
dict_list = []


def main():
    """
    The main function of the Anagram Generator program.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        search = input("Find anagrams for: ")
        if search == EXIT:
            break
        else:
            find_anagrams(search)


def read_dictionary():
    """
    Reads the dictionary file and appends words to the dict_list.
    """
    with open(FILE, "r") as f:
        for line in f:
            word = line.strip()
            dict_list.append(word)


def find_anagrams(s):
    """
    Finds all the anagrams for the given input word.
    :param s: The input word.
    """
    ans_lst = []
    count_lst = []
    ans = ""
    s_length = len(s)
    ans_index = []
    s_index = []
    for i in range(len(s)):
        s_index.append(i)
    print("Searching...")
    find_anagrams_helper(s, s_length, s_index, ans,
                         ans_index, ans_lst, count_lst)
    print(sum(count_lst), "anagrams:", ans_lst)


def find_anagrams_helper(s, s_length, s_index, ans, ans_index, ans_lst, count_lst):
    """
    Recursive helper function to find anagrams.
    :param s: The input word.
    :param s_length: The length of the input word.
    :param s_index: The list of indices of the input word.
    :param ans: The current anagram.
    :param ans_index: The list of indices used in the current anagram.
    :param ans_lst: The list of found anagrams.
    :param count_lst: The list of counts for each found anagram.
    """
    if len(ans_index) == s_length or has_prefix(ans) is False:
        if ans in dict_list and ans not in ans_lst:
            print("Found:", ans)
            ans_lst.append(ans)
            count_lst.append(1)
            print("Searching...")
    else:
        for ele in s_index:
            if ele not in ans_index:
                ans_index.append(ele)
                ans = ""
                for i in ans_index:
                    ans += s[i]
                find_anagrams_helper(
                    s, s_length, s_index, ans, ans_index, ans_lst, count_lst
                )
                ans_index.pop()


def has_prefix(sub_s):
    """
    Checks if there is any word in the dictionary with the given prefix.
    :param sub_s: The prefix.
    :return: True if there is any word with the prefix, False otherwise.
    """
    for word in dict_list:
        if word.startswith(sub_s) is True:
            return True
    return False


if __name__ == "__main__":
    main()
