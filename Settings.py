class Global_Settings:
    def __init__(self):
        self.draw_color = None

    @property
    def draw_color(self):
        return self.draw_color

    @draw_color.setter
    def draw_color(self,value):
        self.draw_color = value

settings = Global_Settings