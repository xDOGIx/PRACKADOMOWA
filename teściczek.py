# class kwadrat:
#     def __init__(self,_bok1,_bok2) -> None:
#         self.bok1 = _bok1
#         self.bok2 = _bok2
        
#     def pole(self) -> float:
#         return self.bok1 * self.bok2
    
#     def obwod(self) -> float:
#         return 2*self.bok1 + 2*self.bok2
        
# bryła1 = kwadrat(2,4)
# print(bryła1.pole())
# print(bryła1.obwod())


class Wzory:
    def __init__(self) -> None:
        pass

    @classmethod
    def prędkość(cls,s,t):
        if t == 0:
            print("Nie można dzielić przez 0")
        else:
            print(f"Prędkość w ruchu prostoliniowym : V = {s/t}")

    @classmethod
    def sila(cls,m,a):
        print(f"Siła : F = {m*a}")
    
    @classmethod
    def sila_ciezkosci(cls,m):
        print(f"Siła grawitacji : Fg = {m*9.81}")
    
    @classmethod
    def ped_ciala(cls,m,v):
        print(f"Pęd ciała : p = {m*v}")

    @classmethod
    def moc_mechaniczna(cls,w,t):
        if t == 0:
            print("Nie można dzielić przez 0")
        else:
            print(f"Moc mechaniczna : P = {w/t}")
    
    @classmethod
    def praca(cls,F,s):
        print(f"Praca mechaniczna : W = {F*s}")

    @classmethod
    def Energia_kinetyczna(cls,m,v):
        print(f"Energia kinetyczna : Ek = {(m*v**2)/2}")    

    @classmethod
    def cisnienie(cls,F,s):
        if s == 0:
            print("Nie można dzielić przez 0")
        else:
            print(f"Ciśnienie : p = {F/s}")

    @classmethod
    def Energia_potencjalna(cls, m, g, h):
        print(f"Energia potencjalna: Ep = {m * g * h}")

Wzory.prędkość(10,2)
Wzory.sila(4,4)
Wzory.sila_ciezkosci(4)
Wzory.ped_ciala(3,4)
Wzory.moc_mechaniczna(3,6)
Wzory.praca(9,2)
Wzory.Energia_kinetyczna(2,3)
Wzory.cisnienie(5,8)
Wzory.Energia_potencjalna(4,5,6)