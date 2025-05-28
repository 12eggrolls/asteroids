import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):  # check Sprite for member
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0) # idk what this mean
        self.radius = radius
    
    def draw(self, screen):
        pass  # override

    def update(self, dt):
        pass  # override

