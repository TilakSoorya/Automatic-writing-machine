# import serial
# arduino = serial.Serial('COM7', 9600)
# arduino.close()
# arduino.open()
# message = "Hello, Arduino!"
# arduino.write(message.encode())
# arduino.close()


import serial

port = "COM7" # Replace with the appropriate port
baud_rate = 9600  # Must match the baud rate in your Arduino sketch

arduino = serial.Serial(port, baud_rate)
command = 'L'  # Replace with the appropriate command character for left
arduino.write(command.encode())  # Send the command as a byte array
arduino.close()

