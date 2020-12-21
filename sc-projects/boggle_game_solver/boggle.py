"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dict_list = []


def main():
    """
	TODO:
	"""
    letters_lst = []
    for i in range(1, 5):
        letters = input(f'{i} row of letters: ')
        letters.lower()
        if len(letters) != 7:
            print('Illegal input')
            break
        if not letters[0].isalpha() or not letters[2].isalpha() or not letters[4].isalpha() or not letters[6].isalpha():
            print('Illegal input')
            break
        if letters[1] != ' ' or letters[3] != ' ' or letters[5] != ' ':
            print('Illegal input')
            break
        else:
            letters_lst.append(letters[0])
            letters_lst.append(letters[2])
            letters_lst.append(letters[4])
            letters_lst.append(letters[6])
    if len(letters_lst) == 16:
        read_dictionary()
        find_words(letters_lst)


def find_words(letters_lst):
    xy = []
    ans_lst = []
    ans = ''
    for x in range(4):
        for y in range(4):
            xy.append([x, y])
    find_words_helper(letters_lst, xy, [], ans_lst, ans)
    print(f'There are {len(ans_lst)} words in total.')


def find_words_helper(letters_lst, xy, current, ans_lst, ans):
    if not has_prefix(ans):
        return
    else:
        if len(current) >= 4 and ans in dict_list and ans not in ans_lst:
            print(f'Found "{ans}"')
            ans_lst.append(ans)
            a = wall_around(current)
            if len(a) != 0:
                for ele in a:
                    if ans + letters_lst[xy.index(ele)] in dict_list:
                        current.append(ele)
                        ans += letters_lst[xy.index(ele)]
                        find_words_helper(letters_lst, xy, current, ans_lst, ans)
                        current.pop()
        for ele in xy:
            if ele not in current:
                if is_neighbor(ele, current) is True:
                    current.append(ele)
                    ans = ''
                    for i in current:
                        ans += letters_lst[xy.index(i)]
                    find_words_helper(letters_lst, xy, current, ans_lst, ans)
                    current.pop()


def wall_around(current):
    lst = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if [current[len(current) - 1][0] + i, current[len(current) - 1][1] + j] not in current:
                if 4 > current[len(current) - 1][0] + i >= 0 and 4 > current[len(current) - 1][1] + j >= 0:
                    lst.append([current[len(current) - 1][0] + i, current[len(current) - 1][1] + j])
    return lst


def is_neighbor(ele, current):
    if len(current) == 0:
        return True
    else:
        if ele[0] - current[len(current) - 1][0] == 1 or ele[0] - current[len(current) - 1][0] == -1 or ele[0] - \
                current[len(current) - 1][0] == 0:
            if ele[1] - current[len(current) - 1][1] == 1 or ele[1] - current[len(current) - 1][1] == -1 or ele[1] - \
                    current[len(current) - 1][1] == 0:
                return True
        return False


def read_dictionary():
    """
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dict_list.append(word)


def has_prefix(sub_s):
    """
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
    for word in dict_list:
        if word.startswith(sub_s) is True:
            return True
    return False


if __name__ == '__main__':
    main()
