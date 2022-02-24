import turtle as t

class Window:
  def __init__(self, width=450, height=450, color="white"):
    self.width = width
    self.height = height
    self.color = color
  
  def draw_box(self, function, width, height, position, text="", text_size=0):
    boxer = t.Turtle()
    boxer.speed(0)
    text_writer = t.Turtle()
    text_writer.speed(0)
    boxer.penup()
    boxer.goto(position[0], position[1])
    boxer.pendown()
    boxer.forward(width)
    boxer.right(90)
    boxer.forward(height)
    boxer.right(90)
    boxer.forward(width)
    boxer.right(90)
    boxer.forward(height)
    boxer.hideturtle()
    boxer.onclick(function)
    text_writer.penup()
    text_writer.goto(position[0], position[1])
    text_writer.right(90)
    text_writer.forward((height / 2) + text_size - 1)
    text_writer.left(90)
    text_writer.forward((width / 2) - (len(list(text))* 2) - text_size)
    text_writer.write(text, font=("arial", text_size))
    text_writer.hideturtle()
  
  def create(self):
    output = t.Screen()
    output.mainloop()





class Button(Window):
  def __init__(self, text, function, background_color="white", outline_color="black", text_color="black", width=50, height=30, boldness=5, position=(0, 0), text_size=5):
    self.text = text
    self.function = function
    self.background_color = background_color
    self.outline_color = outline_color
    self.text_color = text_color
    self.width = width
    self.height = height
    self.boldness = boldness
    self.position = position
    self.text_size = text_size
    
    super().draw_box(function, width, height, position, text, text_size)