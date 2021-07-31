import cv2
import os

cv2.waitKey(3000)

def camera(mirror=False):
    
    cam = cv2.VideoCapture(0)
    
    while True:
        
        ret_val, img = cam.read()
        
        if mirror: 
            img = cv2.flip(img, 1)
            
        cv2.imshow('camera', img)
        
        # ESC -> 28
        # p -> 112
        if cv2.waitKey(1) == 112: 
            cv2.imwrite("images/number{}.png".format( len( os.listdir("images") ) ) , img)
        elif cv2.waitKey(1) == 27: 
            break
        
    cv2.destroyAllWindows()


def main():
    camera(mirror=True)


if __name__ == '__main__':
    main()