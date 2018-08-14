class Settings:
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 356
        self.bg_color = 227, 154, 171
        self.play = False

        self.ground = y = self.screen_height - 20
        self.buffer = .03

        self.cactus_speed = 10
        self.cacti_allowed = 2
        self.score = 0

    def reset(self):
        self.play = False
        self.score = 0