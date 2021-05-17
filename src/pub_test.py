#!/usr/bin/env python3
# This code creates a publisher node which publishes a random number between 0 and 1 to the
# topic /random.
# Author: Mijaz Mukundan
# This code was written to test ROS installation

import rospy
from std_msgs.msg import Float32

import random

def talker():
    # A node must have a unique name, if a new node starts with the same name the previous one 
    # goes poof, the anonymous flag will cause ros to choose a unique name
    rospy.init_node('talker', anonymous=True)

    # Defining which topic would it publish to
    pub = rospy.Publisher(name = '/random', data_class = Float32, queue_size=1)

    # An update rate of 10Hz
    r = rospy.Rate(1)

    while not rospy.is_shutdown():
        rand_num = Float32()
        rand_num.data = random.random() #Create a random number
        pub.publish(rand_num) # Publish the random number

        r.sleep()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
