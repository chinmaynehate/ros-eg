#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_straight(distance, direction, twist, pub, rate):
    speed = 0.05 * direction
    distance_to_move = distance
    duration = distance_to_move / speed
    twist.linear.x = speed
    start_time = rospy.Time.now().to_sec()
    while not rospy.is_shutdown() and (rospy.Time.now().to_sec() - start_time) <abs(duration):
        pub.publish(twist)
        rate.sleep()
    twist.linear.x = 0
    pub.publish(twist)
def rotate(distance, direction, twist, pub, rate):
    speed = 0.05 * direction
    distance_to_move = distance
    duration = distance_to_move / speed
    twist.angular.z = speed
    start_time = rospy.Time.now().to_sec()
    while not rospy.is_shutdown() and (rospy.Time.now().to_sec() - start_time) < abs(duration):
        pub.publish(twist)
        rate.sleep()
    twist.angular.z = 0
    pub.publish(twist)
if __name__ == '__main__':
    try:
        rospy.init_node('square')
        pub=rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        rate = rospy.Rate(10)
        twist = Twist()
        counter = 0
        while not rospy.is_shutdown() and counter < 4:
            move_straight(0.5, 1, twist, pub, rate)
            rospy.sleep(1)
            rotate(1.571, 1, twist, pub, rate)
            rospy.sleep(1)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass