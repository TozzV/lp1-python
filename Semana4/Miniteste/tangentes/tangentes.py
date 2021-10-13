import math;

angulo_inicial = float(input())
delta = float(input())
linhas_desejadas = int(input())

tangentes = [angulo_inicial]


for i in range(linhas_desejadas):
    radiano = math.radians(angulo_inicial)
    tangente = math.tan(radiano)
    if linhas_desejadas > 1:
        angulo_inicial += tangente
        print(f'{angulo_inicial:.2f}', f'{tangente:.4f}')
        

  
         

    
    
        
    

