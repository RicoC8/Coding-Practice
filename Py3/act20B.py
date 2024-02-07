Pi = 3.14

SquareSide = 5
AreaSquare = SquareSide * SquareSide

RectBreadth = 5
RectLength = 5
AreaRectangle = RectBreadth * RectLength

TriBase = 5
TriHeight = 5
AreaTriangle = 0.5 * TriBase * TriHeight

ParallelBase = 5
ParallelHeight = 5
AreaParallel = ParallelBase * ParallelHeight

Radius = 5
AreaCircle = Pi * Radius * Radius

print(AreaSquare)
print(AreaRectangle)
print(AreaTriangle)
print(AreaParallel)
print(AreaCircle)

# ----

def CalcAreaSquare(SquareSide):
    AreaSquare = SquareSide * SquareSide
    print(AreaSquare)

def CalcAreaRect(RectBreadth, RectLength):
    AreaRect = RectBreadth * RectLength
    print(AreaRect)

def CalcAreaTriangle(TriBase, TriHeight):
    AreaTriangle = 0.5 * TriBase * TriHeight
    print(AreaTriangle)

def CalcAreaParallel(ParallelBase, ParallelHeight):
    AreaParallel = ParallelBase * ParallelHeight
    print(AreaParallel)

def CalcAreaCircle(Radius):
    AreaCircle = Pi * Radius * Radius
    print(AreaCircle)

CalcAreaSquare(5)
CalcAreaRect(5, 5)
CalcAreaTriangle(5, 5)
CalcAreaParallel(5, 5)
CalcAreaCircle(5)
