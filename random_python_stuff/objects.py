brooke = {
    'name':'Brooke',
    'height':'kinda tall',
    'hair color':'sandy brown',
    'age':'18'}

print(brooke)



class Person(object):
    def __init__(
    self, name, age, hair_color, eyesight,
    siblings, hair, sports):
        self.name = 'Brooke'
        self.hair = 'curly'
        self.age = 18
        self.eyesight = 'bad'
        self.sports = 'basketball'
        self.hair_color = 'sandy brown'
        self.siblings = 2
        self.hungry = True


    def see(self, glasses):
        print('I am putting on {glasses}'.format(glasses = glasses))
        # self.hungry = false
        self.eyesight = 'better'

    def __str__(self):
        brooke_string = 'Name: {n}, Age: {a}, Eyesight: {e}'.format(n= 'brooke', a= '18', e= )
brooke = Person(
    name = 'Brooke',
    age = 18,
    hair_color ='sandy brown',
    eyesight = 'bad',
    siblings = 2,
    hair = 'curly',
    sports = 'basketball')

sage = Person(
    name = 'Sage',
    age = 17,
    eyesight = 'okay',
    hair_color = 'redish brown',
    siblings = 'idk',
    hair = 'straight',
    sports = 'dance')

print(brooke.name)
brooke.see('contacts')
print('Brooke is hungry: {h}',format(h=brooke.name))
print(sage.name)
print('Sage is hungry: {h}',format(h=Sage.name))
