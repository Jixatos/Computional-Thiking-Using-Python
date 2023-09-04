x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]
w = [113, 88, 58, 65, 71, 46, 36, 33, 37, 40, 24, 21, 20, 15, 20]

def cal_aritmetica(x):
    N = len(x)
    somatorio = 0
    for i in range(N):
        somatorio+=x[i]
    media_aritmetica = somatorio/N
    return media_aritmetica

def cal_geometrica(x):
    N = len(x)
    produtorio = 1
    for i in range(N):
        produtorio*=x[i]
    media_geometrica = produtorio**(1/N)
    return media_geometrica

def cal_harmonica(x):
    N = len(x)
    soma = 0
    for i in range(N):
        soma+=1/x[i]
    media_harmonica = N/soma
    return media_harmonica

def cal_ponderada(x,w):
    soma = 0
    multi = 1
    for i in range(len(x)):
        multi = multi + (w[i] * x[i])
        soma+=w[i]
    media_ponderada = multi/soma
    return media_ponderada

def cal_var_populacional(x):
    N = len(x)
    somatorio = 0
    media = cal_aritmetica(x)
    for i in range(0,N):
        somatorio+=(x[i] - media)**2
    var_populacional = somatorio/N
    return var_populacional

def cal_var_amostral(x):
    N = len(x)
    somatorio_amostral = 0
    media = cal_aritmetica(x)
    for i in range(0,N):
        somatorio_amostral+=(x[i] - media)**2
    var_amostral = somatorio_amostral/(N - 1)
    return var_amostral

def cal_desvio_pp(x):
    variancaPP = cal_var_populacional(x)
    desvio_pp = variancaPP**(1/2)
    return desvio_pp

def cal_desvio_pa(x):
    variancaPA = cal_var_amostral(x)
    desvio_pa = variancaPA**(1/2)
    return desvio_pa

print(cal_var_populacional(x))
print(cal_var_amostral(x))
print(cal_desvio_pp(x))
print(cal_desvio_pa(x))

