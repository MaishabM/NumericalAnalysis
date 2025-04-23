print('Car functions:\n start to Start the car\n run to Run the car \n stop to Stop the car \n quit to Quit')
ins = ""
started = False
running = False
while ins != "QUIT":
    ins = input('-> ').upper()
    if ins == 'START':
        if started:
            print('The car is already started!')
        else:
            started = True
            print('The car is started. Ready to go?\n')
    elif ins == 'RUN':
        if running:
            print('The car is already running')
        else:
            running = True
            print('The car is running**\n')
    elif ins == 'STOP':
        if not started:
            print('The car is already stopped')
        else:
            started = False
            print('The car is stopped\n')
    elif ins == 'QUIT':
        print('The program is quitting...')
    else:
        print('Wrong command. Would you like to try again?\n')