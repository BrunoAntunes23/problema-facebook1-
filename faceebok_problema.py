def verificacao(y):
    if opc.lower()=="sim" or opc.lower()=="s":
        return True

    else:
         return False

lista=[]
repeticao=True

while repeticao==True:
    
        menu=int(input("digite 1 para inserir o item ou 2 para vizualizar a lista"))
        if menu==1:
           item=str(input("insira  item"))
           lista.append(item)
        elif menu==2:
            print(lista)
        opc=input("deseja voltar ao inicio S/N")
        repeticao=verificacao(opc)
     
        
        

    
