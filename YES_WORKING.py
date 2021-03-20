import cv2
import os
import sys


def cropp_video (name_video, max_frames_for_model):

    # Playing video from file:
    print(name_video)
    cap = cv2.VideoCapture(name_video)  ##ТУТ БУДЕТ ТВОЙ ВИДОС
    DOC_FOR_PHOTOS = name_video.split('.')[0]
    try:
        if not os.path.exists(DOC_FOR_PHOTOS+'_'+max_frames_for_model):
            os.makedirs(DOC_FOR_PHOTOS+'_'+max_frames_for_model)
    except OSError:
        print('Error: Creating directory of data')

    count_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    currentFrame = 0
    for item in range(count_frames):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if currentFrame % int(count_frames/int(max_frames_for_model))  == 0:
            # Saves image of the current frame in jpg file
            name = './' + DOC_FOR_PHOTOS+'_'+max_frames_for_model + '/frame' + str(currentFrame) + '.png'
            print(name)
            cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    params = []
    for param in sys.argv:
        params.append(param)
    if len(params) == 2:
        cropp_video(params[1], 1)
    elif len(params) == 3:
        cropp_video(params[1],params[2])
