#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math
def move_straight(distance, direction, twist, pub, rate):
    twist = Twist()
    speed = 0.03 * direction
    distance_to_move = distance
    duration = distance_to_move / speed
    twist.linear.x = speed
    twist.angular.z = 0
    start_time = rospy.Time.now().to_sec()
    while not rospy.is_shutdown() and (rospy.Time.now().to_sec() - start_time) < abs(duration):
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0
    twist.angular.z = 0
    pub.publish(twist)
    
def rotate(distance, direction, twist, pub, rate):
    twist = Twist()
    speed = 0.1 * direction
    distance_to_move = distance
    duration = distance_to_move / speed
    twist.angular.z = speed
    twist.linear.x = 0
    start_time = rospy.Time.now().to_sec()
    while not rospy.is_shutdown() and (rospy.Time.now().to_sec() - start_time) < abs(duration):
        pub.publish(twist)
        rate.sleep()
    twist.angular.z = 0
    twist.linear.x = 0
    pub.publish(twist)
    
if __name__ == '__main__':
    try:
        rospy.init_node('square')
        pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(1000)
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = 0
        i = 0
        angles = [92.5,93,94.5,96]
        while not rospy.is_shutdown() and i < 4:
            move_straight(0.25, 1, twist, pub, rate)
            rospy.sleep(1)
            rotate(math.radians(angles[i]), 1, twist, pub, rate)
            rospy.sleep(1)
            i = i + 1
            rate.sleep()
    except rospy.ROSInterruptException:
        pass

