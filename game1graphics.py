from random import randint
import turtle as turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False
        
# Graphic point on canvas
class GuiPoint(Point):
    def draw(self, canvas):
        canvas.penup()      # Pull the pen up – no drawing when moving.
        canvas.goto(self.x, self.y)
        canvas.pendown()    # Pull the pen down – drawing when moving.
        canvas.dot(6, "red")       
        
class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

# Graphic rectangle on canvas
class GuiRectangle(Rectangle):
    def draw(self, canvas):
        
        canvas.penup()      # Pull the pen up – no drawing when moving.
        canvas.goto(self.point1.x, self.point1.y)
        
        canvas.pendown()    # Pull the pen down – drawing when moving.
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)      
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)                 
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)     
        canvas.forward(self.point2.y - self.point1.y)
        
        
         
# Create rectangle object
rectangle = GuiRectangle(Point(randint(0, 10), randint(0, 10)), 
              Point(randint(10, 40), randint(10, 40)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)
 
# Get point and area from user
user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))
 
# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
# print(GuiRectangle(rectangle.point1, rectangle.point2).area())

# Create a turtle canvas
myt = turtle.Turtle()
rectangle.draw(myt)

# Draw user point
user_point_gui = GuiPoint(user_point.x, user_point.y)
user_point_gui.draw(myt)

# Finish turtle
# turtle.done()
turtle.Screen().exitonclick()
