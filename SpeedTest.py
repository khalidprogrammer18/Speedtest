# This code is a system of speedtest made by three functions 
import time # Import the timer tool

while True: 
    try:
        num_range = int(input("Write the range (must be huge number like 10000): "))
        break
    except:
        print("You should write a number")

def SpeedTest(): # Main function and the whole work of speedtest

    def work(function): # The second function

        start = time.time() # Timer starter

        function() # Starting the test by printing numbers in range one to ten thousand

        end = time.time() # Timer ender

        print(f"The test result is: {round( end - start , 3 )} second") # Printing the differance between timer starting and ending 

    return work # Return all codes in work function to be saved in SpeedTest function

@SpeedTest() # Implement the test function in SpeedTest function ( The connection between two functions )

def test(): # Important function to print 10000 number as a method to calculate the result of SpeedTest

    for number in range(1,num_range): # Loop in order to print 10000 number in row

        print(f"{number}                    ", end="\r") # Printing, \r for setting curser in the start of the line