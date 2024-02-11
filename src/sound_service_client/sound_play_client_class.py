#!/usr/bin/env python3

import rospy
import time
from sound_service_client.srv import BoolString, BoolStringRequest

class SoundPlayServiceClient:
    def __init__(self):
        if not rospy.get_node_uri():
             rospy.init_node('sound_play_client')
        rospy.wait_for_service('sound_play')
        self.bool_string_service = rospy.ServiceProxy('sound_play', BoolString)

    def call_service(self, data, comment):
        try:
            request = BoolStringRequest()
            request.data = data
            request.comment = comment
            response = self.bool_string_service(request)
            return response.success
        except rospy.ServiceException as e:
            rospy.logerr("Service call failed: %s" % e)
            return False

    def sound_transition(self, comment):
        self.call_service(False, comment)

    def sound_finish(self, comment):
        self.call_service(True, comment)

    def sound_countdown(self, comment):
        self.sound_transition(f"{comment}: Count down: 3")
        time.sleep(1)
        self.sound_transition(f"{comment}: Count down: 2")
        time.sleep(1)
        self.sound_transition(f"{comment}: Count down: 1")
        time.sleep(1)
        self.sound_finish(f"{comment}: Count down: 0")



if __name__ == '__main__':
    client = SoundPlayServiceClient()
    # Example usage:
    data = True
    comment = "This is a test comment."
    success = client.call_service(data, comment)
    if success:
        rospy.loginfo("Service call succeeded!")
    else:
        rospy.loginfo("Service call failed.")
