# 6kyu Delete occurrences of an element if it occurs more than n times
# with functions!!!
def delete_nth1(order,max_e):
    return list(map(lambda x: x[1], list(filter(lambda e: order[:e[0]].count(e[1])<max_e, enumerate(order)))))
