DIAS_CONSUMO = 'dias para consumo'
TAMANHO = 'tamanho'

def inserir_panc(lista_pancs:dict, nome:str, dias_consumo:int, tamanho:float) -> None:
    lista_pancs[nome] = {DIAS_CONSUMO: dias_consumo, TAMANHO:tamanho}
    return

lista_pancs = {
    'jambu':{DIAS_CONSUMO: 100, TAMANHO: 0.4}, 
               }

print(lista_pancs['jambu'])
print(lista_pancs['jambu'][DIAS_CONSUMO])
print(lista_pancs['jambu'][TAMANHO])

inserir_panc(lista_pancs, 'peixinho da orta', 123, 0.1)
print(lista_pancs)