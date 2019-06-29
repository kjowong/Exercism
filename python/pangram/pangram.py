def is_pangram(sentence):
    """ 
    Program to check if string is a pangram - contains all characters in the alphabet
    @Sentence: Takes in a string
    @Return: True or False 
    """
    # Create empty set to fill
    check_set = set()
    
    # Loop through sentence 
    for letter in sentence:
        # Change to lowercase if letter in string is an alpha character, add to set
        if letter.isalpha():
            lowerletter = letter.lower()
            check_set.add(lowerletter)
    
    # Check if set's length is 26 characters and return if True
    if len(check_set) == 26:
        return True
    else:
        return False
  

