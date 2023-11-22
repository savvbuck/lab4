ITEMS = {
    'в': (3, 25),
    'п': (2, 15),
    'б': (2, 15),
    'а': (2, 20),
    'и': (1, 5),
    'н': (1, 15),
    'т': (3, 20),
    'о': (1, 25),
    'ф': (1, 15),
    'д': (1, 10),
    'к': (2, 20),
    'р': (2, 20),
}

ITEMS = dict(sorted(ITEMS.items(), key = lambda x: x[1][0]))
CURR_VAL = 15
LENGTH = 4
WIDTH = 2

def get_area_value_key(items):
    area = [items[item][0] for item in items]
    value = [items[item][1] for item in items]   
    key = [item for item in items]     
    return area, value, key


def get_memtable(items, A=8):
    area, value, key = get_area_value_key(items)
    n = len(value)
    V = [[0 for a in range(A+1)] for i in range(n+1)]
    for i in range(n+1):
        for a in range(A+1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif area[i-1] <= a:
                V[i][a] = max(value[i-1] + V[i-1][a-area[i-1]], V[i-1][a])
            else:
                V[i][a] = V[i-1][a]     
        print(V[i])
    return V, area, value, key


def get_selected_items_list(items, A=8):
    V, area, value, key = get_memtable(items)
    n = len(value)
    res = V[n][A]
    items_list = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i-1][A]:
            continue
        else:
            items_list.append((area[i-1], value[i-1], key[i-1]))
            res -= value[i-1]
            A -= area[i-1]       
    print(items_list)
    return items_list

def backpack_show(items):
    C = []
    for item in get_selected_items_list(items):
        if item[0] <= WIDTH:
            C.append([item[2]]*item[0])
    for i in range(LENGTH):
        if len(C[i]) == len(C[i+1]) == 1:
            C[i] = C[i] + C[i+1]
            del C[i+1]       
    for i in range(len(C)):
        print(C[i])                

backpack_show(ITEMS)
