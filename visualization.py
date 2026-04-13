import numpy as np
import pygame
from transformation import get_transformation_matrix

def draw_eigen(screen, font, project, tx, ty, tz, offset_x):
    M = np.array([[1.2,0.5,0],[0,1,0],[0,0,1]])
    vals, vecs = np.linalg.eig(M)

    origin = project(np.array([[tx,ty,tz]]), offset_x)[0]

    colors = [(255,0,0), (0,255,0), (255,255,0)]

    for i in range(3):
        v = vecs[:,i]*2
        pt = project(np.array([v]), offset_x)[0]
        pygame.draw.line(screen, colors[i], origin, pt, 3)
        screen.blit(font.render(f"λ{i+1}={round(vals[i],2)}", True, colors[i]), (pt[0]+10, pt[1]+10))


def draw_live_eigen(screen, font, project, tx, ty, tz, offset_x,
                    angle_x, angle_y, angle_z, scale, shear_on):

    T = get_transformation_matrix(angle_x, angle_y, angle_z, scale, shear_on)
    vals, vecs = np.linalg.eig(T)

    origin = project(np.array([[tx,ty,tz]]), offset_x)[0]
    colors = [(255,0,0), (0,255,0), (255,255,0)]

    for i in range(3):
        v = vecs[:,i].real * 2
        pt = project(np.array([v]), offset_x)[0]
        pygame.draw.line(screen, colors[i], origin, pt, 3)

        text = font.render(f"λ{i+1}={round(vals[i].real,2)}", True, colors[i])
        screen.blit(text, (pt[0]+10, pt[1]+10))


def draw_pca(screen, font, project, points, offset_x):
    mean = np.mean(points, axis=0)
    centered = points - mean
    cov = np.cov(centered.T)
    vals, vecs = np.linalg.eig(cov)

    origin = project(np.array([mean]), offset_x)[0]

    for i in range(2):
        v = vecs[:, i] * 3
        p2 = project(np.array([mean + v]), offset_x)[0]
        pygame.draw.line(screen, (255,100,200), origin, p2, 3)

    # TEXT DISPLAY
    screen.blit(font.render("PCA (Principal Components)", True, (255,100,200)), (250, 20))

    y_offset = 45
    screen.blit(font.render("Covariance Matrix:", True, (200,200,200)), (250, y_offset))

    for i in range(3):
        row_text = f"[ {round(cov[i][0],2)}  {round(cov[i][1],2)}  {round(cov[i][2],2)} ]"
        screen.blit(font.render(row_text, True, (180,180,180)), (250, y_offset + 20 + i*20))

    screen.blit(font.render("Eigenvalues:", True, (200,200,200)), (250, y_offset + 90))

    for i in range(3):
        val_text = f"λ{i+1} = {round(vals[i].real,2)}"
        screen.blit(font.render(val_text, True, (255,180,100)), (250, y_offset + 110 + i*20))