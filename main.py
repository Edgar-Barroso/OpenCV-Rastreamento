import cv2

#rastreador = cv2.legacy.TrackerKCF_create() #processamento mais rapido
rastreador = cv2.legacy.TrackerCSRT_create()#processamento mais lento porem melhor

video = cv2.VideoCapture('street.mp4')

ok,frame = video.read()

bbox = cv2.selectROI(frame)

ok = rastreador.init(frame,bbox)

while True:
    ok,frame = video.read()
    if not ok :
        break
    
    ok,bbox = rastreador.update(frame)
    x,y,w,h = [int(c) for c in bbox]
    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2,1)
    cv2.imshow('rastreamento',frame)
    
    if cv2.waitKey(1) & 0XFF == 27:#esq
        break