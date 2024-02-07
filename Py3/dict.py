phone_book = {'Jonas': '+62817', 'Steve': '+62919', 'Rally' : '+6281921'}

def add(key, val):
    phone_book[key] = val
def display():
    for item in phone_book:
        print(item, ":" , phone_book.get(item))

add('Rico', '+1 817')
display()


