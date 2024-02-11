#!/usr/bin/env python3
import rospy
import rospkg
import pygame
from pygame.locals import *
from std_srvs.srv import *
from std_msgs.msg import Header
from std_msgs.msg import Int16
from sound_service_client.msg import Int16StringStamped
from sound_service_client.srv import BoolString, BoolStringResponse
#from beginner_tutorials.srv import *


rospack = rospkg.RosPack()

pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 1024)
sound_normal = pygame.mixer.Sound(rospack.get_path("sound_service_client") + "/wav/chu1.wav")
sound_special = pygame.mixer.Sound(rospack.get_path("sound_service_client") + "/wav/tm2r_shoot15.wav")


class sound_player:
        sound_num = 0
        success = False
        message = ""
        p_val = Int16StringStamped()

        def __init__(self):
                self.sound_num = 0
                self.p = rospy.Publisher('sound_publisher', Int16StringStamped, queue_size=20)
                self.s = rospy.Service('sound_play', BoolString, self.handle_sound_play)

        def handle_sound_play(self, req):
                self.p_val.header = Header()
                self.p_val.header.stamp = rospy.Time.now()


                if req.data == True:
                        self.p_val.data = 1
                        self.p_val.comment = req.comment
                        sound_special.play()
                        self.p.publish(self.p_val)
                elif req.data == False:
                        self.p_val.data = 0
                        self.p_val.comment = req.comment
                        sound_normal.play()
                        self.p.publish(self.p_val)
                self.success = True
                self.message = "PLAY SOUND"

                # return SetBoolResponse(self.success, self.message)
                return BoolStringResponse(self.success)

def sound_play_server():
        rospy.init_node('sound_play_server')
        sp = sound_player()
        print("Ready to play sound.")
        rospy.spin()

if __name__ == "__main__":
        sound_play_server()
