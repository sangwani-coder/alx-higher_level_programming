#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dic = {'john':12, 'bob':14, 'mike':14, 'moly':16, 'adam':10}
best_key = best_score(a_dic)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
