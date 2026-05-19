from pygame import* 

win_width= 700
win_height= 500 
back= (200,200,200)
window= display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
window.fill(back)
run= True
finish= False
font.init()
font1= font.SysFont('verdana', 40)
win_l = font1.render('PlayerL WIN', True, (200,30,30))
win_r = font1.render('PlayerR WIN', True, (200,30,30))
class Game_Sprite(sprite.Sprite):
    def __init__(self,picture, w,h,x,y,speed_x,speed_y):
        super().__init__()
        self.image= transform.scale(image.load(picture),(w,h))
        self.rect= self.image.get_rect()
        self.rect.x= x
        self.rect.y= y 
        self.speed_x= speed_x
        self.speed_y= speed_y 
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(Game_Sprite):
    def update_l(self):
        keys= key.get_pressed()
        if keys [K_w] and self.rect.y> 0: 
            self.rect.y-= self.speed_y 
        if keys [K_s] and self.rect.y< win_height- 150: 
            self.rect.y+= self.speed_y
    def update_ball(self):
        self.rect.x+= self.speed_x
        self.rect.y+= self.speed_y 
        if self.rect.y <  0 or self.rect.y>450:
            self.speed_y *=-1
    def update_r(self):
        keys= key.get_pressed()
        if keys [K_UP] and self.rect.y> 0: 
            self.rect.y-= self.speed_y 
        if keys [K_DOWN] and self.rect.y< win_height- 150: 
            self.rect.y+= self.speed_y
        



player2= Player('platform.png',30,150,670,100,0,10)
player= Player('platform.png', 30,150,0,200,0,10)
ball= Player("ball_p.png",40,40,120,100,5,5)

while run:
    
    for e in event.get():
        if e.type== QUIT:
            run= False 
   # elif e.type== KEYDOWN:
        #if e.key==K_SPACE:
            #score_1= 0 
           #score_r=0
            #time.delay(1000)
            #finish= False 
    if not finish:
        window.fill(back)
        ball.reset()
        ball.update_ball()
        player.reset()
        player.update_l()
        player2.reset()
        player2.update_r()
        
        if sprite.collide_rect(player_l,ball) or sprite.collide_rect(player_r, ball):
            ball.speed_x        *= -1
        if ball.rect.x<0:
            window.blit(win_l, (200,200))
            finish = True 
        if ball.rect.x> win_weight-50:
            window.blit(win_r, (200,200))
            finish = True 
        
    time.delay(40)
    display.update()