import numpy as np

class tablero(): 
    def __init__(self):
        self.color=["⬛","⬜"]
        self.tablero_blank = np.zeros((8,8))
        self.tablero = np.zeros((8,8),dtype=str)
        self.init_tablero()
        self.piezas = piezas()
        self.init_piezas_tablero()
    
    def __str__(self):
        letters = ['A','B','C','D','E','F','G','H']
        numbers = ['8','7','6','5','4','3','2','1']
        tablero_str = "TABLERO----------\n"
        for line in range(0,8):
            tablero_str += numbers[line] + " " 
            for posicion in range(0,8):
                if(self.tablero[line][posicion]=='0'): 
                    tablero_str += self.color[0] + " "
                elif(self.tablero[line][posicion]=='1'):
                    tablero_str += self.color[1] + " "
                else:
                    tablero_str += str(self.tablero[line][posicion]) + " " 
            tablero_str += "\n"

        tablero_str += "· "
        for line in range(0,8):
            tablero_str += str(letters[line]) + " "
        tablero_str += "\n"

        tablero_str += "-----------------\n"

        return tablero_str

    def init_tablero(self):
        color_index = 0
        for line in range(0,8):
            for posicion in range(0,8):
                color_index=color_index%2
                self.tablero_blank[line][posicion] = color_index
                self.tablero[line][posicion] = color_index
                color_index+=1
            color_index+=1

    def init_piezas_tablero(self):

        self.tablero[6] = self.piezas.pieza_a_notacion("peon","blanca")
        self.tablero[1] = self.piezas.pieza_a_notacion("peon","negra")
        for posicion in [0,7]:
            self.tablero[7][posicion] = self.piezas.pieza_a_notacion("torre","blanca")
            self.tablero[0][posicion] = self.piezas.pieza_a_notacion("torre","negra")
        for posicion in [1,6]:
            self.tablero[7][posicion] = self.piezas.pieza_a_notacion("caballo","blanca")
            self.tablero[0][posicion] = self.piezas.pieza_a_notacion("caballo","negra")
        for posicion in [2,5]:
            self.tablero[7][posicion] = self.piezas.pieza_a_notacion("arfil","blanca")
            self.tablero[0][posicion] = self.piezas.pieza_a_notacion("arfil","negra")
           
        self.tablero[7][4] = self.piezas.pieza_a_notacion("rey","blanca")
        self.tablero[0][4] = self.piezas.pieza_a_notacion("rey","negra")
        self.tablero[7][3] = self.piezas.pieza_a_notacion("dama","blanca")
        self.tablero[0][3] = self.piezas.pieza_a_notacion("dama","negra")

    def actualizar_tablero(self):
        pass
    
    
                
class piezas():
    def __init__(self):
        self.letters = ['a','b','c','d','e','f','g','h']
        self.numbers = ['8','7','6','5','4','3','2','1']
        p_fig_blancas={"torre":"♖","caballo":"♘","arfil":"♗","rey":"♔","dama":"♕","peon":"♙"}
        p_fig_negras={"torre":"♜","caballo":"♞","arfil":"♝","rey":"♚","dama":"♛","peon":"♟"}
        self.p_blancas={"torre":"T","caballo":"C","arfil":"A","rey":"R","dama":"D","peon":"P"}
        self.p_negras={"torre":"t","caballo":"c","arfil":"a","rey":"r","dama":"d","peon":"p"}
        self.piezas={"blanca" : self.p_blancas, "negra" : self.p_negras}

    def pieza_a_notacion(self,pieza,color):
        return self.piezas[color][pieza]

    def notacion_a_pieza(self,p_not):
            blancas = list(self.p_blancas.keys())
            negras = list(self.p_negras.keys())
            for color_index, pB , pN  in zip(range(len(self.p_blancas)),self.p_blancas.values(),self.p_negras.values()) : 
                if pB==p_not :
                    return (blancas[color_index],"blanca")
                elif pN==p_not :
                    return (negras[color_index],"negra")
            return (None,None)
    
    def posibles_movimientos(self,t,p,pc,px,py,mx,my):
        posibles_mov = []
        conjunto_mov = []
        if(p=='torre'):
            come = 0
            if(px==mx):
                if(py>my): 
                    conjunto_mov = range(my,py)
                else :  
                    conjunto_mov = range(py,my)
                for H in conjunto_mov:
                    if((t[px][H] == 0) or (t[px][H] == 1) or (come==0)):
                        if(self.notacion_a_pieza(t[px][H])[1] != pc ):
                            come+=1
                        posibles_mov.append((px,H))
                    else:
                        break
            elif(py==my):
                if(px>mx): 
                    conjunto_mov = range(mx,px)
                else :  
                    conjunto_mov = range(px,mx)
                for V in conjunto_mov:
                    if((t[V][py] == '0') or (t[V][py] == '1') or (come==0)):
                        if(self.notacion_a_pieza(t[V][py])[1] != self.notacion_a_pieza(t[px][py])[1] ):
                            come+=1
                        posibles_mov.append((V,py))
                    else:
                        break
        if(p=='peon'):
            if(pc=='blanca'):
                if(px>mx and py==my):
                    if(px-mx==1):
                        posibles_mov.append((mx,my))
                    elif(px-mx==2 and px==6):
                        posibles_mov.append((mx,my))
            
            
        return posibles_mov

class player():
    def __init__(self):
        self.id = input("Id de jugador : ")
        self.t = tablero()
        print(self)
    
    def __str__(self):
        return str(self.t)
    
    def movimiento(self,py,px,my,mx):
        letters = ['a','b','c','d','e','f','g','h']
        numbers = ['8','7','6','5','4','3','2','1']
        py = letters.index(py)
        px = numbers.index(str(px))
        my = letters.index(my)
        mx = numbers.index(str(mx))
        print(self)
        p = self.t.piezas.notacion_a_pieza(self.t.tablero[px][py])
        posibles = self.t.piezas.posibles_movimientos(self.t.tablero,p[0],p[1],px,py,mx,my)
        print(posibles)

        if(len(posibles)==0):
            print('posicion no valida')
        else:
            self.t.tablero[mx][my] = self.t.tablero[px][py]
            self.t.tablero[px][py] = self.t.tablero_blank[px][py]
            print(self)

        return posibles



# PRUEBAS PLAYER

player1 = player()
print(player1.movimiento('a',1,'a',7))

# PRUEBAS TABLERO
#a = tablero()
#print(a)
#print(a.piezas.notacion_a_pieza('d'))
#print(a.piezas.posibles_mov('a',1))
