<<<<<<< HEAD
table = {
    'outwear':{
        'ukr':[40,42,44,46,48,50,52,54],
        'ger':[34,36,38,40,42,44,46,48],
        'fra':[36,38,40,42,44,46,48,50],
        'ita':[38,40,42,44,46,48,50,52],
        'usa':[6,8,10,12,14,16,18,20],
        'uk' :[8,10,12,14,16,18,20,22],
        'int':['S','M','M','L','L', 'XL', 'XL', 'XXL']
    },
    'women':{
        'ukr':[40,42,44,46,48,50,52,54],
        'ger':[34,36,38,40,42,44,46,48],
        'fra':[36,38,40,42,44,46,48,50],
        'usa':[8,10,12,14,16,18,20,22],
        'uk' :[24,26,28,30,32,34,36,38],
        'int':['XXS','XS','S','M','L', 'XL', 'XXL', 'XXXL']
        }
    }


def get_size(ukr_size, size_type, country):
    try:
        res = table[size_type][country][table[size_type]['ukr'].index(ukr_size)]
    except:
        return 'Wrong parameters!'
    else:
        return res
=======
table = {
    'outwear':{
        'ukr':[40,42,44,46,48,50,52,54],
        'ger':[34,36,38,40,42,44,46,48],
        'fra':[36,38,40,42,44,46,48,50],
        'ita':[38,40,42,44,46,48,50,52],
        'usa':[6,8,10,12,14,16,18,20],
        'uk' :[8,10,12,14,16,18,20,22],
        'int':['S','M','M','L','L', 'XL', 'XL', 'XXL']
    },
    'women':{
        'ukr':[40,42,44,46,48,50,52,54],
        'ger':[34,36,38,40,42,44,46,48],
        'fra':[36,38,40,42,44,46,48,50],
        'usa':[8,10,12,14,16,18,20,22],
        'uk' :[24,26,28,30,32,34,36,38],
        'int':['XXS','XS','S','M','L', 'XL', 'XXL', 'XXXL']
        }
    }


def get_size(ukr_size, size_type, country):
    try:
        res = table[size_type][country][table[size_type]['ukr'].index(ukr_size)]
    except:
        return 'Wrong parameters!'
    else:
        return res
>>>>>>> e434180a3c7da68eaa676270f57471358d0fdc29
