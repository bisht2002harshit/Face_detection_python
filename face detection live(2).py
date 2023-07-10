import cv2
video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default")
while(True):
	ret, image = video_capture.read()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30, 30))
	print("Found {0} faces!".format(len(faces)))
	
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow('Face found', image)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture()
cv2.destroyAllWindows()