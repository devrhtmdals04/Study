# How to make hashtable (dictionary) in python?
# 1. hashmap  = {}
# 2. hashmap = defaultdict(list) this dictionary is for list sryle value ex. {key=1, value=[0, 3, 6], key=2, value=[3, 6, 5]} this value can return hashmap.values(). result = [0, 3, 6], [3, 6, 5]

# How to get alphabet order index?
# ord(char) - ard('a') if char is 'b' it returns 1.

# How to make clean string?
# use upper() or lower() and isalnum() (is alphabet numeric?) clean_str = "".join(s.lower() for s in str if s.isalnum())

# checklist
# if you did 'tuple(list)' the 'list' doesn't tuplicated. do tupled = tuple(list) and use tupled, then, tupled will be tuble.

# why two-pointer neds sort? 
# 1. Avoid Duplications. use while comparison. 
# 2. Optimization pointing. if you need sum, if the diff is lower than you want, upper left pointer of sorted list, than you can get optimized pointer.

# make dictionary by Pythonic way: 'dict[key] = dict.get(key, default) + 1' this will make your code compact. by using this 

# How to sort dictionary by items?
# sorteddictbyitems = sorted(dict.items(), key = lambda x:x[1], reverse=True) this is Descending order, if you wand right order, use reverse=False.
# Or use this Pythonic method: dict.get(key, value)

# how to make index rule in two-dimention list?
# you have i, j for two-dimention list. each index can get 0~2 values. so you can product 3times one of then(particulary i).
# so, use '(i//3)*3 + (j//3)'.

