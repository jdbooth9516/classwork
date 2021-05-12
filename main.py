import random

def get_favorite():
    language = ['python', 'C++', 'Java', 'Javascript']
    found_language = False
    user_input = input("What is you favorite programming language? ")

    for lan in language:
        if user_input == lan:
            found_language = True
            return print('We have found your language')

    else:
        print("We didn't find your language")


#get_favorite()


def get_random(min, max):
    rand_num = random.randint(min, max)
    return rand_num


# print(get_random(1, 100))


def reverse_word(word):
    return word[::-1]


# print(reverse_word('monty'))


def count_down():
    i = 100
    while i > 0:
        if i % 4 == 0 and i % 7 == 0:
            print("Flamingo-Banana")
        elif i % 7 == 0:
            print("Flamingo")
        elif i % 4 == 0:
            print("Banana")
        else:
            print(i)
        i -= 1


# count_down()

def reduce_list():
    num_list = [1, 2, 3, 7, 8, 9, 45, 134, 43, 2, 3, 1, 6, 7, 5, 4]

    new_list = {x for x in num_list if x < 5}

    print(new_list)


# reduce_list()


def get_centenial():
    user_age = int(input("Please enter you age: "))
    current_year = 2021
    difference = 100 - user_age

    centenial = current_year + difference

    return centenial



# print(get_centenial())


def compare_list():
    list_a = []
    list_b = []

    for i in range(20):
        list_a.append(random.randint(1, 100))

    for j in range(20):
        list_b.append(random.randint(1, 100))

    dup_list = [x for x in list_b if x in list_a]
    print(list_a)
    print()
    print(list_b)
    print()
    print(dup_list)


# compare_list()

def anagram(word_a, word_b):
    list_a = []
    list_b = []
    for x in word_a:
        list_a.append(x)

    for y in word_b:
        list_b.append(y)

    list_a.sort()
    list_b.sort()
    length = len(list_a)
    i = 0


    while i < length:
        if list_a[i] != list_b[i]:
            return f"{word_a} and {word_b} are NOT anagrams"
        i += 1

    else:
        return f"{word_a} and {word_b} are anagrams"


# print(anagram("are", "rea"))


def reverse_word_in_phrase(phrase):
    words = phrase.split()
    reversed_words = [x[::-1] for x in words]
    reversed_phrase = " ".join(reversed_words)
    return reversed_phrase


# print(reverse_word_in_phrase("Hello world I am a programmer"))

def build_pyramid(num):
    num_space = num
    num_star = num


    while num > 0:
        level = " " * num_space + "*" * num_star
        print(level)
        num_space += 1
        num_star -= 2
        num -= 2


build_pyramid(int(input("Please Select a odd number: ")))




