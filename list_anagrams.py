# list1 = ['helloto', 'world', 'none', 'crown', 'foo', 'ofo']
# list2 = ['othello', 'dream', 'onen', 'prince', 'foo', 'bar', 'telegram']

# Print all the words of List 1 and List 2 which are anagrams of each other
anagram_set = {}

def is_anagram(word1, word2):
    if (sorted(word1) == sorted(word2)):
        return True
    else:
        return False
        
def print_anagrams(list1, list2):
    for word in list1:
        word_list = [word]
        sorted_key = ''.join(sorted(word))
        anagram_set[sorted_key] = word_list
    for word in list2:
        sorted_key = ''.join(sorted(word))
        word_list = anagram_set.get(sorted_key, None)
        if word_list is not None:
            word_list.append(word)
            anagram_set[sorted_key] = word_list
    all_values = []
    for value in anagram_set.values():
        if len(value) > 1:
            all_values.append(value)
    print (all_values)

def main():
    list1 = ['helloto', 'world', 'none', 'crown', 'foo', 'ofo' , 'facebook', 'book']
    list2 = ['othello', 'dream', 'onen', 'prince', 'foo', 'bar', 'telegram', 'bookface', 'koob']
    
    print_anagrams(list1, list2)
    
if __name__ == "__main__":
    main()
