import turtle
import numpy as np
from PIL import Image, ImageOps
from PIL import EpsImagePlugin
EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs10.01.1\bin\gswin64c'
#%%



          
def drawline(tur, pos1, pos2):
    #tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])
    tur.penup()
    tur.goto(pos1[0], pos1[1])


def cross_draw(tur, height, n, r):

    h=height
    
    steps = np.linspace(-h/2,h/2,n)
      
    if len(steps) % 2 == 0:
        pos = np.hstack((steps[1:int(len(steps)/2)], steps[1:int(len(steps)/2)][::-1])) - r
    
    if len(steps) % 2 == 1:
        pos = np.hstack((steps[1:int(len(steps)/2)], np.array(0), steps[1:int(len(steps)/2)][::-1])) - r
    

    # if len(steps) % 2 == 0:
    #     res_gora = pos[1:] + pos[:0:-1]
        
    # if len(steps) % 2 == 1:
    #     res_gora = pos[:-1] + pos[::-1]


    
    for i,st in enumerate(steps[1:-1]):
        
                
        drawline(tur, [st, -height / 2], [st, max(-h/2, pos[i])])
        
        drawline(tur, [st, height / 2], [st, min(h/2, -pos[i])])
        
        drawline(tur, [-height / 2, st], [max(-h/2, pos[i]), st])
        
        drawline(tur, [height / 2, st], [min(h/2, -pos[i]), st])
        
        
    tur.penup()
    turtle.update()

       

def draw(line_width, drawing_height, fractal_depth, circle):
        
    screenset = turtle.Screen()
    screenset.tracer(0)
    screenset.setup(drawing_height, drawing_height)
    
    artistpen = turtle.RawTurtle(screenset)
    artistpen.shape('classic')
    artistpen.hideturtle()
    artistpen.pensize(line_width)
    artistpen.color('black')
    artistpen.speed('fastest')


    margin = 0.5* line_width
    dr = drawing_width - margin
       
    cross_draw(artistpen, dr, fractal_depth,circle)
    
    drawline(artistpen,[-dr/2, -dr/2],[-dr/2, dr/2])
    drawline(artistpen,[-dr/2, dr/2],[dr/2, dr/2])
    drawline(artistpen,[dr/2, dr/2],[dr/2, -dr/2])
    drawline(artistpen,[dr/2, -dr/2],[-dr/2, -dr/2])
    
    
    turtle.update()
    ts = artistpen.getscreen()
    ts= ts.getcanvas()
   
    file_path =  'C:\\Users\\macko\\Desktop\\RAZER backup\\simulation_fractals\\structures_results\\testing3\\' + '_'.join(['CrossMod',
        'depth', str(fractal_depth),
        'radius', str(int(np.round(circle,2)))]  ) + '.eps'
    
    #file_tmp = 'C:\\Users\\macko\\Desktop\\RAZER backup\\simulation_fractals\\2023_testing\\tmp.eps'
    
    
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
    
    # depth = np.arange(11,16,1)
    # lines = [0.1,0.5,1,1.5,2,3,4,5]
    # circles = [0,10,20,30,40,50,60,70,80,90,100,120,140,150,160]
    
    
    depth = np.arange(2, 11, 1)
    lines = np.arange(5.5,10.5,0.5)
    circles = [0]
    
    
    drawing_width = 1048#1048
    drawing_height = 1048#1048
    
    count = 0
    str_number = len(depth)*len(lines)*len(circles)


    for line in lines:
        # for rad in circles:
        for dep_ in depth:
            print(f"now drawing: line: {line}, radius: {0}, depth: {dep_}, progress: {np.round(count/str_number,2)*100} %, ({count} / {str_number} )")
            draw(line,drawing_height, dep_ ,0)
            count += 1
                

#%%

h=1000
r = 40
n = 8


### dol

steps = np.linspace(-h/2,h/2,n)

# -500 -> 0 - 3x40 = - 120 (-3r)
# - 250 -> 0 - 2x40 = - 80 (-2r) 
# 0 -> 0 - 1x40 = -40 (-1r)
# 250 -> 0 - 2x40 = -80 (-2r)
# 500 -> 0 - 3x40 = -120 (-3r)

step_no = int(len(steps) / 2 + 1)


pos = [i*r for i in np.arange(-step_no,0,1)]


if len(steps) % 2 == 0:
    res = pos[1:] + pos[:0:-1]
    
if len(steps) % 2 == 1:
    res = pos[:-1] + pos[::-1]

print('dol ',res)


### gora

pos = [h/2 - i*r for i in np.arange(1,step_no+1,1)]
if len(steps) % 2 == 0:
    res = pos[1:] + pos[:0:-1]
    
if len(steps) % 2 == 1:
    res = pos[:-1] + pos[::-1]
    
print('gora', res)

### lewo


    
# h=height
# r = 0
# ss = height / n # steps = np.linspace(-h/2,h/2,n+1)


# steps = np.linspace(-h/2,h/2,n)


# step_no = int(len(steps) / 2 + 1)


# pos = [i*ss - r for i in np.arange(-step_no,0,1)]


# if len(steps) % 2 == 0:
#     res_dol = pos[1:] + pos[:0:-1]
    
# if len(steps) % 2 == 1:
#     res_dol = pos[:-1] + pos[::-1]

# print('dol ', res_dol)





  
        
        
 