import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):  # check Sprite/instance for containers member
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0) # idk what this mean
        self.radius = radius

    def is_collided(self, CircleShape):
        if self.position.distance_to(CircleShape.position) <= self.radius + CircleShape.radius:
            return True
        else:
            return False
    def draw(self, screen):
        pass  # override

    def update(self, dt):
        pass  # override

