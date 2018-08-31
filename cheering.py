def cheering():
    """ Cheering with an and a grammar
        ver. 1
    """
    an_letter = "aefhilmnorsxAEFHILMNORSX"
    word = input("I will cheer for you. Give me a world: ")
    times = int(input("Enthusiasm level (1-10): ")) 
    i = 0
    while i < len(word):
        char = word[i]
        if char in an_letter:
            print("Give me an ", char)
        else:
            print("Give me a ", char)
        i += 1
    print("What does the spell ?")
    for i in range(times):
        print(word, "!!!")

#print(cheering())