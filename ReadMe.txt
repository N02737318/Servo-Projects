This project has several parts:

Easiest:
Design a basic boom which is compatible with our servos clip and some sort of clip for the camera itself
which we can super glue on the servos. This way we can avoid gluing the camera itself since only the clip will be glued on

Harder:
-Control a servos successfully from a python script
-Create a functioning html interface with buttons and a GUI with arrow controlled capabilities
	-have the client's html page successfully interact with a socket which will interact
	with a server and load javascript functions correctly
	-Have the server correctly return the state of the servos in terms of degrees
	-have buttons allow a screen shot to be taken, or to zoom in and out
-Create a constant live stream of the camera

Bonus:
Have face recognition capabilities using open source face recognition libraries and neural networks