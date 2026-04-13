import pygame
import numpy as np
import sys

from shapes import *
from transformation import *
from projection import *
from visualization import *

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
show_live_eigen = False   # 🔥 FIXED

# SHAPES
shape_map={
    "cube":cube,"pyramid":pyramid,"tetra":tetra,
    "octa":octa,"prism":prism,"tri_prism":tri_prism,
    "sphere":sphere,"cylinder":cylinder,
    "cone":cone,"pent_prism":pent_prism
}

shape_names=list(shape_map.keys())

active_shape="cube"
vertices,edges=shape_map[active_shape]()

# TRANSFORM VARIABLES
angle_x=angle_y=angle_z=0
scale=1
tx, ty, tz = 0,0,0

# AXES
def draw_axes(offset_x):
    axis_len=3*scale
    axes=np.array([[0,0,0],[axis_len,0,0],[0,axis_len,0],[0,0,axis_len]])

    axes=rotX(axes,angle_x)
    axes=rotY(axes,angle_y)
    axes=rotZ(axes,angle_z)
    axes+=np.array([tx,ty,tz])

    ax=project_perspective(axes,offset_x)

    pygame.draw.line(screen,(255,0,0),ax[0],ax[1],3)
    pygame.draw.line(screen,(0,255,0),ax[0],ax[2],3)
    pygame.draw.line(screen,(0,150,255),ax[0],ax[3],3)

    pygame.draw.circle(screen,(255,255,255),ax[0],4)

    screen.blit(font.render("X",True,(255,0,0)),(ax[1][0]+5,ax[1][1]))
    screen.blit(font.render("Y",True,(0,255,0)),(ax[2][0]+5,ax[2][1]))
    screen.blit(font.render("Z",True,(0,150,255)),(ax[3][0]+5,ax[3][1]))
    screen.blit(font.render("O",True,(255,255,255)),(ax[0][0]+5,ax[0][1]))

# MAIN LOOP
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
                show_live_eigen=not show_live_eigen   # 🔥 FIXED

    # KEY CONTROLS
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

    # APPLY TRANSFORMATIONS
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

        for e in edges:
            pygame.draw.line(screen,NEON_BLUE,pts_3d[e[0]],pts_3d[e[1]],2)
            pygame.draw.line(screen,(0,255,150),pts_2d[e[0]],pts_2d[e[1]],2)

        for i in range(len(pts_3d)):
            pygame.draw.line(screen,(80,200,150),pts_3d[i],pts_2d[i],1)

        draw_axes(350)
        offset = 350

    # FEATURES
    if show_eigen:
        draw_eigen(screen, font, project_perspective, tx, ty, tz, offset)

    if show_live_eigen:
        draw_live_eigen(screen, font, project_perspective,
                        tx, ty, tz, offset,
                        angle_x, angle_y, angle_z, scale, shear_on)

    if show_pca:
        draw_pca(screen, font, project_perspective, t, offset)

    pygame.display.update()
    clock.tick(60)