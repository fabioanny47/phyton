def numeros_variables():
   variados=[]
   no_variados=[]
   l=int (input("ingrese valor"))
   r=int (input("ingrese valor")) 
   k=int (input("ingrese valor"))
   if l < r:
      print ("el numero ",l,"es mayor que ", r)
      listasvariadas=[]
      for i in range(l,r+1):
         if i <= -10 or i >= 10:
            i_str=str(i)
            print(i_str)
            for j in range (0,len (i_str)):
               if(i_str[j] != i_str[j+1]):
                 listasvariadas.append(i)
               else:
                  print("el numero",i_str,"no es variado")   
         else: 
            print(i) 

   
numeros_variables()