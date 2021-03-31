def numeros_variables():
    l=int (input("ingrese valor de l "))
    r=int (input("ingrese valor de r ")) 
    k=int (input("ingrese valor de k "))
    
    if l < r:
        print ("el numero ",l,"es mayor que ", r)
        listasvariadas=[]
        for i in range(l,r+1):
            i_str=str(i)
            is_variado = True
            if i <= -10 or i >= 10:              
                for j in range (0,len(i_str) - 1):
                    if(i_str[j] != i_str[j+1]):
                        print('')
                    else:
                        is_variado = False
                        #print("el numero",i_str,"no es variado")     
            if is_variado:
                listasvariadas.append(i)   
        else: 
            print("el numero",i,"no es variado")
        
        print(listasvariadas)
        if (k >= 0 and k <len(listasvariadas)):
            print('El número variado en la posición ',k,'-ésima es ',listasvariadas[k])
        else:
            print('La posición ',k,'-ésima no existe')
    

   
numeros_variables()