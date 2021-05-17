#!/usr/bin/env python3
# This program creates a listner node which subscribes to the topic /random and prints "True" if 
# the value obtained in random is greater than 0.5
# Author: Mijaz Mukundan
#This code is written to test ROS installation

import rospy
from std_msgs.msg import Float32

def callback(msg):
    if msg.data > 0.5:
        print("True")
    else:
        print("False")

def listner():
    # A node must have a unique name, if a new node starts with the same name the previous one 
    # goes poof, the anonymous flag will cause ros to choose a unique name
    rospy.init_node('listner', anonymous=True)
    
    # Callback function is called whenever it reads a message from the topic
    rospy.Subscriber(name = '/random',data_class=Float32,callback = callback,queue_size=1)
    
    #Keeps the program running until the node is terminated
    rospy.spin()

if __name__=='__main__':
    listner()
