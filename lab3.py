def solve(numheads,numlegs):
    """4x + 2y = 94
    x + y = 35, x = 35 - y
    140 - 2y = 94
    -2y = -46 
    y = 23
    x = 12"""
    for chick in range(numheads + 1):
        rab = numheads - chick
        if(chick * 2 + rab * 4) == numlegs:
            return chick, rab
heads = 35
legs = 94
print(solve(heads,legs))

    