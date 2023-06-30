import pygame
import math
pygame.init()

screenX = 800
screenY = 500
black = (0, 0, 0)
white = (255, 255, 255)
gray = (209, 209, 209)
screen = pygame.display.set_mode([screenX, screenY])
mConv = 50

ballElevation = -(2 * mConv)
vx = 5 * mConv
vy = -(10 * mConv)
g = 9.8 * mConv


ballX = 125
ballY = ballElevation + 375
dix = 125
diy = ballY
rate = 60
dt = 1/rate
#pixels per second (1m = 50)
#-y -> up

text_font = pygame.font.SysFont("Arial", 25)

traildots = {}

running = True

def drawText(text, font, colour, x, y):
    img = font.render(text, True, colour, (255, 255, 0))
    textRect = img.get_rect()
    textRect.center = (x, y)
    screen.blit(img, textRect)
def drawGrid():
    for x in range(1, 16):
        pygame.draw.line(screen, gray, ((x*screenX/16), 0), ((x*screenX/16), screenY))
        pygame.draw.line(screen, gray, (0, x*screenY/10), (screenX, x*screenY/10))

def drawGround():
    pygame.draw.line(screen, black, (0, 4 * (screenY / 5)), (screenX, 4 * (screenY / 5)), width=3)

def trail():
    for a, b in traildots.items():
        pygame.draw.circle(screen, black, (b[0], b[1]), 4)


checkpoints = 0
clock = pygame.time.Clock()
airtime = 0
tickers = 0
moving = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    pygame.draw.line(screen, black, (dix, diy), (ballX, ballY))
    drawGrid()
    drawGround()
    trail()
    angle = float("%.2f" % round((-(math.atan(vy/vx)*180)/math.pi),3))
    pygame.draw.circle(screen, (0, 0, 255), (ballX, ballY), 25)
    #drawText("hello", text_font, black, 50, 450)
    dx = (ballX - dix)/50
    dispx = float("%.2f" % round(dx, 3))
    drawText(f"dx: {dispx}m", text_font, black, 710, 90)
    airtime = float("%.2f" % round(tickers/60, 3))
    dispv = float("%.2f" % round(((vx ** 2 + vy ** 2) ** 0.5)/50, 3))
    drawText(f"v: {dispv}m/s", text_font, black, 710, 120)
    drawText(f"θ: {angle}°", text_font, black, 710, 30)
    if tickers % 6 == 0:
        checkpoints += 1
        traildots.update({checkpoints : [ballX, ballY, angle, vx, tickers, vy]})
    drawText(f"dt: {airtime}s", text_font, black, 710, 60)
    pygame.display.flip()
    if moving:
        clock.tick(rate)
        tickers += 1
        ballX = ballX + vx*dt
        ballY = ballY + vy*dt
        vy = vy + g*dt
        if ballY >= 374:
            moving = False
            traildots.update({checkpoints: [ballX, ballY, angle, vx, tickers, vy]})
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN and moving == False:
            pos = pygame.mouse.get_pos()
            for a, b in traildots.items():
                if ((pos[0] - b[0]) ** 2 + (pos[1] - b[1]) ** 2) ** 0.5 <= 4:
                    ballX = b[0]
                    ballY = b[1]
                    angle = b[2]
                    vx = b[3]
                    tickers = b[4]
                    vy = b[5]
        if events.type == pygame.QUIT:
            pygame.quit()

pygame.quit()