class ambulance:
    """Priortiy= 0 if there is no patient in the ambulence and 1 if there is

    speed= maximum speed of the ambulance

    capacity= number of patients inside the ambulance"""
    #def __init__(object,priority,speed,capacity):
        #object.priority = priority
        #object.speed = speed
        #object.capacity = capacity

ambulance1 = ambulance()
ambulance1.priority = 1
ambulance1.speed = 15
ambulance1.capacity = 4

def cv(object):
    controlled_velocity = -10 *(1-object.priority) + 2.37*(object.speed/10)**3.98 + 30*(object.capacity+1.2)
    print (controlled_velocity)

cv(ambulance1)
