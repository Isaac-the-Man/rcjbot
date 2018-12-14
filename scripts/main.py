#!/usr/bin/env python
import rospy
from rcjbot.msg import MotorValues

def main():
  rospy.init_node('main')
  pub = rospy.Publisher('main', MotorValues, queue_size=1)
  rate = rospy.Rate(10)

  while not rospy.is_shutdown():
    motor_values = MotorValues()
    motor_values.left_power = 0
    motor_values.right_power = 255
    pub.publish(motor_values)

  rate.sleep()

if __name__ == '__main__':
  main()
