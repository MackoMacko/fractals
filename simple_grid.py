
#%%
import turtle
import numpy as np
from PIL import Image, ImageOps


from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.01.1\bin\gswin64c'


speed = 8
bg_color = "white"
pen_color = "black"
screen_width = 1250
screen_height = 1250
        
    
def drawline(tur, pos1, pos2):
    #tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])
    tur.penup()
    tur.goto(pos1[0], pos1[1])


def cross_draw(tur, height, n):
#        div_step = 2*(n+1)
#        steps = np.arange(-height/div_step,
#                          -height/2,-height/div_step)
    h=height
    #steps = np.arange(h/2-h/(2*n+1),-h/2,-h/(2*n+1))
    steps = np.linspace(-h/2,h/2,n+1)
    print(steps)
    for i,st in enumerate(steps):
        drawline(tur, [st, h / 2], [-h / 2, -st])
        drawline(tur, [st,-h / 2], [h / 2, - st])
#        drawline(tur, [-st, -height / 2], [st, height / 2])

    # for i,st in enumerate(steps):
    #     drawline(tur, [-height / 2, st ], [ height / 2, st])
    

def draw(line_width, drawing_width, drawing_height, fractal_depth):
        
    screenset = turtle.Screen()
    screenset.tracer(0)
    screenset.setup(drawing_width, drawing_height)
    
    artistpen = turtle.RawTurtle(screenset)
    artistpen.color(pen_color)
    artistpen.shape('classic')
    artistpen.hideturtle()
    artistpen.pensize(line_width)
    artistpen.color('black')
    artistpen.speed(9)


    margin = 0.5*line_width
    dr = drawing_width - margin
       
    cross_draw(artistpen, dr, fractal_depth)
    
    drawline(artistpen,[-dr/2, -dr/2],[-dr/2, dr/2])
    drawline(artistpen,[-dr/2, dr/2],[dr/2, dr/2])
    drawline(artistpen,[dr/2, dr/2],[dr/2, -dr/2])
    drawline(artistpen,[dr/2, -dr/2],[-dr/2, -dr/2])
    
    
    turtle.update()
    ts = artistpen.getscreen()
    ts= ts.getcanvas()
   
    file_path =  'C:\\Users\\macko\\Desktop\\RAZER backup\\simulation_fractals\\structures_results\\testing2\\' + '_'.join(['rectLine',
        'depth', str(fractal_depth)]  ) + '.eps'
    
    #file_tmp = 'C:\\Users\\macko\\Desktop\\RAZER backup\\simulation_fractals\\2023_testing\\tmp.eps'
    #rectGrid_depth_7_line_1
    
    ts.postscript(file = file_path ,height=1050, width=1050)   
    
    fitting_scale = np.poly1d([ 4.00359767e-04, -2.56985122e-02,  
                          3.30349021e+00,  1.07097546e+03])
    
    fitting_line = np.poly1d(([ 6.33137088e-04, -4.09441583e-02,
                              1.90074653e+00,  9.79140432e-01]))
    
    scale = 1000/fitting_scale(line_width)
    im = Image.open(file_path)
    im = im.resize((int(1500*scale),int(1500*scale)))
    im_gray = ImageOps.grayscale(im)
    im_gray.save(file_path[:-4] + '_line_' + str(int(np.round(fitting_line(line_width),0)))+'.bmp')
    
    turtle.clearscreen()

if __name__ == "__main__":
    
    depth = np.arange(2,31,1)
    lines = np.arange(0.01,10,0.5)
    #lines = [0,1,2,3]
    # circles = [0,10,20,30,40,50,60,70,80,90,100]
    
    
    drawing_width = 1048
    drawing_height = 1048
    
    for d in depth:
        for line in lines:
            print(f'drawing: {d}, {line}')
            draw(line,drawing_width,drawing_height,d)
                


  
        
        
 