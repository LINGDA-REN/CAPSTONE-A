import turtle  

t = turtle.Turtle()  

t.pencolor("blue")  
t.fillcolor("orange")  

def draw_petal():  
    t.begin_fill()  
    t.circle(100, 60) 
    t.left(120)          
    t.circle(100, 60)    
    t.left(120)          
    t.end_fill()  


def draw_flower():  
    for _ in range(6):    
        draw_petal()  
        t.left(60)        

t.speed(10)            
draw_flower()          

t.hideturtle()  
turtle.done() 