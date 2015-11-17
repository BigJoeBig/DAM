from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


#from Project import brikker

class Keyboard:
    #ID = 99
 
    def __init__(self, brikker):
        self.brikker = brikker
        self.selected_key = 0
        self.brikke = None


    def findBrikke(self):
#         for brikke in self.bikker:
#             if brikke.id == self.selected_key:
#                 self.brikke = brikke
#                 return
#           
        self.brikke = self.brikker[self.selected_key]
        
    def keydown(self, key, xx, yy):
        #print key
        #print xx
        if self.brikke == None:
            self.brikke = self.brikker[0]
         
        if key == 'w' :
            print self.brikker
            self.brikke.flyttOpp()  
        elif key == 's' :             
            self.brikke.flyttNed()       
        elif key == 'a' :             
            self.brikke.flyttV()       
        elif key == 'd' : 
            self.brikke.flyttH()     
        elif key == '1' :        
            self.brikke = self.brikker[0]

        elif key == '2' :   
            self.brikke = self.brikker[1]
        elif key == '3' :   
            self.brikke = self.brikker[2]
        elif key == '4' :   
            self.brikke = self.brikker[3]
        elif key == '5' :   
            self.brikke = self.brikker[4]            
            #b.printut()
       
       
#           b = self.brikker[self.ID] 
#         if key == 'w' :
#             self.brikker[self.ID].flyttOpp()  
#         elif key == 's' :             
#             b.flyttNed()       
#         elif key == 'a' :             
#             b.flyttV()       
#         elif key == 'd' : 
#             b.flyttH()     
#         elif key == '1' :        
#             
#             self.ID = 1
#             print self.ID
#             
#         elif key == '2' :        
#             self.ID = 2
#             print self.ID
#             #b.printut()
#        