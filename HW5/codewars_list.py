# 8kyu Invert values
def invert(l):
    return [-x for x in l]

# 7kyu Regex validate PIN code
def validate_pin(pin):
    return pin.isdigit() and (len(pin)in [4,6])

# 6kyu Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    new = []
    for x in order:
        if new.count(x)<max_e:
            new.append(x)
    return  new
    #return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ]


