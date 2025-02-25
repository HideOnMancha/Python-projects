import pyautogui as p 
import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load('C:/Users/Luan/Downloads/mcrafadavj.mp3') 
pygame.mixer.music.play()

a1 = p.confirm('Pausar o player?', buttons=['Sim','Não'])

if a1=='Sim':
    p.alert('Voce pausou o player!')
        pygame.mixer.music.stop:
        







