import numpy as np
import cv2


def main():
	# Use Integrated webcam
	cap = cv2.VideoCapture(0)

	while True:
		# Get single frame
		ret, frame = cap.read()
		
		# Make gray-scale of frame
		# All algorithms use this format of image
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Show frame
		cv2.imshow('Source frame', frame)
		cv2.imshow('Gray-scale', gray)
		
		# Exit by pressing "q"
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	cap.release()
	cv2.destroyAllWindows()

# Run main if script running from command line
if( __name__ == "__main__"):
	main()

