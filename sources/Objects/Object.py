class Object:
    def __init__(self):
        # object position
        self.x = 0
        self.y = 0
        self.delta_time = 0

        # object state
        self.state_index = 0

        # sprite information
        self.spr_width = 0
        self.spr_height = 0
        self.spr_speed = 0
        self.spr_index = 0
        self.spr_size = 0
        self.spr_list = []
        self.spr_x = self.x + self.spr_width / 2 * self.spr_size
        self.spr_y = self.x + self.spr_height / 2 * self.spr_size

    def draw_image(self):
        return None