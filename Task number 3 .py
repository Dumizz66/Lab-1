SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"
color = [232,255,19]

def draw_ele(color,t):
    line = ' ' * t
    print(f"{SET_COLOR}{color}m{line}{END}", end = '')

def draw_img():  

 def tosi1_line():
     draw_ele(color[1], 5) ;  draw_ele(color[0], 3) ; draw_ele(color[1],47)
 
 
 
 
 
 

 
 def tosi2_line():
    draw_ele(color[1],8) ;  draw_ele(color[0],3) ;  draw_ele(color[1],44)
 

 
 def tosi3_line():
     draw_ele(color[1],11) ; draw_ele(color[0],3) ;  draw_ele(color[1],41)


 def tosi4_line():
     draw_ele(color[1],14) ; draw_ele(color[0],3) ;  draw_ele(color[1],38)
 
 
 
 def tosi5_line():
     draw_ele(color[1],17) ; draw_ele(color[0],3) ;  draw_ele(color[1],35)
     
 def tosi6_line():
     draw_ele(color[1],20) ; draw_ele(color[0],3) ;  draw_ele(color[1],32)

 def tosi7_line():
     draw_ele(color[1],23) ; draw_ele(color[0],6) ;  draw_ele(color[1],26)

 def tosi8_line():
     draw_ele(color[1],29) ; draw_ele(color[0],9) ;  draw_ele(color[1],17)

 def tosi9_line():
     draw_ele(color[1],38) ; draw_ele(color[0],12) ;  draw_ele(color[1],5)
     
 
 
 
     

 
 tosi1_line() ; print()
 tosi1_line() ; print()
 tosi1_line() ; print()
 tosi1_line() ; print()
 tosi2_line() ; print()
 tosi2_line() ; print()
 tosi2_line() ; print()
 tosi3_line() ; print()
 tosi3_line() ; print()
 tosi4_line() ; print()
 tosi5_line() ; print()
 tosi6_line() ; print()
 tosi7_line() ; print()
 tosi8_line() ; print()
 tosi9_line() ; print()
 

 

if __name__ == "__main__":
  for i in range(1):
    draw_img()