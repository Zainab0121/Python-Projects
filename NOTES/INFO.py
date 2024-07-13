### Mapping, Filtering and Lambda

def square(num):
    return num**2
square(9)

my_list= [9, 8, 7, 6, 5]
c = []
for i in my_list:
    c.append(square(i))

# map
c = list(map(square, my_list))


#filterring
list(filter(lambda i: i%2 == 0, c))


