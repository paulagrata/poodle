from os import walk #walk through dif folders.
import pygame

def import_folder(path):
    surface_list = []
    for __, __, img_files in walk(path): #for folder_name, sub_folder, img_files [ony want img_files]
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list