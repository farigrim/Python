#Importer une bibliotheque
import math 
##################################################################################### Calcul du theoreme de pythagore ############################################################################## 

                                                                                      # Dans le cas général #
A = int(input())  #la longueur A
B = int(input())   #la longueur B
borne_max = 9999999 #valeur max de calcul
borne_min = 0.0009   #valeur min de calcul

AC= A**2 #le carré de la longueur A
BC= B**2 #le carré de la longueur B
CC= AC+BC #la somme
C=math.sqrt(CC) #la racine / la valeur rechercher C 
print('la valeur rechercher "C" est égale a =',C)
 
#########################################################################################  Etude des differents cas ################################################################################

 ##### Saissir une variable en entrée str##### 



                                   ##### si A ou B et un str alors un message d'erreur doit s'afficher afin de changer de type#####

if (type(A)==str) or (type(B)==str):
    print("il est impossible d'effectuer le calcul avec un str ")
    print("VEUILLER SAISSIR UNE NOUVELLE VALEUR DE TYPE NUMERIQUE")
 elif (type(A)==str) or (type(B)==int): #### dans le cas ou seulement une des valeurs qui est un str 
        while ((type(A)==str) & (type(B)==int)): #### cas A est un str et B est un int 
           try:
             A = int(input()) # redire la valeur de A en int
           except ValueError:
            print("la valeur de A ne peut pas convertie en int")
             A = int(input())

 elif  (type(B)==str) or (type(A)==int): #### dans le cas ou seulement une des valeurs qui est un str 
  while ((type(B)==str) & (type(A)==int)): #### cas B est un str et A est un int 
           try:
             B = int(input()) # Convertire la valeur de B en int
           except ValueError:
            print("la valeur de A ne peut pas etre convertie en int")
             B = int(input())  
    

                                       ##### cas des nombre complexes#####      


if (type(a) == complex) and (type(B) == int):
     A = A.real #prendre que le coté réelle 

    elif (type(a) == int) and (type(B) == complex):
     B = B.real #prendre que le coté réelle 

    elif:
        A = A.real
        B = B.real
        return A,B

                                       ##### cas ou la valeur de A ou B est null ou negatif#####  


if (A =< O) or (B =< 0) :
      
        print("le calcule ne peut pas etre effectuer avec un nombre nul ou infferieur a zero")  
        print ("VEUILLEZ SAISSIR A NOUVEAU VOS VALEUR")   

                                       ##### cas ou les nombre sont trés grands#####

if (A> borne_max) and (B> borne_max)  :
      print("vous depassez la borne max de calcul")
      print("saissir de nouvelle valeur")
 
                                      ##### cas ou les nombre sont trop petit #####

if (A< borne_min) and (B< borne_min):
      print("vous etes inferieur au borne min de calcul")
      print("saissir de nouvelle valeur")


#################################################################################### fin #################################################################################