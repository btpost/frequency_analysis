import sys
sys.path.insert(0, '../')
from collections import Counter

def frequency(args, text):
    if args == []:
        return frequency_distribution(text)
    elif args[0] == '-kl':
        return frequency_distribution(text, key_length=int(args[1]))
    else:
        raise ValueError('invalid input', args)

def frequency_distribution(text, key_length=1):
    dist_list = []
    i = 0
    for i in range(key_length):
        dist_list.append(Counter())
    
    i = 0
    while i < len(text)-key_length:
        for j in range(key_length):
            curr_counter = dist_list[j]
            curr_counter[text[i+j]] += 1
        i += key_length
    return dist_list