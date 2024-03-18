import turtle
import numpy as np
import itertools as tl
from PIL import Image, ImageOps, EpsImagePlugin
import matplotlib.pyplot as plt
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.01.1\bin\gswin64c'


def drawline(tur, pos1, pos2):
    #tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])
    tur.penup()
    tur.goto(pos1[0], pos1[1])





def draw_X( height, n, line):
    turtle.clearscreen()
    
    def draw_single(tur, pos, d):
                
        drawline(tur, pos, [pos[0] - d/2, pos[1] - d/2])
        drawline(tur, pos, [pos[0] + d/2, pos[1] - d/2])
        drawline(tur, pos, [pos[0] + d/2, pos[1] + d/2])
        drawline(tur, pos, [pos[0] - d/2, pos[1] + d/2])





    def space_filling(n, height):
        
        if n == 0:
            return np.array([[0,0]])
        
           
        vert_final = np.array([[0,0]])
        
        for j in range(1,n):
        
            seeds = height*np.array([ 1/2**j + i*(1/2**(j-1)) for i in range(2**(j-1))])
        
            vertices = np.array(
                list(
                (tl.product(
                np.concatenate((seeds, -1*seeds)), repeat= 2))))
            
        
            vert_final = np.vstack((vert_final, vertices))
        
            
        # return vertices
        #print(vert_final)
        return vert_final


    vertices = space_filling(n,height/2)
    
    
    d = height / 2**n
    
    
    drawing_height = height
    
    screenset = turtle.Screen()
    screenset.tracer(0)
    screenset.setup(drawing_height, drawing_height)
    
    tur = turtle.RawTurtle(screenset)
    tur.color('black')
    tur.shape('classic')
    tur.hideturtle()
    tur.pensize(line)
    tur.color('black')
    tur.speed(9)

    
    tur.color('black')
    tur.pensize(line)
    
    
    
    
    for i in vertices:

        draw_single(tur, i, d)
        
        
    
    tur.color('black')
    
    h = height
    
    
    drawline(tur, [-h/2, -h/2], [h/2, h/2])
    drawline(tur, [-h/2, h/2], [h/2, -h/2])
    
    tur.pensize(4*line)
    drawline(tur, [-h/2, h/2], [-h/2, -h/2])
    drawline(tur, [-h/2, -h/2], [h/2, -h/2])
    drawline(tur, [h/2, -h/2], [h/2, h/2])
    drawline(tur, [h/2, h/2], [-h/2, h/2])
    

   
    turtle.update()
    
    ts = tur.getscreen()
    ts = ts.getcanvas()
   
    file_path =  'C:\\Users\\macko\\Desktop\\RAZER backup\\simulation_fractals\\structures_results\\testing2\\' + '_'.join(['SpacefillingRect',
        'depth', str(n),
        'line', str(int(line))]  ) + '.eps'
    
    
    ts.postscript(file = file_path ,height=1050, width=1050)   
    
    fitting_scale = np.poly1d([ 4.00359767e-04, -2.56985122e-02,  
                          3.30349021e+00,  1.07097546e+03])
    
    fitting_line = np.poly1d(([ 6.33137088e-04, -4.09441583e-02,
                              1.90074653e+00,  9.79140432e-01]))
    
    scale = 1000/fitting_scale(line)
    im = Image.open(file_path)
    im = im.resize((int(1500*scale),int(1500*scale)))
    im_gray = ImageOps.grayscale(im)
    im_gray.save(file_path[:-4] + '_real_px_line_' + str(int(np.round(fitting_line(line),0)))+'.bmp')
    
    turtle.clearscreen()
    
    
    
if __name__ == "__main__":

    #depths = [20]
    widths = np.arange(0,10,0.5)
    #widths = [0,1,2,3,4,5,6,7,8,9,10]
    
    
    drawing_height = 1048
    #drawing_width = 1050
    depths = [1,2,3,4,5,6]
    # widths = [1,2]
    
    for fractal_depth in depths:
        for line_width in widths:
            print(f'now drawing: depth: {fractal_depth},  {line_width}')
            draw_X( drawing_height, fractal_depth, line_width)

    


#%%


def space_filling(n, height):
    
    if n == 0:
        return np.array([[0,0]])
    
       
    vert_final = np.array([[0,0]])
    
    for j in range(1,n):
    
        seeds = height*np.array([ 1/2**j + i*(1/2**(j-1)) for i in range(2**(j-1))])
    
        vertices = np.array(
            list(
            (tl.product(
            np.concatenate((seeds, -1*seeds)), repeat= 2))))
        
    
        vert_final = np.vstack((vert_final, vertices))
    
        
    # return vertices
    #print(vert_final)
    return vert_final

      
 
 

















    
    
    
    
    
    
    
    
