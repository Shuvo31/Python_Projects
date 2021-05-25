import cv2
import numpy as np
from PIL import ImageGrab
def screen():
    fourcc=cv2.VideoWriter_fourcc(*"XVID")
    output=cv2.VideoWriter("Output.avi",fourcc,5.0,(1920,1080))
    while True:
        img=ImageGrab.grab()
        img_np=np.array(img)
        frame=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recoder",frame)
        output.write(frame)
        if cv2.waitKey(1)==27:
            break
    output.release()
    cv2.destroyAllWindows()
screen()

