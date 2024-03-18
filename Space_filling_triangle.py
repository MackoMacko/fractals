import turtle
import numpy as np
import itertools as tl
from PIL import Image, ImageOps, EpsImagePlugin

EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.01.1\bin\gswin64c'


def drawline(tur, pos1, pos2):
    #tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])
    tur.penup()
    tur.goto(pos1[0], pos1[1])




   

#%%
def triangle_span(line_width, n, height):
    
    turtle.clearscreen()
    screenset = turtle.Screen()
    screenset.tracer(0)
    screenset.setup(np.sqrt(3)*drawing_height/2, drawing_height)
    
    tur = turtle.RawTurtle(screenset)
    tur.color(pen_color)
    tur.shape('classic')
    #tur.hideturtle()
    
    tur.color('black')
    tur.speed('fastest')
    tur.pensize(line_width)
     
    drawing_width = drawing_height
    
    def drawline(tur, pos1, pos2):
        #tracing the algorithm.
        tur.penup()
        tur.goto(pos1[0], pos1[1])
        tur.pendown()
        tur.goto(pos2[0], pos2[1])
        tur.penup()
        tur.goto(pos1[0], pos1[1])
    
    
    def draw_single(tur, up, pos, height):
        
        tur.penup()
        tur.goto(pos)
        tur.pendown()

        if up == 1:
            tur.setheading(90) #setting the head to north
            
        if up == -1:
            tur.setheading(270) #setting the head to south
        
        tur.forward(height)
        tur.backward(height)
        
        tur.right(120)
        tur.forward(height)
        tur.backward(height)
        
        tur.right(120)
        tur.forward(height)
        tur.backward(height)
        
    
    
    def draw_triangle(tur, direction, pos, height):
        
        d = direction
        
        draw_single(tur, -d, pos, height/2)
        draw_single(tur, d, (pos[0], pos[1] + d*height), height/2)
        draw_single(tur, d, (pos[0] - d*height*np.sqrt(3)/2, pos[1] - d*height/2), height/2)
        draw_single(tur, d, (pos[0] + d*height*np.sqrt(3)/2, pos[1] - d*height/2), height/2)
        draw_single(tur, d, (pos[0], pos[1]), height)

       
        
    def space_filling(n, height):
        height = height / 2**(n-1)
        
        vertices = {(0,0)}


        for i in range(n+10):
            vertices_copy = vertices.copy()
            vertices = set()
            h = 2*height
            for vert in vertices_copy:

                vertices.add((vert[0], vert[1]+h))
                vertices.add((vert[0] - h*np.sqrt(3)/2, vert[1] - h/2))
                vertices.add((vert[0] + h*np.sqrt(3)/2, vert[1] - h/2))
    
        
        for vert in vertices:
        
            drawline(tur, vert, (vert[0] - height*np.sqrt(3), vert[1] - height))    
            drawline(tur, vert, (vert[0] + height*np.sqrt(3), vert[1] - height)) 
            drawline(tur, vert, (vert[0],vert[1]+2*height))
            
            
            draw_triangle(tur, -1, vert, height)
            
            draw_triangle(tur, 1, (vert[0] - height*np.sqrt(3), vert[1] - height), height)
            
            draw_triangle(tur, 1, (vert[0] + height*np.sqrt(3), vert[1] - height), height)
            
            draw_triangle(tur, 1, (vert[0],vert[1]+2*height), height)
            
            
        #drawline(tur,(0,0), (0, - drawing_height/2))
            
       

        return 1
           
    
    tur.left(90)
    
    space_filling(n, height/2)



    corners = {'LT': (-np.sqrt(3)*height/4, height/2),
               'RT': (np.sqrt(3)*height/4, height/2),
               'LD': (-np.sqrt(3)*height/4, -height/2),
               'RD': (np.sqrt(3)*height/4, -height/2) }
    
    
    vertices =  [(0,height/2),
                (np.sqrt(3)*height/4,height/4),
                (np.sqrt(3)*height/4,-height/4),
                (0,-height/2),
                (-np.sqrt(3)*height/4,-height/4),
                (-np.sqrt(3)*height/4,height/4),
                (0,height/2)]


    ##whitening the outer left border:
    tur.fillcolor('white')
    tur.color('white')
    tur.penup()
    tur.goto(corners['LT'])
    tur.begin_fill()
    tur.color('white')
    drawline(tur,corners['LT'], corners['LD'])
    drawline(tur,corners['LD'], [-drawing_height/2, - drawing_width/2]) 
    drawline(tur,[-drawing_height/2, - drawing_width/2], [-drawing_height/2, drawing_width/2])   
    drawline(tur, [-drawing_height/2, drawing_width/2], corners['LT'])        
    tur.end_fill()
    
    ###whitening the outer rigth border:
    tur.penup()
    tur.goto(corners['RT'])
    tur.begin_fill()
    drawline(tur,corners['RT'], corners['RD'])
    drawline(tur,corners['RD'], [drawing_height/2, - drawing_width/2]) 
    drawline(tur,[drawing_height/2, - drawing_width/2], [drawing_height/2, drawing_width/2])   
    drawline(tur, [drawing_height/2, drawing_width/2], corners['RT'])        
    tur.end_fill()
    
        
    
    #triangle lines drawing
    tur.color('black')
    tur.fillcolor('black')
    tur.penup()
    tur.goto(vertices[5][0],vertices[5][1])

    tur.begin_fill()
    drawline(tur,vertices[5], corners['LT'])
    drawline(tur,corners['LT'], vertices[0]) 
    drawline(tur,vertices[0], vertices[5])        
    tur.end_fill()
    
    
    tur.penup()
    tur.goto(vertices[0][0],vertices[0][1])
    tur.begin_fill()
    drawline(tur,vertices[0], corners['RT'])
    drawline(tur,corners['RT'], vertices[1]) 
    drawline(tur,vertices[1], vertices[0])        
    tur.end_fill()
    
    
    tur.penup()
    tur.goto(vertices[4][0],vertices[4][1])
    tur.begin_fill()
    drawline(tur,vertices[4], corners['LD'])
    drawline(tur,corners['LD'], vertices[3]) 
    drawline(tur,vertices[3], vertices[4])        
    tur.end_fill()
    
    
    tur.penup()
    tur.goto(vertices[2][0],vertices[2][1])
    tur.begin_fill()
    drawline(tur,vertices[2], corners['RD'])
    drawline(tur,corners['RD'], vertices[3]) 
    drawline(tur,vertices[3], vertices[2])        
    tur.end_fill()
    
    
    #filling up and down lines for sure:
    
    tur.penup()
    drawline(tur,corners['LT'], corners['LD'])
    drawline(tur,corners['RT'], corners['RD'])
 
    turtle.update()     
    
    
    ts = tur.getscreen()
    ts = ts.getcanvas()
   
    file_path =  'C:\\Users\\macko\\Desktop\\RAZER backup\\simulation_fractals\\structures_results\\space-spanning-triangle\\' + '_'.join(['Hexagonal_spanning',
        'depth', str(fractal_depth),
        'line', str(line_width)]  ) + '.eps'
    
    
    ts.postscript(file = file_path ,height=1050, width=1050*np.sqrt(3)/2)   
    
    fitting_scale = np.poly1d([ 4.00359767e-04, -2.56985122e-02,  
                          3.30349021e+00,  1.07097546e+03])
    
    fitting_line = np.poly1d(([ 6.33137088e-04, -4.09441583e-02,
                              1.90074653e+00,  9.79140432e-01]))
    
    scale = 1000/fitting_scale(line_width)
    im = Image.open(file_path)
    im = im.resize((int(1500*scale*np.sqrt(3)/2),int(1500*scale)))
    im_gray = ImageOps.grayscale(im)
    im_gray.save(file_path[:-4] + '_line_' + str(np.round(fitting_line(line_width),0))+'.bmp')
    
    turtle.clearscreen()
    



if __name__ == "__main__":
    
    bg_color = "white"
    pen_color = "black"
    
    drawing_height = 1048
    fractal_depth = 5
    line_width = 1
    
    
    
    
    widths = [0,0.5,1,1.5,2,3,4,5,6,7,8,9,10,12,14,16,18]
    
    #widths = [1]
    
    for line_width in widths:
    
        
        triangle_span(line_width, fractal_depth, drawing_height)
    

    

        
    
    
  #%%    
def Hexagon_Fract(height, line, hex_length):
    
    
    screenset = turtle.Screen()
    screenset.tracer(0)
    screenset.setup(drawing_width, drawing_height)
    
    tur = turtle.RawTurtle(screenset)
    tur.color(pen_color)
    tur.shape('classic')
    tur.hideturtle()
    tur.pensize(line_width)
    tur.color('black')
    tur.speed(9)
    
       
    hex_in_row = height / hex_length
    
    pos_x = np.arange(-(hex_in_row), (hex_in_row),1)
    
    
    Hexagon(tur, drawing_width, [0,0],line)
    
    for i in pos_x:
        for j in pos_x:       
            Hexagon(tur, hex_length, [(np.sqrt(3)/2)*hex_length*j + (hex_length*(np.sqrt(3)/4))*i, hex_length*(0.75)*i], line)
  
    
    corners = {'LT': (-np.sqrt(3)*height/4, height/2), 'RT': (np.sqrt(3)*height/4, height/2),
               'LD': (-np.sqrt(3)*height/4, -height/2), 'RD': (np.sqrt(3)*height/4, -height/2) }
    
    vertices =  [(0,height/2),
                (np.sqrt(3)*height/4,height/4),
                (np.sqrt(3)*height/4,-height/4),
                (0,-height/2),
                (-np.sqrt(3)*height/4,-height/4),
                (-np.sqrt(3)*height/4,height/4),
                (0,height/2)]
    
    
    
    
    ##whitening the outer left border:
    tur.fillcolor('white')
    tur.color('white')
    tur.penup()
    tur.goto(corners['LT'])
    tur.begin_fill()
    tur.color('white')
    drawline(tur,corners['LT'], corners['LD'])
    drawline(tur,corners['LD'], [-drawing_height/2, - drawing_width/2]) 
    drawline(tur,[-drawing_height/2, - drawing_width/2], [-drawing_height/2, drawing_width/2])   
    drawline(tur, [-drawing_height/2, drawing_width/2], corners['LT'])        
    tur.end_fill()
    
    ###whitening the outer rigth border:
    tur.penup()
    tur.goto(corners['RT'])
    tur.begin_fill()
    drawline(tur,corners['RT'], corners['RD'])
    drawline(tur,corners['RD'], [drawing_height/2, - drawing_width/2]) 
    drawline(tur,[drawing_height/2, - drawing_width/2], [drawing_height/2, drawing_width/2])   
    drawline(tur, [drawing_height/2, drawing_width/2], corners['RT'])        
    tur.end_fill()
    
        
    
    #lines drawing
    tur.color('black')
    tur.fillcolor('black')
    tur.penup()
    tur.goto(vertices[5][0],vertices[5][1])

    tur.begin_fill()
    drawline(tur,vertices[5], corners['LT'])
    drawline(tur,corners['LT'], vertices[0]) 
    drawline(tur,vertices[0], vertices[5])        
    tur.end_fill()
    
    
    tur.penup()
    tur.goto(vertices[0][0],vertices[0][1])
    tur.begin_fill()
    drawline(tur,vertices[0], corners['RT'])
    drawline(tur,corners['RT'], vertices[1]) 
    drawline(tur,vertices[1], vertices[0])        
    tur.end_fill()
    
    
    tur.penup()
    tur.goto(vertices[4][0],vertices[4][1])
    tur.begin_fill()
    drawline(tur,vertices[4], corners['LD'])
    drawline(tur,corners['LD'], vertices[3]) 
    drawline(tur,vertices[3], vertices[4])        
    tur.end_fill()
    
    
    tur.penup()
    tur.goto(vertices[2][0],vertices[2][1])
    tur.begin_fill()
    drawline(tur,vertices[2], corners['RD'])
    drawline(tur,corners['RD'], vertices[3]) 
    drawline(tur,vertices[3], vertices[2])        
    tur.end_fill()
    

    
    
    
    
    
    tur.penup()
    drawline(tur,corners['LT'], corners['LD'])
    drawline(tur,corners['RT'], corners['RD'])
 
    turtle.update()
    
    ts = tur.getscreen()
    ts = ts.getcanvas()
   
    file_path =  'C:\\Users\\macko\\Desktop\\RAZER backup\\simulation_fractals\\structures_results\\hex-hex-grid\\' + '_'.join(['Hexagonal',
        'hex_size', str(fractal_depth),
        'line', str(line_width)]  ) + '.eps'
    
    
    ts.postscript(file = file_path ,height=1050, width=1050)   
    
    fitting_scale = np.poly1d([ 4.00359767e-04, -2.56985122e-02,  
                          3.30349021e+00,  1.07097546e+03])
    
    fitting_line = np.poly1d(([ 6.33137088e-04, -4.09441583e-02,
                              1.90074653e+00,  9.79140432e-01]))
    
    scale = 1000/fitting_scale(line_width)
    im = Image.open(file_path)
    im = im.resize((int(1500*scale),int(1500*scale)))
    im_gray = ImageOps.grayscale(im)
    im_gray.save(file_path[:-4] + '_line_' + str(np.round(fitting_line(line_width),0))+'.bmp')
    
    turtle.clearscreen()
    

if __name__ == "__main__":

    depths = [20]
    widths = np.arange(0,5,0.5)
    
    # depths = [100,200,300]
    # widths = [1,2]
    
    for fractal_depth in depths:
        for line_width in widths:
            print(f'now drawing: {fractal_depth},  {line_width}')
            Hexagon_Fract(drawing_height, line_width, fractal_depth)
    
    
    
    
    
    
    
    
    
    
    
