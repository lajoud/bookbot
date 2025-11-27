def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(items):
    return items["num"]

def sorted_dict(chars_dict):
    new_list=[]
    for key,value in chars_dict.items():
        new_list.append({"char":key,"num":value})

    new_list.sort(reverse=True,key=sort_on)
    
    
    return new_list

def report_print(dict_list, path, num_words):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for element in dict_list:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")

    