# Mantendo estados dentro da classe:


class Camera:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming

    def film(self):
        if self.filming:
            print(f'{self.name} is already filming...')
            return

        print(f'{self.name} is filming...')
        self.filming = True

    def stop_filming(self):
        if not self.filming:
            print(f'{self.name} is not filming...')
            return

        print(f'{self.name} is stopping filming...')
        self.filming = False

    def photograph(self):
        if self.filming:
            print(f'{self.name} can not photograph and filming')
            return

        print(f'{self.name} is photographing...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.film()
c1.film()
c1.photograph()
c1.stop_filming()
c1.photograph()

print()

c2.stop_filming()
c2.film()
c2.film()
c2.photograph()
c2.stop_filming()
c2.photograph()
