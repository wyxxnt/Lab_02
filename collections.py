def find_phone_by_name(name):
    for i in range(len(phone_book)):
        person = phone_book[i]
        if person['name'] == name:
            return person['phone']
    return None

phone = find_phone_by_name('Тревіс Скотт')
print('Телефон Тревіса:', phone)

phone_hash = {
    'Кирило Кузнецов': '+380445554433',
    'Тревіс Скотт': '+380501234567',
    'Клавдія Петрівна': '+380679876543'
}

def find_phone_by_name_hash(name):
    if name in phone_hash:
        return phone_hash[name]
    else:
        return None

phone2 = find_phone_by_name_hash('Клавдія Петрівна')
print('Телефон Клавдії:', phone2)
