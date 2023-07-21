# importem les llibreries i programes necessaris per fer que funcioni el programa
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# connectar-se al servidor 
mc = minecraft.Minecraft.create()

#####################################################################
#                          ESCRIURE AL XAT                          #
#####################################################################

# escriurem al xat un missatge qualsevol
# ho farem amb .postToChat("missatge")
"""
    TO DO
"""


#####################################################################
#                        MOURE AL JUGADOR                           #
#####################################################################

# mourem el jugador a la posició x=-1, y=4, z=-1
# moure al jugador amb .setPos(id_jugador, [x,y,z])
"""
    TO DO
"""


#####################################################################
#                          POSAR UN BLOC                            #
#####################################################################

# posarem un bloc qualsevol a la posició x=-2, y=4, z=-2
# ho farem amb .setBlock([x,y,z], tipus_bloc)
"""
    TO DO
"""


#####################################################################
#           COMPROVAR SI EL JUGADOR ESTÀ DAMUNT DEL BLOC            #
#####################################################################

# comprovarem si el jugador es troba damunt d'un bloc determinat
# 1r -> agafar la posició actual del jugador amb .player.getTilePos()
# 2n -> agafar el tipus de bloc que es troba per sota del jugador amb .getBlock([x,y,z])
# 3r -> fer un bucle per anar comprovant si el jugador està damunt del bloc
#       la condició del bucle hauria de tenir en compte que mentre el jugador no estigui 
#       damunt del bloc ha d'anar mirant el bloc que es troba per sota del jugador
# (opcional) -> al sortir del bucle posar un missatge per saber que el jugador ha trepitjat el bloc
"""
    TO DO
"""


#####################################################################
#                        CONSTRUIR UNA CASA                         #
#####################################################################

# construïrem una casa de 7x6x7 (amplada, altura, llargària)
# ho farem amb .setBlocks([x1,y1,z1], [x2,y2,z2], tipus_bloc)
"""
    TO DO
"""

