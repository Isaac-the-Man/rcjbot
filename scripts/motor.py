#!/usr/bin/env python
import rospy
from rcjbot.msg import MotorValues

class Motor():
  def __init__(self):
    self.sub_main = rospy.Subscriber('main', MotorValues, self.call_back_motor_values)

  def call_back_motor_values(self, msg):
    left_p = msg.left_power
    right_p = msg.right_power
    rospy.loginfo('left_power: {}'.format(left_p))
    rospy.loginfo('right_power: {}'.format(right_p))


if __name__ == '__main__':
  rospy.init_node('motor')
  motor = Motor()
  rate = rospy.Rate(10)
  rospy.spin()
