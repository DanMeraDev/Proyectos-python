import pygame
import random
import math
from pygame import mixer
from pyvidplayer import Video

# Inicializar Pygame
pygame.init()

# Crear pantalla
pantalla = pygame.display.set_mode((900, 700))
darth_vader = pygame.image.load("starwars.jpg")
darth_vader_scala = pygame.transform.scale(darth_vader, (900, 700))
inicio_img = pygame.image.load("btn.png").convert_alpha()
musica_reproducida = False
seguir_ejecutando = True
tiempo_inicio = pygame.time.get_ticks()  
tiempo_esperado = 64000

# Título e Icono
pygame.display.set_caption("Star Wars - The Empire Strikes Back")
icono = pygame.image.load("orden-jedi.png")
pygame.display.set_icon(icono)


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self):
        
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        pantalla.blit(self.image, (self.rect.x, self.rect.y))

boton_inicio = Button(180, 300, inicio_img, 1)
#variables Jugador
nave = pygame.image.load("xwing.png")
nave_escala = pygame.transform.scale(nave, (90, 70))
jugador_x = 405
jugador_y = 600
jugador_x_cambio = 0

# Variables enemigo
enemigo = []
enemigo_escala = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos): 
    enemigo_escala.append(pygame.transform.scale(pygame.image.load("pngegg.png"), (90, 70)))
    enemigo_x.append(random.randint(0, 800))
    enemigo_y.append(random.randint(50, 300))
    enemigo_x_cambio.append(0.15)
    enemigo_y_cambio.append(70)

# Variables bala
balas = []
bala = pygame.image.load("Laser.png")
bala_escala = pygame.transform.scale(bala, (110, 100))
bala_x = 0
bala_y = 600
bala_x_cambio = 0
bala_y_cambio = 1
bala_visible = False
se_ejecuta = True

# variable puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# texto final de juego
fuente_final = pygame.font.Font("freesansbold.ttf", 40)

# funcion final
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (60, 200))

# funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# funcion jugador
def jugador(x, y):
    pantalla.blit(nave_escala, (x, y))
    
# funcion enemigo
def enemigo(x, y, n):
    pantalla.blit(enemigo_escala[n], (x, y))
    
    
# funcion disparar bala 
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala_escala, (x-10, y - 60))
    

# funcion detectar colisiones
def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1-x_2, 2) + math.pow(y_2-y_1, 2))
    if distancia < 50:
        mixer.Sound("golpe.mp3").play()
        return True
    else: 
        return False

# Funcion juego 
def pantalla_juego():
    global jugador_x, jugador_x_cambio, puntaje, pantalla, se_ejecuta, jugador_y, balas, cantidad_enemigos, musica_reproducida
    pantalla.blit(darth_vader_scala, (0, 0))
    
    # Musica de fondo
    if not musica_reproducida:
        mixer.music.load("background.mp3")
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)
        musica_reproducida = True
    
    # iterar eventos
    for evento in pygame.event.get():    
        if evento.type == pygame.QUIT:
            se_ejecuta = False    
        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_d:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_bala = mixer.Sound("blaster.mp3")
                    sonido_bala.set_volume(0.7)
                    sonido_bala.play()
                    nueva_bala = {
                    "x": jugador_x-25,
                    "y": jugador_y - 67,
                    "velocidad": -2.5
                    }
                    balas.append(nueva_bala)
        # evento soltar flecha
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                jugador_x_cambio = 0

    # Modificar ubicacion jguador
    jugador_x += jugador_x_cambio
    
    # Mantener dentro de bordes enemigo
    if jugador_x <= 0:
        jugador_x = 0
    if jugador_x >= 810:
        jugador_x = 810
        
    # Modificar ubicacion enemigo
    for e in range(cantidad_enemigos):
        #fin del juego
        if enemigo_y[e] > 520:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            balas.clear()
            texto_final()
            return False
        
        enemigo_x[e] += enemigo_x_cambio[e]

    # Mantener dentro de bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.15
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_x[e] >= 810:
            enemigo_x_cambio[e] = -0.15
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # colision
        for bala in balas:
            colision_bala_enemigo = colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("golpe.mp3")
                sonido_colision.set_volume(0.65)
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break
        
        enemigo(enemigo_x[e], enemigo_y[e], e)
                
    # Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(bala_escala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
        
    
    jugador(jugador_x, jugador_y)
    
    # Mostra puntaje
    mostrar_puntaje(texto_x, texto_y)
    return True

# Pantalla de inicio
inicio = Video("0329.mp4")
inicio.set_size((900, 700))


def intro():
    global se_ejecuta
    for evento in pygame.event.get():
        #evento c errar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
    inicio.draw(pantalla, (0, 0))
    return boton_inicio.clicked

mixer.music.load("background.mp3")
mixer.music.set_volume(1)



# Loop del juego
while se_ejecuta:
    #RGB
    pantalla.fill((153, 51, 255))
    
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicio
    
    # Pantallas
    if not musica_reproducida:
        if intro():
            pantalla_juego()
            inicio.close()
        if tiempo_transcurrido >= tiempo_esperado:
            boton_inicio.draw() 
        
    else:
        pantalla_juego()
    
    
    
    # Actualizar
    pygame.display.update()
    
    