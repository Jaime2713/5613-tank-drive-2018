#!/usr/bin/env python3
'''
    This is a demo program showing the use of the RobotDrive class,
    specifically it contains the code necessary to operate a robot with
    tank drive.
'''

import wpilib
from wpilib.drive import DifferentialDrive


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        '''Robot initialization function'''

        # object that handles basic drive operations
        self.frontLeftMotor = wpilib.Spark(0)
        self.rearLeftMotor = wpilib.Spark(1)
        self.frontRightMotor = wpilib.Spark(2)
        self.rearRightMotor = wpilib.Spark(3)

        self.left = wpilib.SpeedControllerGroup(self.frontLeftMotor, self.rearLeftMotor)
        self.right = wpilib.SpeedControllerGroup(self.frontRightMotor, self.rearRightMotor)

        self.myRobot = DifferentialDrive(self.left, self.right)
        self.myRobot.setExpiration(1.0)

        # joysticks 1 & 2 on the driver station
        self.leftStick = wpilib.Joystick(0)
        self.rightStick = wpilib.Joystick(1)

    def teleopInit(self):
        '''Executed at the start of teleop mode'''
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        '''Runs the motors with tank steering'''
        # self.myRobot.tankDrive(self.leftStick.getY() * -1, self.rightStick.getY() * -1)
        self.myRobot.tankDrive(0.2, 0.2, False)

if __name__ == '__main__':
    wpilib.run(MyRobot)
