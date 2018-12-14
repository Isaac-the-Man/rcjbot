#!/usr/bin/env python
import rospy, unittest, rostest
import rosnode
import time

# the test class for main
class MainTest(unittest.TestCase):
	def test_node_exist(self):
		nodes = rosnode.get_node_names()
		self.assertIn('/main', nodes, '\'main\' node does not exists')

if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node('test_main')
	rostest.rosrun('rcjbot', 'test_main',MainTest)
