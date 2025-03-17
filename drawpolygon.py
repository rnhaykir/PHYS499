# Draws a triangle with vertices (x0, y0), (x1, y1), and (x2, y2)
# t: Turtle Graphics object for drawing
# x: a list of 3 numbers corresponding to the x coordinates of the vertices of the triangle to draw
# y: a list of 3 numbers corresponding to the x coordinates of the vertices of the triangle to draw
def draw_triangle(t, x, y):
    coors = [(x[0], y[0]), (x[1], y[1]), (x[2], y[2])]
    drawtriangle(t, coors)

# Draws a filled triangle with vertices (x0, y0), (x1, y1), and (x2, y2)
# t: Turtle Graphics object for drawing
# x: a list of 3 numbers corresponding to the x coordinates of the vertices of the triangle to draw
# y: a list of 3 numbers corresponding to the x coordinates of the vertices of the triangle to draw
def draw_filled_triangle(t, x, y):
    coors = [(x[0], y[0]), (x[1], y[1]), (x[2], y[2])]
    drawfilledtriangle(t, coors)

# Draws a triangle with vertices (x0, y0), (x1, y1), and (x2, y2)
# t: Turtle Graphics object for drawing
# points: a vector of (x, y) coordinates of the vertices of the triangle to draw like
#
#       [(x[0], y[0]), (x[1], y[1]), (x[2], y[2])]
#
def drawtriangle(t, points):
    t.penup()
    s = t.getscreen()
    w = s.canvwidth
    h = s.canvheight
    t.goto(w * points[0][0], w * points[0][1])
    t.pendown()
    for point in points:
        t.goto(w * point[0], w * point[1])

    t.goto(w * points[0][0], w * points[0][1])  # Go back to the origin to close the polygon shape

# Draws a filled triangle with vertices (x0, y0), (x1, y1), and (x2, y2)
# t: Turtle Graphics object for drawing
# points: a vector of (x, y) coordinates of the vertices of the triangle to draw like
#
#       [(x[0], y[0]), (x[1], y[1]), (x[2], y[2])]
#
def drawfilledtriangle(t, points):
    t.penup()
    s = t.getscreen()
    w = s.canvwidth
    h = s.canvheight
    t.begin_fill()
    t.goto(w * points[0][0], w * points[0][1])
    t.pendown()
    for point in points:
        t.goto(w * point[0], w * point[1])

    t.goto(w * points[0][0], w * points[0][1])  # Go back to the origin to close the polygon shape
    t.end_fill()
