import pygame
import numpy as np
import sys
import math

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Transformation Visualizer")

clock = pygame.time.Clock()

# COLORS
NEON_BLUE = (0,255,255)
DARK_BG = (5,10,20)
GRID_COLOR = (0,80,100)

font = pygame.font.SysFont("consolas", 16)

projection_demo = False

shear_on = False
show_eigen = False
show_pca = False
show_live_eigen = False

# ------------------ SHAPES ------------------

def cube():
    v=[[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],
       [-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]]
    e=[(0,1),(1,2),(2,3),(3,0),
       (4,5),(5,6),(6,7),(7,4),
       (0,4),(1,5),(2,6),(3,7)]
    return np.array(v),e

def pyramid():
    v=[[0,1,0],[-1,-1,-1],[1,-1,-1],[1,-1,1],[-1,-1,1]]
    e=[(0,1),(0,2),(0,3),(0,4),
       (1,2),(2,3),(3,4),(4,1)]
    return np.array(v),e

def tetra():
    v=[[1,1,1],[-1,-1,1],[-1,1,-1],[1,-1,-1]]
    e=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    return np.array(v),e

def octa():
    v=[[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
    e=[(0,2),(0,3),(0,4),(0,5),
       (1,2),(1,3),(1,4),(1,5),
       (2,4),(2,5),(3,4),(3,5)]
    return np.array(v),e

def prism():
    v=[[-2,-1,-1],[2,-1,-1],[2,1,-1],[-2,1,-1],
       [-2,-1,1],[2,-1,1],[2,1,1],[-2,1,1]]
    e=[(0,1),(1,2),(2,3),(3,0),
       (4,5),(5,6),(6,7),(7,4),
       (0,4),(1,5),(2,6),(3,7)]
    return np.array(v),e

def tri_prism():
    return pyramid()

def pent_prism():
    v=[]; e=[]
    for i in range(5):
        a=2*math.pi*i/5
        v.append([math.cos(a),math.sin(a),-1])
    for i in range(5):
        a=2*math.pi*i/5
        v.append([math.cos(a),math.sin(a),1])
    for i in range(5):
        e.append((i,(i+1)%5))
        e.append((i+5,(i+1)%5+5))
        e.append((i,i+5))
    return np.array(v),e

def cylinder():
    v=[]; e=[]
    for i in range(0,360,30):
        a=math.radians(i)
        v.append([math.cos(a),math.sin(a),-1])
        v.append([math.cos(a),math.sin(a),1])
    n=len(v)
    for i in range(0,n,2):
        e.append((i,(i+2)%n))
        e.append((i+1,(i+3)%n))
        e.append((i,i+1))
    return np.array(v),e

def cone():
    v=[[0,0,1]]; e=[]
    for i in range(0,360,30):
        a=math.radians(i)
        v.append([math.cos(a),math.sin(a),-1])
    for i in range(1,len(v)):
        e.append((0,i))
    return np.array(v),e

def sphere():
    v=[]
    for i in range(0,180,30):
        for j in range(0,360,30):
            v.append([
                math.sin(math.radians(i))*math.cos(math.radians(j)),
                math.sin(math.radians(i))*math.sin(math.radians(j)),
                math.cos(math.radians(i))
            ])
    v=np.array(v)
    e=[(i,i+1) for i in range(len(v)-1)]
    return v,e

shape_map={
    "cube":cube,"pyramid":pyramid,"tetra":tetra,
    "octa":octa,"prism":prism,"tri_prism":tri_prism,
    "sphere":sphere,"cylinder":cylinder,
    "cone":cone,"pent_prism":pent_prism
}

shape_names=list(shape_map.keys())

active_shape="cube"
vertices,edges=shape_map[active_shape]()

# ------------------ TRANSFORM ------------------

angle_x=angle_y=angle_z=0
scale=1
tx, ty, tz = 0,0,0

def rotX(p,a): return np.dot(p,[[1,0,0],[0,math.cos(a),-math.sin(a)],[0,math.sin(a),math.cos(a)]])
def rotY(p,a): return np.dot(p,[[math.cos(a),0,math.sin(a)],[0,1,0],[-math.sin(a),0,math.cos(a)]])
def rotZ(p,a): return np.dot(p,[[math.cos(a),-math.sin(a),0],[math.sin(a),math.cos(a),0],[0,0,1]])

def shear(p, k=0.5):
    return np.dot(p, [[1,k,0],[0,1,0],[0,0,1]])

# ------------------ PROJECTION ------------------

def project_perspective(points, offset_x):
    out=[]
    for x,y,z in points:
        f=200/(z+5)
        out.append((int(x*f+offset_x), int(-y*f+350)))
    return out

def project_orthographic(points, offset_x):
    out=[]
    for x,y,z in points:
        out.append((int(x*100+offset_x), int(-y*100+350)))
    return out

# ------------------ EIGEN & PCA (UNCHANGED) ------------------

def draw_eigen(offset_x):
    M = np.array([[1.2,0.5,0],[0,1,0],[0,0,1]])
    vals, vecs = np.linalg.eig(M)
    origin = np.array([[0,0,0]]) + np.array([tx,ty,tz])
    o = project_perspective(origin, offset_x)[0]

    colors = [(255,0,0), (0,255,0), (255,255,0)]

    for i in range(3):
        v = vecs[:,i]*2
        pt = project_perspective(np.array([v]), offset_x)[0]
        pygame.draw.line(screen, colors[i], o, pt, 3)
        text = font.render(f"λ{i+1}={round(vals[i],2)}", True, colors[i])
        screen.blit(text, (pt[0]+10, pt[1]+10))

def draw_live_eigen(offset_x):
    T = get_transformation_matrix()
    vals, vecs = np.linalg.eig(T)
    origin = np.array([[0,0,0]]) + np.array([tx,ty,tz])
    o = project_perspective(origin, offset_x)[0]

    colors = [(255,0,0), (0,255,0), (255,255,0)]

    for i in range(3):
        v = vecs[:,i].real * 2
        pt = project_perspective(np.array([v]), offset_x)[0]
        pygame.draw.line(screen, colors[i], o, pt, 3)
        text = font.render(f"λ{i+1}={round(vals[i].real,2)}", True, colors[i])
        screen.blit(text, (pt[0]+10, pt[1]+10))

def draw_pca(points, offset_x):
    mean = np.mean(points, axis=0)
    centered = points - mean
    cov = np.cov(centered.T)
    vals, vecs = np.linalg.eig(cov)

    origin = project_perspective(np.array([mean]), offset_x)[0]

    # Draw principal components (same as before)
    for i in range(2):
        v = vecs[:, i] * 3
        p = mean + v
        p2 = project_perspective(np.array([p]), offset_x)[0]
        pygame.draw.line(screen, (255,100,200), origin, p2, 3)

    # ------------------ NEW UI DISPLAY ------------------

    # Title
    screen.blit(font.render("PCA (Principal Components)", True, (255,100,200)), (250, 20))

    # Covariance matrix
    y_offset = 45
    screen.blit(font.render("Covariance Matrix:", True, (200,200,200)), (250, y_offset))

    for i in range(3):
        row_text = f"[ {round(cov[i][0],2)}  {round(cov[i][1],2)}  {round(cov[i][2],2)} ]"
        screen.blit(font.render(row_text, True, (180,180,180)), (250, y_offset + 20 + i*20))

    # Eigenvalues (variance)
    screen.blit(font.render("Eigenvalues:", True, (200,200,200)), (250, y_offset + 90))

    for i in range(3):
        val_text = f"λ{i+1} = {round(vals[i].real,2)}"
        screen.blit(font.render(val_text, True, (255,180,100)), (250, y_offset + 110 + i*20))

# ------------------ AXES ------------------

def draw_axes(offset_x):
    axis_len=3*scale
    axes=np.array([[0,0,0],[axis_len,0,0],[0,axis_len,0],[0,0,axis_len]])

    axes=rotX(axes,angle_x)
    axes=rotY(axes,angle_y)
    axes=rotZ(axes,angle_z)
    axes+=np.array([tx,ty,tz])

    ax=project_perspective(axes,offset_x)

    pygame.draw.line(screen,(255,0,0),ax[0],ax[1],3)   # X - red
    pygame.draw.line(screen,(0,255,0),ax[0],ax[2],3)   # Y - green
    pygame.draw.line(screen,(0,150,255),ax[0],ax[3],3) # Z - blue

    pygame.draw.circle(screen,(255,255,255),ax[0],4)

    # LABELS 🔥
    screen.blit(font.render("X",True,(255,0,0)),(ax[1][0]+5,ax[1][1]))
    screen.blit(font.render("Y",True,(0,255,0)),(ax[2][0]+5,ax[2][1]))
    screen.blit(font.render("Z",True,(0,150,255)),(ax[3][0]+5,ax[3][1]))
    screen.blit(font.render("O",True,(255,255,255)),(ax[0][0]+5,ax[0][1]))

# ------------------ MATRIX ------------------

def get_transformation_matrix():
    Rx = np.array([[1,0,0],[0,math.cos(angle_x),-math.sin(angle_x)],[0,math.sin(angle_x),math.cos(angle_x)]])
    Ry = np.array([[math.cos(angle_y),0,math.sin(angle_y)],[0,1,0],[-math.sin(angle_y),0,math.cos(angle_y)]])
    Rz = np.array([[math.cos(angle_z),-math.sin(angle_z),0],[math.sin(angle_z),math.cos(angle_z),0],[0,0,1]])

    S = np.array([[scale,0,0],[0,scale*1.5,0],[0,0,scale*0.5]])

    if shear_on:
        k = math.sin(pygame.time.get_ticks()*0.002)
        Sh = np.array([[1,k,0],[0.3,1,0],[0,0.5,1]])
    else:
        Sh = np.identity(3)

    return Sh @ Rz @ Ry @ Rx @ S

# ------------------ MAIN LOOP ------------------

while True:
    screen.fill(DARK_BG)

    # GRID
    for x in range(0,WIDTH,40):
        pygame.draw.line(screen,GRID_COLOR,(x,0),(x,HEIGHT),1)
    for y in range(0,HEIGHT,40):
        pygame.draw.line(screen,GRID_COLOR,(0,y),(WIDTH,y),1)

    # SIDEBAR
    pygame.draw.rect(screen,(10,20,30),(0,0,220,HEIGHT))
    pygame.draw.line(screen,(0,255,255),(220,0),(220,HEIGHT),2)

    # TITLES
    screen.blit(font.render("SHAPES", True, NEON_BLUE), (30,20))
    screen.blit(font.render("CONTROLS", True, NEON_BLUE), (30,480))

    # SHAPE BUTTONS
    for i,name in enumerate(shape_names):
        rect=pygame.Rect(20,60+i*45,180,35)
        color=(0,150,180) if name==active_shape else (0,70,90)
        pygame.draw.rect(screen,color,rect)
        screen.blit(font.render(name,True,NEON_BLUE),(rect.x+10,rect.y+8))

    # CONTROL BUTTONS
    proj_button  = pygame.Rect(20,520,180,35)
    eigen_button = pygame.Rect(20,565,180,35)
    pca_button   = pygame.Rect(20,610,180,35)

    pygame.draw.rect(screen,(0,120,150),proj_button)
    pygame.draw.rect(screen,(180,120,0) if show_eigen else (120,80,0),eigen_button)
    pygame.draw.rect(screen,(150,0,180) if show_pca else (80,0,120),pca_button)

    screen.blit(font.render("3D → 2D VIEW",True,NEON_BLUE),(30,528))
    screen.blit(font.render("Eigen Vectors",True,NEON_BLUE),(30,573))
    screen.blit(font.render("Show PCA",True,NEON_BLUE),(30,618))

    # EVENTS
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit(); sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            mx,my=event.pos

            for i,name in enumerate(shape_names):
                rect=pygame.Rect(20,60+i*45,180,35)
                if rect.collidepoint(mx,my):
                    active_shape=name
                    vertices,edges=shape_map[name]()

            if proj_button.collidepoint(mx,my):
                projection_demo=not projection_demo
            if eigen_button.collidepoint(mx,my):
                show_eigen=not show_eigen
            if pca_button.collidepoint(mx,my):
                show_pca=not show_pca

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_h:
                shear_on=not shear_on
            if event.key==pygame.K_v:
                show_live_eigen=not show_live_eigen

    # TRANSFORMATIONS (UNCHANGED)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: angle_y-=0.05
    if keys[pygame.K_RIGHT]: angle_y+=0.05
    if keys[pygame.K_UP]: angle_x-=0.05
    if keys[pygame.K_DOWN]: angle_x+=0.05
    if keys[pygame.K_q]: angle_z-=0.05
    if keys[pygame.K_e]: angle_z+=0.05
    if keys[pygame.K_w]: scale+=0.02
    if keys[pygame.K_s]: scale-=0.02

    if keys[pygame.K_a]: tx-=0.05
    if keys[pygame.K_d]: tx+=0.05
    if keys[pygame.K_r]: ty+=0.05
    if keys[pygame.K_f]: ty-=0.05
    if keys[pygame.K_z]: tz+=0.05
    if keys[pygame.K_x]: tz-=0.05

    scale=max(scale,0.1)

    t=vertices.copy()*scale
    if shear_on: t=shear(t)

    t=rotX(t,angle_x)
    t=rotY(t,angle_y)
    t=rotZ(t,angle_z)
    t+=np.array([tx,ty,tz])

    # DRAW OBJECT
    if not projection_demo:
        pts = project_perspective(t,650)

        for e in edges:
            pygame.draw.line(screen,NEON_BLUE,pts[e[0]],pts[e[1]],2)

        draw_axes(650)
        offset = 650

    else:
        pts_3d = project_perspective(t,350)
        pts_2d = project_orthographic(t,900)

    # draw both
        for e in edges:
            pygame.draw.line(screen,NEON_BLUE,pts_3d[e[0]],pts_3d[e[1]],2)
            pygame.draw.line(screen,(0,255,150),pts_2d[e[0]],pts_2d[e[1]],2)

    # projection lines
        for i in range(len(pts_3d)):
            pygame.draw.line(screen,(80,200,150),pts_3d[i],pts_2d[i],1)

        draw_axes(350)
        offset = 350

    # FEATURES
    if show_eigen: draw_eigen(offset)
    if show_live_eigen: draw_live_eigen(offset)
    if show_pca: draw_pca(t,offset)

    pygame.display.update()
    clock.tick(60)