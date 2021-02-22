
def solve():
    M, T2, T3, T4 = input().split()
    pizza_by_ingredients = dict()
         = dict()
    conex_grahp = [[0 for _ in range(m)] for _ in range(T2 + T3 + T4)]
    for m in range(M):
        line = input().split()
        _, *ingredients = line
        pizza_ingredients.update({m: set(ingredients)})
        
#m1 3 p1 p2 p4
#m2 4 p3 p6 p8 p7

        # 3   onion   pepper   olive
        # 2   olive cosa
        # 4   onion2   pepper2   olive    cosa2
        # 2   onion   pepper

        # 0+2 = 36, 1+3 = 16
        # 3+2 = 36, 0+1 = 16
        # onion: [1,4]
        # pepper: [1,6]
        # olive: [1,0]

solve()

