'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

word = "abcthxyzth"


def count_th(word):
    # set count to 0
    count = 0

    # base case
    if len(word) <= 1:
        return 0
        print("len(word", len(word))

    elif "th" in word:
        # index of first and second letters
        if word[0] == 't' and word[1] == 'h':
            print(count)
            count += 1
            print("word[0]", word[0])
            print("word[1]", word[1])

    # start at 1st letter and iterate through with count
    print(count_th(word[1:]) + count)
    return count_th(word[1:]) + count


print(len(word))
print(word[0])
print(word[1])
count_th(word)
