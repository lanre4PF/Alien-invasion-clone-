class Settings():
    def __init__(self):
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_colour = (230,230,230)
        self.caption = "Alien Invasion"
        self.speed_factor = 1.5

        #Bullet settings
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3