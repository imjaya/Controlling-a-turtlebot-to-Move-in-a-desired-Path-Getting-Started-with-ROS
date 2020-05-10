#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
                                                                ### Jayasurya Sevalur Mahendran, ASU ID:1217399443, MAIL ID: jsevalur@asu.edu
def move():
    # Starts a new node
    rospy.init_node('my_initials', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    speed = 2
    distance = 1.5
    vel_msg.linear.x = -1.5
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.0


    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot
    vel_msg.linear.x = -0
    velocity_publisher.publish(vel_msg)

################################################################################
    current_distance = 0
    distance = 2.0
    vel_msg.linear.x = -2.0
    #Since we are moving linearly in x axis and with an angular velocity in z axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 3.00
    t0 = rospy.Time.now().to_sec()

    while(current_distance < distance):

        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0.00
    velocity_publisher.publish(vel_msg)

################################################################################
    current_distance = 0
    distance = 1.0
    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = -1.0
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.0

    while(current_distance < distance):

        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot

    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

###############################################################################

    current_distance = 0
    distance = 2.0
    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = -2.0
    #Since we are moving linearly in x-axis and with an angular velocity in z axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -3.00

    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)


################################################################################

    current_distance = 0
    distance = 2.0
    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x =-1.0
    #Since we are moving just in x-axis
    vel_msg.linear.y = -0.0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.0

    while(current_distance < distance):
        #Publish the velocity
        velocity_publisher.publish(vel_msg)
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
        #After the loop, stops the robot
    
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
