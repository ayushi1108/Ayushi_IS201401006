import pygame,os,random
from random import randint
from pygame.locals import *
wix=1000
wiy=750
pri=0

def msg (screen,text,color=(55,55,55),size=36,pos=(-1,-1)):
    if pos[0] ==-1:pos=(screen.get_rect().centerx,pos[1])
    if pos[1] ==-1:pos=(pos[0],screen.get_rect().centery)
    font = pygame.font.Font(None, size)
    text = font.render(text, 1, color)
    textpos = text.get_rect()
    textpos.centerx = pos[0]
    textpos.centery= pos[1]
    screen.blit(text, textpos)

def load_sound(name):
    if not pygame.mixer or not pygame.mixer.get_init():
        pass
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print ('Cannot load sound: %s' % name)
        raise SystemExit(str(geterror()))
    return sound


class button():
    x=0
    y=-wiy//5
    h=wix//3-1
    l=wiy//5
    enclick=True
    midl=0
    def pos(self,n):
        self.x=n*wix//3
    def midd(self,n):
        self.midl=n
    def update(self,screen):
        if self.enclick :
	    pygame.draw.rect(screen,(0,0,0),[self.x,self.y,self.h,self.l])
        else :pygame.draw.rect(screen,(180,180,180),[self.x,self.y,self.h,self.l])
	#r=0
	#g=0
	#b=0
	#if self.x==0:
	#	r=255
	#elif self.x==333:
	#	g=255
	#else:
	#	b=255
        #pygame.draw.rect(screen,(r,g,b),[self.x,self.y,self.h,self.l],2)
	pygame.draw.rect(screen,(255,0,0),[0,self.y,self.h,self.l],2)
        pygame.draw.rect(screen,(0,255,0),[333,self.y,self.h,self.l],2)
        pygame.draw.rect(screen,(0,0,255),[666,self.y,self.h,self.l],2)
	print self.midl
        #msg(screen,"LESS THAN",color=(0,128,255),pos=(167,self.y+75))
	msg(screen,"MID = "+str(self.midl),color=(0,128,255),pos=(500,self.y+75))
        #msg(screen,"HIGHER THAN",color=(0,128,255),pos=(833,self.y+75)) 
    def click(self,ps):
        if ps[0] in range(self.x,self.x+self.h):
            if ps[1] in range (self.y,self.y+self.l):
                self.enclick =False
		if self.x==333:
		    screen.fill((224,224,255))
		    msg(screen,"YOU WIN ",color=(110,128,225),size=100,pos=(-1,-1))
		    msg(screen,"SCORE "+str(score),color=(0,255,0),pos=(-1,30))
		    msg(screen,"Developed by Ayushi Anand and Chaitanya Nagpal",color=(110,108,225),pos=(-1,wiy//2+40))
		    pygame.display.update()
		    pygame.time.wait(4000)
		    x=0
                    while x<len(mids):
		    	screen.fill((224,224,255))
		    	msg(screen,"SEARCH "+str(search),color=(255,0,0),pos=(-1,100))
		        msg(screen,"HIGH = "+str(highs[x])+" MID = "+str(mids[x])+" LOW = "+str(lows[x]),color=(110,108,225),pos=(-1,wiy/2-200))
			if mids[x]>search:
			    x1=0
			    msg(screen,"Searched element less than mid so go left",color=(110,108,225),pos=(-1,wiy/2-100))
			elif mids[x]<search:
			    x1=666
			    msg(screen,"Searched element greater than mid so go right",color=(110,108,225),pos=(-1,wiy/2-100))
			else:
			    x1=333
			    msg(screen,"Searched element equal to mid select mid",color=(110,108,225),pos=(-1,wiy/2-100))	
			pygame.draw.rect(screen,(0,0,0),[x1,wiy/2,self.h,self.l])
			msg(screen,"LESS THAN",color=(0,128,255),pos=(167,(wiy/2)+75))
			pygame.draw.rect(screen,(255,0,0),[0,wiy/2,self.h,self.l],2)
 		        msg(screen,"MID = "+str(mids[x]),color=(0,128,255),pos=(500,(wiy/2)+75))
			pygame.draw.rect(screen,(0,255,0),[333,wiy/2,self.h,self.l],2)
        		msg(screen,"HIGHER THAN",color=(0,128,255),pos=(833,(wiy/2)+75))
			pygame.draw.rect(screen,(0,0,255),[666,wiy/2,self.h,self.l],2)

        		x+=1
		    	pygame.display.update()
		    	pygame.time.wait(3000)
		    pygame.quit()
		    quit()
                return 0
        return 1  

pygame.init()
pygame.mixer.get_init()
mutrue=load_sound("punch.wav")
mufall= load_sound("boom.wav")
clock=pygame.time.Clock()
screen=pygame.display.set_mode((wix,wiy))
pygame.display.set_caption("Search2Learn")
i=0;
mape=[]
while i < 10000:
	mape.append(randint(0,99999))
	i+=1
mape.sort()
print mape
position=randint(0,9999)
search=mape[position]
screen.fill((224,224,255))
high=len(mape)
low=0
mid=(high+low)/2
print mid
lost=0
time=0
delt=60
sb=[]
mids=[]
highs=[]
lows=[]
speey=4
score=0
flag=0
h=wix//3-1
l=wiy//5
msg(screen,"Binary Search",color=(0,0,0),size=100,pos=(-1,50)) 
msg(screen,"To search we use DIVIDE AND CONQUER in this algo ",color=(0,0,0),size=30,pos=(-1,150))
msg(screen,"and divide the the complete set into three parts ",color=(0,0,0),size=30,pos=(-1,190))
msg(screen,"based on the middle element and if the search element ",color=(0,0,0),size=30,pos=(-1,230))
msg(screen,"is GREATER THAN middle element then go towards RIGHT ",color=(0,0,0),size=30,pos=(-1,270))
msg(screen,"and if the search element is LESS THAN middle element ",color=(0,0,0),size=30,pos=(-1,310))
msg(screen,"then go towards LEFT !",color=(0,0,0),size=30,pos=(-1,350))
pygame.draw.rect(screen,(255,0,0),[0,wiy/2,h,l])
msg(screen,"Less Than",color=(0,0,0),size=50,pos=(167,450))
pygame.draw.rect(screen,(0,255,0),[333,wiy/2,h,l])
msg(screen,"Mid",color=(0,0,0),size=50,pos=(500,450))
pygame.draw.rect(screen,(0,0,255),[666,wiy/2,h,l])
msg(screen,"Higher Than",color=(0,0,0),size=50,pos=(833,450))
pygame.display.update()
pygame.time.wait(4000)
while lost == 0:
    while 1:
	print pri
	print mids
        if len(sb)>=1:
	    if sb[-1].x!=333:
		sb.append(button())
	else:
		sb.append(button())
	posi=2
	m=mape[mid]
	if len(mids)>0:
	    if mids[-1]!=m:
		mids.append(m)
		highs.append(mape[high-1])
		lows.append(mape[low])
	else:
	    mids.append(m)
            highs.append(mape[high-1])
            lows.append(mape[low])
	if search>m:
	    low=mid
	if search<m:
	    high=mid+1
	    posi=0
	if search==m:
	    posi=1
	mid=(high+low)/2
	print "high=",str(high)
	print "mid=",str(mid)
	print "low=",str(low)
        sb[-1].pos(posi)
	sb[-1].midd(mids[-1])
	if flag==1:
	    if len(mids)>pri+1:
        	pri+=1
        	flag=0
        if lost!=0 : break
        for j in range(wiy//(5*speey)):
            time+=1/delt
            clock.tick(delt)
            screen.fill((224,224,255))
            if lost!=0 : break
            for k in range(len(sb)) :
                try:
                    sb[k].y+=speey
                    sb[k].update(screen)
                    if (sb[k].y >wiy-sb[k].l and sb[k].enclick == True) : lost=1
                except : pass
            for event in pygame.event.get():
                if event.type == QUIT or \
                   (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    lost=sb[score].click(pygame.mouse.get_pos())
                    if lost==0:mutrue.play()
                    else :mufall.play()
		    if len(mids)>pri+1:
			print mids
			print "len=",
			print len(mids)
			print "pri=",
			print pri
			pri+=1
		    else:
			flag=1
                    score+=1
            msg(screen,"SCORE "+str(score),color=(0,255,0),pos=(-1,30))
	    msg(screen,"SEARCH "+str(search),color=(255,0,0),pos=(-1,100))
    	    #msg(screen,"MID = "+str(mids[pri]),color=(0,128,255),pos=((wix/2)-5,wiy/2))
	    #msg(screen,str(i),color=(0,128,255),pos=(-1,wiy-100))
            pygame.display.update()
	    pygame.time.wait(15)
    speey+=1
pygame.mixer.music.stop()
msg(screen,"YOU LOSE ",color=(110,128,225),size=100,pos=(-1,-1))
msg(screen,"SCORE "+str(score),color=(0,255,0),pos=(-1,30))
msg(screen,"Developed by Ayushi Anand and Chaitanya Nagpal",color=(110,108,225),pos=(-1,wiy//2+40))
x=0
pygame.display.update()
pygame.time.wait(4000)
pygame.quit()
quit()
