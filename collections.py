phone_book = [
    {'name': 'Marcus Aurelius', 'phone': '+380445554433'},
    {'name': 'Іван Петренко', 'phone': '+380501234567'},
    {'name': 'Марія Іваненко', 'phone': '+380679876543'}
]

def find_phone_by_name(name):
    for i in range(len(phone_book)):
        person = phone_book[i]
        if person['name'] == name:
            return person['phone']
    return None

phone = find_phone_by_name('Іван Петренко')
print('Телефон Івана:', phone)

phone_hash = {
    'Marcus Aurelius': '+380445554433',
    'Іван Петренко': '+380501234567',
    'Марія Іваненко': '+380679876543'
}

def find_phone_by_name_hash(name):
    if name in phone_hash:
        return phone_hash[name]
    else:
        return None

phone2 = find_phone_by_name_hash('Марія Іваненко')
print('Телефон Марії:', phone2)
