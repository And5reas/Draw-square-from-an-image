# Importar a biblioteca OpenCV
import cv2
# Importar a biblioteca NumPy
import numpy as np
import turtle

# load img
img = cv2.imread('doisQuadrados2.png')
img2 = cv2.imread('rect344.png')

# Define the blue colour we want to find - remember OpenCV uses BGR ordering
blue = [255, 0, 0]
red = [0, 0, 255]

# Get X and Y coordinates of all blue pixels
y, x = np.where(np.all(img == blue, axis=2))
y2, x2 = np.where(np.all(img == red, axis=2))
zipped = np.column_stack((x, y))
def getString():
    print(x2, y2)

    print("x[-1] =", x[-1])
    print("y[0] =", y[0])
    print("zipped[0] =", zipped[0])
    print("zipped[-1] =", zipped[-1])
    print("zipped[0] - zipped[-1] =", zipped[0] - zipped[-1])
    print("zipped[-1] - zipped[0] =", zipped[-1] - zipped[0])

def desenharQuadrado():
    tela = turtle.Screen()
    tela.bgcolor("green")

    desenhista = turtle.Turtle()
    desenhista.penup()
    desenhista.sety(-y[0]*5)
    desenhista.setx(x[0]*5)
    desenhista.pendown()
    desenhista.color("blue")
    desenhista.begin_fill()
    desenhista.forward((x[-1] - x[0])*5)
    desenhista.right(90)
    desenhista.forward((y[-1] - y[0])*5)
    desenhista.right(90)
    desenhista.forward((x[-1] - x[0])*5)
    desenhista.right(90)
    desenhista.forward((y[-1] - y[0])*5)
    desenhista.end_fill()

    desenhista2 = turtle.Turtle()
    desenhista2.penup()
    desenhista2.sety(-y2[0]*5)
    desenhista2.setx(x2[0]*5)
    desenhista2.pendown()
    desenhista2.color("red")
    desenhista2.begin_fill()
    desenhista2.forward((x2[-1] - x2[0])*5)
    desenhista2.right(90)
    desenhista2.forward((y2[-1] - y2[0])*5)
    desenhista2.right(90)
    desenhista2.forward((x2[-1] - x2[0])*5)
    desenhista2.right(90)
    desenhista2.forward((y2[-1] - y2[0])*5)
    desenhista2.end_fill()

    tela.exitonclick()