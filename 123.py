import cv2


def add_frame_all(sx1, sy1, sx2, sy2, num, img_root):
    im = cv2.imread(img_root)
    cv2.rectangle(im, (int(sx1), int(sy1)), (int(sx2), int(sy2)), (0, 255, 0), 3)
    cv2.imwrite(img_root, im)
    cv2.imshow("im", im)
    cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return


num = 1
add_frame_all(90,370,130,400,1,"./img2/9.jpg")
#add_frame_all(140, 375, 140, 405, 1, "./1.jpg")
# add_frame_all(120,255,260,370,1,"C:/Users/Acer/Desktop/1.jpg")
cv2.destroyAllWindows()