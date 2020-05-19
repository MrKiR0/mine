def replace_dirty_words(text, bad_words):
    split_version = text.split(" ")
    value = ""
    len_bad_word = len(split_version)
    for x in range(0, len(split_version)):
        for y in range(0, len(bad_words)):
            if (split_version[x].find(bad_words[y]) != -1):
                split_version[x] = "*" * len(split_version[x])

        value = value + split_version[x] + " "
    
    return value

  

result = replace_dirty_words("I am a fucking genius and I don't give a fuck", ['fuck']) 
print (result)
