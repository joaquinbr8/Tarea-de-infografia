import arcade

# globales
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_TITLE = "hola arcade"

class LineWindow(arcade.Window):
    def __init__(self, width, height, title):
        # iniciar el padre
        super().__init__(width, height, title)
        # fondo:
        arcade.set_background_color(arcade.color.AMETHYST)
    
    def draw_vertical_line(self, x1, y1, x2, y2, color, size=2):
        assert x1 == x2
        for y in range(y1, y2 + 1):
            # print(x1, y)
            arcade.draw_point(x1, y, color,size)


    def on_draw(self):
        arcade.start_render()
        # self.draw_vertical_line(50, 10, 50, 250, arcade.color.AERO_BLUE)
        x1 = 20
        y1 = 22
        x2 = 300
        y2 = 250
        arcade.draw_line(x1, y1, x2, y2, arcade.color.AERO_BLUE, 2)
        

window = LineWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

arcade.run()
