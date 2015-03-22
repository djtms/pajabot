#!/usr/bin/python
import zerorpc
import os
import re

class SpaceAPI(object):
    def updateStatus(self, labOpen, topic):
	# Clean up to avoid massive security hole, if firewall fails
	labOpenCleaned = re.sub(r'[^a-zA-Z0-9]',' ', labOpen)
	print "Set lab open " + str(labOpenCleaned) + " and topic " + topic
	os.system("~/updatestatus.sh " + str(labOpenCleaned) + " Foo")
        return "Update ok"

s = zerorpc.Server(SpaceAPI())
s.bind("tcp://0.0.0.0:4242")
s.run()

