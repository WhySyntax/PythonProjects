from Functions.TheFuncts import Functs as f
def squaremaker(a):
    def FML():
        return '+----------+'+'----------+'*(a-1)
    def Others():
        return '|          |'+'          |'*(a-1)
    return FML,Others
LengthOfSides=f.int2('What length do you wish for your sides to be? ')
FML,Others=squaremaker(LengthOfSides)
for x in range(LengthOfSides):
    print(FML())
    for x in range(5):
        print(Others())
print(FML())
