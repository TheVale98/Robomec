

HOST = "localhost"
PORT = 4223
UID = "67QG3v" # Change XXYYZZ to the UID of your Silent Stepper Brick

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_silent_stepper import BrickSilentStepper

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    ss = BrickSilentStepper(UID, ipcon) # Create device object

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    ss.set_motor_current(800) # 800mA
    ss.set_step_configuration(ss.STEP_RESOLUTION_16, True) # 1/8 steps (interpolated)
    
    # Slow acceleration (500 steps/s^2),
    # Fast deacceleration (5000 steps/s^2)
    ss.set_max_velocity(4000)
    ss.set_speed_ramping(4000, 4000)
    

    ss.enable() # Enable motor power
    ss.drive_backward()
    ss.set_steps(3000) 


    import time
    time.sleep(10)
    ss.disable()
    ipcon.disconnect()