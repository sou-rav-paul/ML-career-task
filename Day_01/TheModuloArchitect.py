'''Goal : Input a raw number of seconds (e.g. 3665). Use Integer Division // and Modulo % to calculate exactly how many Hours, Minutes and Seconds this represents.

'''
seconds = int(input("Enter seconds :"))

hours=seconds//3600
remaining_seconds=seconds % 3600
minutes=remaining_seconds//60
actual_seconds=remaining_seconds % 60
print(f'You Entered {hours} hours , {minutes} minutes , {actual_seconds} seconds')