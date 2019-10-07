def word_count(file_name):# put your code here.
    file = open(file_name)
    word_list = []
    for line in file:
        line = line.rstrip()
        line = line.split(" ")
        word_list = word_list + line

    # #Does not work, come back and fix this section
    # for word in word_list:
    #     word = word.replace(",", "")
    #     word = word.replace(".", "")
    #     word = word.replace("?", "")

    word_counts = {}
    for word in word_list:
        word_counts[word] = word_counts.get(word, 0) + 1


    for item, count in word_counts.items():
        print(f'{item} {count}')

    return ""
#print(word_count("test.txt"))
print(word_count("twain.txt"))