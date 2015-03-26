import zerorpc

class SpaceAPI(object):
    def __init__(self, url):
	print "SpaceAPI connecting to " + url
	self.c = zerorpc.Client()
	self.c.connect(url)

    def updateStatus(self, labOpen, topic):
	print "Setting lab open " + str(labOpen) + " and topic " + topic
	try:
		self.c.updateStatus(labOpen, topic)
	except:
        	print "Update failure"
		

