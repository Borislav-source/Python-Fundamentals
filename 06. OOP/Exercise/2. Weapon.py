class Weapon:
    def __init__(self, bullets):
        self.bullets = int(bullets)

    def shoot(self):
        if int(self.bullets) > 0:
            self.bullets -= 1
            return 'shooting...'
        return 'no bullets left'

    def __repr__(self):
        if self.bullets < 0:
            self.bullets = 0
        return f'Remaining bullets: {self.bullets}'.format(self=self)


weapon = Weapon('7')
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)

