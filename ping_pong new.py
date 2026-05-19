from pygame import* 
#часть1
win_width= 700
win_height= 500 
back= (255,120,30)
window= display.set_mode((win_width, win_height))
display.set_caption('Ping Pong')
window.fill(back)
run= True
finish= False

class Game_Sprite(sprite.Sprite):
    def __init__(self,picture, w,h,x,y,speed_x,speed_y):
        super().__init__()
        self.image= transform.scale(image.load(picture),(w,h))
        self.rect= self.image.get_rect()
        self.rect.x= x
        self.rect.y= y 
        self.speed_x= x
        self.speed_y= y 
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

ball= Game_Sprite("ball_p.png",40,40,120,100,12,12)
ball.reset()




while run:
    time.delay(50)
    display.update()
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
