import pygame
from laser import Laser

class Weapon:
    def __init__(self, name, image, damage, ammo, laser_img):
        self.name = name
        self.image = image
        self.damage = damage
        self.ammo = ammo
        self.laser_img = laser_img

    def fire(self, x, y, target_x, target_y):
        if self.ammo > 0:
            self.ammo -= 1
            return Laser(x, y, target_x, target_y, self.laser_img, 'mario')
        return None

    def reload(self, ammo):
        self.ammo += ammo

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
