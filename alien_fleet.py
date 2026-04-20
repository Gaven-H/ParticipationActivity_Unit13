import pygame

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
    
    def create_fleet(self) -> None:
        alien_w = self.settings.alien_w
        screen_w = self.game.settings.screen_w

        fleet_w = self.calculate_fleet_size(alien_w, screen_w)
        fleet_horizontal_space = fleet_w * alien_w

    def calculate_fleet_size(self, alien_w, screen_w):
        fleet_w = (screen_w//alien_w)
        
        if fleet_w % 2 == 0:
            fleet_w -=1
        else:
            fleet_w -= 2

        return fleet_w

        