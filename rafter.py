from serial import Serial
from time import sleep
from json5 import load


class Rafter:
    def __init__(self, port):
        self.config = load(open('config.json5'))
        self.ser = Serial(self.config['comport'], self.config['baudrate'], timeout=1)
        self.endpoints = self.config['endpoints']
        self.joints = []
        
        class Joint:
            def __init__(self, pin, mnPos, mxPos, nPos):
                self.pin = pin
                self.mnPos = mnPos
                self.mxPos = mxPos
                self.nPos = nPos

            def set_angle(self, angle):
                #self.rafter.set_angle(self.name, angle)
                pass
            
        for joint_type in self.config["joint_pins"].keys():
            for joint in range(len(self.config["joint_pins"][joint_type])):
                j = Joint(
                    self.config["joint_pins"][joint_type][joint],
                    self.config["joint_limits"][joint_type]["min"],
                    self.config["joint_limits"][joint_type]["max"],
                    self.config["joint_limits"][joint_type]["neutral"]
                )
                self.joints.append(j)

    def close(self):
        self.ser.close()