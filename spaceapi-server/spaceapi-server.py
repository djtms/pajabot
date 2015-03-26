#!/usr/bin/python
import zerorpc
import os

class SpaceAPI(object):
    def updateStatus(self, labOpen, topic):
	print "Set lab open " + str(labOpen) + " and topic " + topic
	os.system("~/updatestatus.sh " + str(labOpen) + " Foo")
        return "Update ok"

s = zerorpc.Server(SpaceAPI())
s.bind("tcp://0.0.0.0:4242")
s.run()

