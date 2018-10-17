def long_process(id, n):
    sum = 0
    for x in range(n):
        sum += x
        print(id, sum)
        if x < n - 1:
            yield
        else:
            yield sum


def start_many_generators(arr):
    count = 1
    R = {}
    ids = {}

    for i in arr:
        name = 'Id' + str(count)
        id = long_process(name, i)
        R[name] = None
        ids[name] = id
        count += 1

    for j in range(256):
        for k in R.keys():
            if R[k] is None:
                R[k] = next(ids[k])

    print(R)


# old code
Id1 = long_process('Id1', 10)
Id2 = long_process('Id2', 100)
Id3 = long_process('Id3', 256)
R = {'Id1': None, 'Id2': None, 'Id3': None}

for i in range(256):
    if R['Id1'] is None: R['Id1'] = next(Id1)
    if R['Id2'] is None: R['Id2'] = next(Id2)
    if R['Id3'] is None: R['Id3'] = next(Id3)

print(R)

# end of old code


list = [10, 100, 256, 78]

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
start_many_generators(list)
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')