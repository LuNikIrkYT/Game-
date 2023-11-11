a = []
def sp(n):
    p = [0] * (n + 2)
    for i in range(n + 2):
        p[i] = ['0'] * (n + 2)
    for i in range(n + 2):
        p[0][i] = 3
        p[n + 1][i] = 3
        p[i][0] = 3
        p[n + 1][i] = 3
    p[8][8] = '1'
    p[8][2] = '2'
    p[2][2] = '3'

    return p
    

def vp(n, p):
    for i in range(1, n + 1, 1):
        for j in range(1, n + 1, 1):
            print(p[i][j], end = '  ')
        print()

#тест
        
n = 15
p = sp(n)
vp(n, p)

print()
print('---------------------------------------------------')
print('0 - незанятая клетка')
print('1 - клетка с главным героем')
print('2 - клетка с "посылкой"')
print('3 - клетка с "домом"')