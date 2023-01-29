import cv2
import numpy as np
import pyautogui


while True:

    # x, y = pyautogui.size()
    # print("Screen resolution: {}x{}".format(x, y))

    # break

    # take screenshot
    image = pyautogui.screenshot(region=(100, 350, 255, 250))
    # convert it to numpy
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # pixel count to know if there is diffrent between whte and black
    # if any pix vlaue is less than 100 then its black
    black_pixel_no = np.sum(image < 100)
    # if any pix vlaue is less than 100 then its white
    white_pixel_no = np.sum(image > 100)

    print(black_pixel_no, 'black_pixel_no')
    print(white_pixel_no, 'white_pixel_no')

    # light mode

    if black_pixel_no > 4000 and black_pixel_no < 30000:
        pyautogui.press('up')

    # light mode

    if white_pixel_no > 4000 and white_pixel_no < 30000:
        pyautogui.press('up')

    cv2.imshow('image', image)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
