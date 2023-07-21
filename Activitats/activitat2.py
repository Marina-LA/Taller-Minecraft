# importem les llibreries i programes necessaris per fer que funcioni el programa
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# connectar-se al servidor 
mc = minecraft.Minecraft.create()

#####################################################################
#                          EVENTS DE BLOC                           #
#####################################################################
# feu una funció que retorni el tipus de bloc que s'ha colpejat
# pista -> potser us serà útil utilitzar .getBlock()
"""
    TO DO
"""


#####################################################################
#                          EVENTS DE XAT                            #
#####################################################################
# feu una funció que retorni el missatge introduït pel xat del joc
"""
    TO DO
"""



#####################################################################
#                          QUIÉN ES QUIÉN                           #
#####################################################################
# programarem el joc de "Quién es quién" per poder jugar amb la màquina

# llista de blocs amb els quals jugarem
blocs =[block.ICE.id, block.WOOL.id, block.GOLD_ORE.id, \
        block.WOOD.id, block.DIRT.id, block.LEAVES.id, block.TNT.id, \
        block.BOOKSHELF.id, block.DIAMOND_ORE.id, block.MELON.id]

# llista de pistes per cada bloc
pista_bloc = {0:["blau"], \
              1:["blanc"], \
              2:["groc"], \
              3:["marro"], \
              4:["marro"], \
              5:["verd"], \
              6:["vermell", "blanc"], \
              7:["blau", "marro", "verd", "groc", "vermell", "blanc"], \
              8:["blau"], \
              9:["verd"]}

# fem que la màquina triï un bloc aleatòriament
bloc_maquina = random.randint(0, 9)

# col·loquem els blocs en el món
for i in range(10):
    pos_jugador = mc.player.getTilePos()
    mc.setBlock(pos_jugador.x+i, pos_jugador.y, pos_jugador.z, blocs[i])

# funció que comprovarà si el bloc que ha triat la màquina compleix amb el que hem dit
def comprovacio(missatge):
    # s'agafen les pistes per al bloc que ha triat la màquina
    llista_pistes = pista_bloc[bloc_maquina]

    # si el jugador no ha introduït cap missatge, no es fa la comprovació
    if missatge == None:
        return None
    
    # AFEGIU UN BUCLE FOR
    # aquest bucle ha de comprovar per a cada pista de la variable llista_pistes
    # si és igual o diferent a la variable missatge que es passa per paràmetre
    # si igual -> s'ha de dir pel xat "SI"
    # si NO igual -> s'ha de dir pel xat "NO"
    # (opcional) -> si el jugador introdueix pel xat "help" es poden mostrar els 
    # diferents colors que es poden escriure pel xat
    """
        TO DO
    """


# variable que controlarà el joc
start = True
mc.postToChat("Comencem el joc!")

# bucle principal del joc
while start:

    # obtenir el bloc amb la funció block_events() que hàgiu fet anteriorment
    """
        TO DO
    """


    # obtenir el missatge amb la funció chat_events() que hàgiu fet anteriorment
    """
        TO DO
    """


    # cridar al mètode comprovacio(missatge) per veure si la pista és certa o falsa
    """
        TO DO
    """


    # mirar si el jugador ha colpejat el bloc que ha triat la màquina
    """
            TO DO
    """


    time.sleep(1)

mc.postToChat("S'ha acabat el joc")
