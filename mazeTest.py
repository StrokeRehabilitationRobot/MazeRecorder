from UDP.UDP import UDP
import math
from Main import Robot
from Main import PlotArm
from Dynamics import Dynamics
import numpy as np
from Haptic_Controller import GravityCompensationController
from Main import helper
import csv
import datetime
import time
import Maze


robot = Robot.Robot("arm1",id=0)
#ploter = PlotArm.PlotArm()

VEL_CONTROL = 48
VEL_TARGET = 42
PID_CONTROL = 37
PID_CONFIG = 65
REC_LENGTH = 25

udp = UDP(9876)
baseConstants = [0.001, 0.0002, 0.01]
shoulderConstants = [0.002, 0.00025, 0.01]
elbowConstants = [0.002, 0.0004, 0.01]

maze = Maze.App()

packet = 15*[0.0]

pidConstants = [0.001, 0.0005, .01, .001, .0005, .01, 0.002, 0.0004, 0.01, 0, 0, 0, 0, 0, 0];
udp.send_packet(0,PID_CONFIG, pidConstants)
Kv = np.matrix([[.5, 0, 0], [0, -5, 0], [0, 0, -1]])
Kl = np.matrix([[1, 0, 0], [0, -10, 0], [0, 0, -50]])
#controller = GravityCompensationController.GravityCompensationController(Kl, Kv)

#Get trial info from user
print("Setting up recording file...")
#name = raw_input("Participant's first name\n")
#task = raw_input("Task name (no spaces):\n")
#hand = raw_input("Dominant Hand (DH) or Non-Dominant Hand (NH)?")
# Set up recording file
#filename = datetime.datetime.now().strftime("recordings/" + name +
                                            #"_" + task + "_" + hand + "_%j_%H%M.csv")
#myFile = open(filename, 'w+')
#recorder = csv.writer(myFile)

raw_input("Press Enter to Begin Recording")
start_time = time.time()
print("Starting at " + str(start_time) + " and recording for " + str(REC_LENGTH) + " seconds")
end_time = start_time + REC_LENGTH
maze.on_init()
while(time.time() < end_time):

    #u = controller.getTorque(robot)
    packet[0] = helper.angle_to_encoder(0)
    packet[3] = helper.angle_to_encoder(0.25*math.pi)
    packet[6] = helper.angle_to_encoder(0)
    upstream = udp.send_packet(0, 37, packet)
    robot.update(upstream)
    #print robot.q
    data_to_record = Dynamics.fk(robot)
    #print data_to_record
    # recorder.writerow(data_to_record[2])
    #ploter.update(*Dynamics.fk(robot))
    maze.arm_pos(data_to_record[2][1], data_to_record[2][0])
    maze.on_loop()
    maze.on_render()
    #print robot.q

maze.on_cleanup()
print("Recording complete")




