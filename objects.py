def fn():
    obj1 = {'name': 'Іван'}
    obj2 = {'name': 'Петро'}
    
    obj1['name'] = 'Микола'
    obj2['name'] = 'Сергій'
    
    print('obj1:', obj1)
    print('obj2:', obj2)
    
    return obj1, obj2

fn()

def create_user(name, city):
    user = {}
    user['name'] = name
    user['city'] = city
    return user

user = create_user('Marcus Aurelius', 'Roma')
print('Користувач:', user)
