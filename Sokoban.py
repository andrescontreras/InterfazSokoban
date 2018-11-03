import const
import time
class Board:
     ## ---------------------------------------------------------------------
    Data = [[]]
    Width = 0
    Height = 0
    playerpos = [0,0]
    cajas = 0

    ## ---------------------------------------------------------------------

    def __init__( self, arch ):
         print(const.CAJA)
         with open('Niveles/nivel3.txt') as f:
            lines = f.readlines()
            self.Width = int(lines[0])
            self.Height = int(lines[1])
            self.llenarMatriz(lines)    
         f.close()
         print("Width: ",self.Width)
         print("Height: ",self.Height)
         print("jugador: ", self.playerpos)
         #print("tabla")
         #print(self.Data)

    def llenarMatriz(self,lines):
        print("W: ",self.Width, "H: ",self.Height)

        self.Data = [ [ (0) for j in range(self.Height)] for i in range(self.Width) ]
        for i in range (2,self.Height+2):
            for j in range (0,self.Width):
                self.Data[i-2][j] = lines[i][j]
                if(self.Data[i-2][j] == const.JUGADOR or self.Data[i-2][j] == const.JUGADORM):
                    self.playerpos = [i-2,j]
                if (self.Data[i-2][j] == const.CAJA or self.Data[i-2][j] == const.CAJAM):
                    self.cajas = self.cajas + 1

    def mover (self,direccion):
        if (direccion=='A'):
            #W
			#Avanzar Arriba
            if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADOR):
                #Si la casilla actual es un jugador
                if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.LIBRE):
                    # Y la siguiente casilla es libre
                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                    self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                    self.playerpos[1] = self.playerpos[1] - 1
                    return self.Data
                else: 
                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.META):
                        # Y la siguiente casilla es meta
                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                        self.playerpos[1] = self.playerpos[1] - 1
                        return self.Data
                    else:
                        if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.CAJA):
                            #Y la siguiente es una caja
                            if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.LIBRE):
                                #Y la siguiente es un espacio libre
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                                self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJA
                                self.playerpos[1] = self.playerpos[1] - 1
                                return self.Data
                            else:
                                if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.META):
                                    #Y la siguiente es una meta
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJAM
                                    self.playerpos[1] = self.playerpos[1] - 1
                                    return self.Data
                                else:
                                    #No se puede mover
                                    return self.Data
                        else:
                            if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.CAJAM):
                                # Y la siguiente es una caja sobre meta
                                if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.LIBRE):
                                    #Y la siguiente es un espacio libre
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJA
                                    self.playerpos[1] = self.playerpos[1] - 1
                                    return self.Data
                                else:
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.META):
                                        #Y la siguiente es una meta
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJAM
                                        self.playerpos[1] = self.playerpos[1] - 1
                                        return self.Data
                                    else:
                                        #No se puede mover
                                        return self.Data
            else:###############################
                if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADORM):
                    #Si la casilla acutal es un jugador sobre la meta
                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.LIBRE):
                        # Y la siguiente casilla es libre
                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                        self.playerpos[1] = self.playerpos[1] - 1
                        return self.Data
                    else:
                        if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.META):
                            # Y la siguiente casilla es meta
                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                            self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                            self.playerpos[1] = self.playerpos[1] - 1
                            return self.Data
                        else:
                            if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.CAJA):
                                #Y la siguiente es una caja
                                if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.LIBRE):
                                    #Y la siguiente es un espacio libre
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                                    self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJA
                                    self.playerpos[1] = self.playerpos[1] - 1
                                    return self.Data
                                else:
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.META):
                                        #Y la siguiente es una meta
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADOR
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJAM
                                        self.playerpos[1] = self.playerpos[1] - 1
                                        return self.Data
                                    else:
                                        #No se puede mover
                                        return self.Data
                            else:
                                if (self.Data[self.playerpos[0]][self.playerpos[1] - 1] == const.CAJAM):
                                    # Y la siguiente es una caja sobre meta
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.LIBRE):
                                        #Y la siguiente es un espacio libre
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                                        self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJA
                                        self.playerpos[1] = self.playerpos[1] - 1
                                        return self.Data
                                    else:
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] - 2] == const.META):
                                            #Y la siguiente es una meta
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                            self.Data[self.playerpos[0]][self.playerpos[1] - 1] = const.JUGADORM
                                            self.Data[self.playerpos[0]][self.playerpos[1] - 2] = const.CAJAM
                                            self.playerpos[1] = self.playerpos[1] - 1
                                            return self.Data
                                        else:
                                            #No se puede mover
                                            return self.Data
        else:
            if (direccion=='W'):
                #A
                #Avanzar Izquierda
                if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADOR):
                    #Si la casilla actual es un jugador
                    if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.LIBRE):
                        # Y la siguiente casilla es libre
                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                        self.Data[self.playerpos[0]- 1 ][self.playerpos[1]] = const.JUGADOR
                        self.playerpos[0] = self.playerpos[0] - 1
                        return self.Data
                    else:
                        if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.META):
                            # Y la siguiente casilla es meta
                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                            self.playerpos[0] = self.playerpos[0] - 1
                            return self.Data
                        else:
                            if (self.Data[self.playerpos[0]- 1][self.playerpos[1]] == const.CAJA):
                                #Y la siguiente es una caja
                                if (self.Data[self.playerpos[0]- 2][self.playerpos[1]] == const.LIBRE):
                                    #Y la siguiente es un espacio libre
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                    self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                                    self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJA
                                    self.playerpos[0] = self.playerpos[0] - 1
                                    return self.Data
                                else:
                                    if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.META):
                                        #Y la siguiente es una meta
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                        self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                                        self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJAM
                                        self.playerpos[0] = self.playerpos[0] - 1
                                        return self.Data
                                    else:
                                        #No se puede mover
                                        return self.Data
                            else:
                                if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.CAJAM):
                                    # Y la siguiente es una caja sobre meta
                                    if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.LIBRE):
                                        #Y la siguiente es un espacio libre
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                        self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                        self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJA
                                        self.playerpos[0] = self.playerpos[0] - 1
                                        return self.Data
                                    else:
                                        if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.META):
                                            #Y la siguiente es una meta
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                            self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJAM
                                            self.playerpos[0] = self.playerpos[0] - 1
                                            return self.Data
                                        else:
                                            #No se puede mover
                                            return self.Data
                else:###############################
                    if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADORM):
                        #Si la casilla acutal es un jugador sobre la meta
                        if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.LIBRE):
                            # Y la siguiente casilla es libre
                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                            self.playerpos[0] = self.playerpos[0] - 1
                            return self.Data
                        else:
                            if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.META):
                                # Y la siguiente casilla es meta
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                self.playerpos[0] = self.playerpos[0] - 1
                                return self.Data
                            else:
                                if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.CAJA):
                                    #Y la siguiente es una caja
                                    if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.LIBRE):
                                        #Y la siguiente es un espacio libre
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                        self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                                        self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJA
                                        self.playerpos[0] = self.playerpos[0] - 1
                                        return self.Data
                                    else:
                                        if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.META):
                                            #Y la siguiente es una meta
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADOR
                                            self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJAM
                                            self.playerpos[0] = self.playerpos[0] - 1
                                            return self.Data
                                        else:
                                            #No se puede mover
                                            return self.Data
                                else:
                                    if (self.Data[self.playerpos[0] - 1][self.playerpos[1]] == const.CAJAM):
                                        # Y la siguiente es una caja sobre meta
                                        if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.LIBRE):
                                            #Y la siguiente es un espacio libre
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                            self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                            self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJA
                                            self.playerpos[0] = self.playerpos[0] - 1
                                            return self.Data
                                        else:
                                            if (self.Data[self.playerpos[0] - 2][self.playerpos[1]] == const.META):
                                                #Y la siguiente es una meta
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                self.Data[self.playerpos[0] - 1][self.playerpos[1]] = const.JUGADORM
                                                self.Data[self.playerpos[0] - 2][self.playerpos[1]] = const.CAJAM
                                                self.playerpos[0] = self.playerpos[0] - 1
                                                return self.Data
                                            else:
                                                #No se puede mover
                                                return self.Data
            else:
                if (direccion=='D'):
                    #S
					#Avanzar Abajo
                    if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADOR):
                        #Si la casilla actual es un jugador
                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.LIBRE):
                            # Y la siguiente casilla es libre
                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                            self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                            self.playerpos[1] = self.playerpos[1] + 1
                            return self.Data
                        else:
                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.META):
                                # Y la siguiente casilla es meta
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                self.playerpos[1] = self.playerpos[1] + 1
                                return self.Data
                            else:
                                if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.CAJA):
                                    #Y la siguiente es una caja
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.LIBRE):
                                        #Y la siguiente es un espacio libre
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                        self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                        self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJA
                                        self.playerpos[1] = self.playerpos[1] + 1
                                        return self.Data
                                    else:
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.META):
                                            #Y la siguiente es una meta
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJAM
                                            self.playerpos[1] = self.playerpos[1] + 1
                                            return self.Data
                                        else:
                                            #No se puede mover
                                            return self.Data
                                else:
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.CAJAM):
                                        # Y la siguiente es una caja sobre meta
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.LIBRE):
                                            #Y la siguiente es un espacio libre
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJA
                                            self.playerpos[1] = self.playerpos[1] + 1
                                            return self.Data
                                        else:
                                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.META):
                                                #Y la siguiente es una meta
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJAM
                                                self.playerpos[1] = self.playerpos[1] + 1
                                                return self.Data
                                            else:
                                                #No se puede mover
                                                return self.Data
                    else:###############################
                        if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADORM):
                            #Si la casilla acutal es un jugador sobre la meta
                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.LIBRE):
                                # Y la siguiente casilla es libre
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                self.playerpos[1] = self.playerpos[1] + 1
                                return self.Data
                            else: 
                                if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.META):
                                    # Y la siguiente casilla es meta
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                    self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                    self.playerpos[1] = self.playerpos[1] + 1
                                    return self.Data
                                else:
                                    if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.CAJA):
                                        #Y la siguiente es una caja
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.LIBRE):
                                            #Y la siguiente es un espacio libre
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                            self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJA
                                            self.playerpos[1] = self.playerpos[1] + 1
                                            return self.Data
                                        else:
                                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.META):
                                                #Y la siguiente es una meta
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADOR
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJAM
                                                self.playerpos[1] = self.playerpos[1] + 1
                                                return self.Data
                                            else:
                                                #No se puede mover
                                                return self.Data
                                    else:
                                        if (self.Data[self.playerpos[0]][self.playerpos[1] + 1] == const.CAJAM):
                                            # Y la siguiente es una caja sobre meta
                                            if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.LIBRE):
                                                #Y la siguiente es un espacio libre
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                                self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJA
                                                self.playerpos[1] = self.playerpos[1] + 1
                                                return self.Data
                                            else:
                                                if (self.Data[self.playerpos[0]][self.playerpos[1] + 2] == const.META):
                                                    #Y la siguiente es una meta
                                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                    self.Data[self.playerpos[0]][self.playerpos[1] + 1] = const.JUGADORM
                                                    self.Data[self.playerpos[0]][self.playerpos[1] + 2] = const.CAJAM
                                                    self.playerpos[1] = self.playerpos[1] + 1
                                                    return self.Data
                                                else:
                                                    #No se puede mover
                                                    return self.Data
                else:
                    if (direccion=='S'):
                        #D
						#Avanzar Derecha
                        if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADOR):
                            #Si la casilla actual es un jugador
                            if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.LIBRE):
                                # Y la siguiente casilla es libre
                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                self.Data[self.playerpos[0]+ 1 ][self.playerpos[1]] = const.JUGADOR
                                self.playerpos[0] = self.playerpos[0] + 1
                                return self.Data
                            else:
                                if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.META):
                                    # Y la siguiente casilla es meta
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                    self.playerpos[0] = self.playerpos[0] + 1
                                    return self.Data
                                else:
                                    if (self.Data[self.playerpos[0]+ 1][self.playerpos[1]] == const.CAJA):
                                        #Y la siguiente es una caja
                                        if (self.Data[self.playerpos[0]+ 2][self.playerpos[1]] == const.LIBRE):
                                            #Y la siguiente es un espacio libre
                                            self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                            self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                            self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJA
                                            self.playerpos[0] = self.playerpos[0] + 1
                                            return self.Data
                                        else:
                                            if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.META):
                                                #Y la siguiente es una meta
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                                self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                                self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJAM
                                                self.playerpos[0] = self.playerpos[0] + 1
                                                return self.Data
                                            else:
                                                #No se puede mover
                                                return self.Data
                                    else:
                                        if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.CAJAM):
                                            # Y la siguiente es una caja sobre meta
                                            if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.LIBRE):
                                                #Y la siguiente es un espacio libre
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                                self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                                self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJA
                                                self.playerpos[0] = self.playerpos[0] + 1
                                                return self.Data
                                            else:
                                                if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.META):
                                                    #Y la siguiente es una meta
                                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.LIBRE
                                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                                    self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJAM
                                                    self.playerpos[0] = self.playerpos[0] + 1
                                                    return self.Data
                                                else:
                                                    #No se puede mover
                                                    return self.Data
                        else:###############################
                            if (self.Data[self.playerpos[0]][self.playerpos[1]] == const.JUGADORM):
                                #Si la casilla acutal es un jugador sobre la meta
                                if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.LIBRE):
                                    # Y la siguiente casilla es libre
                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                    self.playerpos[0] = self.playerpos[0] + 1
                                    return self.Data
                                else:
                                    if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.META):
                                        # Y la siguiente casilla es meta
                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                        self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                        self.playerpos[0] = self.playerpos[0] + 1
                                        return self.Data
                                    else:
                                        if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.CAJA):
                                            #Y la siguiente es una caja
                                            if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.LIBRE):
                                                #Y la siguiente es un espacio libre
                                                self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                                self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJA
                                                self.playerpos[0] = self.playerpos[0] + 1
                                                return self.Data
                                            else:
                                                if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.META):
                                                    #Y la siguiente es una meta
                                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADOR
                                                    self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJAM
                                                    self.playerpos[0] = self.playerpos[0] + 1
                                                    return self.Data
                                                else:
                                                    #No se puede mover
                                                    return self.Data
                                        else:
                                            if (self.Data[self.playerpos[0] + 1][self.playerpos[1]] == const.CAJAM):
                                                # Y la siguiente es una caja sobre meta
                                                if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.LIBRE):
                                                    #Y la siguiente es un espacio libre
                                                    self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                    self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                                    self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJA
                                                    self.playerpos[0] = self.playerpos[0] + 1
                                                    return self.Data
                                                else:
                                                    if (self.Data[self.playerpos[0] + 2][self.playerpos[1]] == const.META):
                                                        #Y la siguiente es una meta
                                                        self.Data[self.playerpos[0]][self.playerpos[1]] = const.META
                                                        self.Data[self.playerpos[0] + 1][self.playerpos[1]] = const.JUGADORM
                                                        self.Data[self.playerpos[0] + 2][self.playerpos[1]] = const.CAJAM
                                                        self.playerpos[0] = self.playerpos[0] + 1
                                                        return self.Data
                                                    else:
                                                        #No se puede mover
                                                        return self.Data

    def movimientos (self,cadena):
        if len( cadena ) == 1:
            self.mover(cadena)
        else:
            for c in range (0, len( cadena ) ):
                self.mover(cadena[c])
                self.Print()
                time.sleep(0.2)
        return self.Data

    def cajabloqueada (self,posx,posy):
        conta = 0
        if (self.Data[posx - 1][posy] == const.MURO):
            conta = conta + 1
        if (self.Data[posx + 1][posy] == const.MURO):
            conta = conta + 1
        if (self.Data[posx][posy - 1] == const.MURO):
            conta = conta + 1
        if (self.Data[posx][posy + 1] == const.MURO):
            conta = conta + 1
        if conta >= 2:
            return True
        else:
            return False

    def estadodeljugador(self):
        cont = 0
        for filas in range (0, len(self.Data) - 1):
            for columnas in range (0, len(self.Data[0]) - 1 ):
                if self.Data[filas][columnas] == const.CAJAM:
                    cont = cont + 1
                if self.Data[filas][columnas] == const.CAJA:
                    return self.cajabloqueada(filas,columnas)
                
        if cont == self.cajas:
            return True
        else: 
            return False

    def Print (self):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.Data]))