import arcade

# Definición de constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Rectángulo con Python"

class RectanguloWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        self.draw_rectangle(20, 20, 50, 30, arcade.color.RED)

    def draw_rectangle(self, x0, y0, width, height, color):
        x1, y1 = x0 + width, y0
        x2, y2 = x0 + width, y0 + height
        x3, y3 = x0, y0 + height

        # Lados del rectángulo
        self.draw_line(x0, y0, x1, y1, color)
        self.draw_line(x1, y1, x2, y2, color)
        self.draw_line(x2, y2, x3, y3, color)
        self.draw_line(x3, y3, x0, y0, color)

    def draw_line(self, x0, y0, x1, y1, color):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            arcade.draw_point(x0, y0, color, 1)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

if __name__ == "__main__":
    window = RectanguloWindow()
    arcade.run()