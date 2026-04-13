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