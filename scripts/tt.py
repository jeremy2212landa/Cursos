import turtle

col = ('yellow','red','orange','green', 'blue','purple')

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
for i in range (150):
    t.color(col[i%6])
    t.forward(i*4)
    t.left(150)
    t.width(2)

