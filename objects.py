def fn():
    obj1 = {'name': 'Тревіс Скотт'}
    obj2 = {'name': 'Клавдія Петрівна'}
    
    obj1['name'] = 'Кирило Кузнецов'
    obj2['name'] = 'Тревіс Скотт'
    
    print('obj1:', obj1)
    print('obj2:', obj2)
    
    return obj1, obj2

fn()

def create_user(name, city):
    user = {}
    user['name'] = name
    user['city'] = city
    return user

user = create_user('Клавдія Петрівна', 'Київ')
print('Користувач:', user)
