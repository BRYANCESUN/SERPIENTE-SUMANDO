import constantes
 
class Mundo ():
    def __init__(self):
        self.map_titles = []
 
    def process_data (self, data, tile_list):
        self.level_length = len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image = tile_list[tile]
                image_rect = image.get_rect()
                image_x = x * constantes.TAM_CELDA
                image_y = y * constantes.TAM_CELDA
                # topleft: la esquina superior izquierda del tile queda en su celda
                # (con center, cada tile quedaba corrido media celda y cortado)
                image_rect.topleft = (image_x , image_y)
                title_data = (image, image_rect, image_x, image_y)
                self.map_titles.append(title_data)
 
    def draw(self, surface):
        for tile in self.map_titles:
            surface.blit(tile[0], tile[1])