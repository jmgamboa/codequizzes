def lights_array(num):
    arr = []
    light = 0 # off light
    count = 0
    while count < num:
        arr.append(light) #add off lights to empty array
        count += 1
    return arr #return array of lights off - 0 is off

def switch_lights(num):
    arr = lights_array(num) #get array of light starting off
    count = 1
    while count <= num: #start swicthing a every pass until the limit num
        for index, value in enumerate(arr):
            if (index + 1) % count == 0: #if index is divisible by count(pass #)
                if value == 0:
                    arr[index] = 1 #turn light on
                else:
                    arr[index] = 0 #turn light off

        count += 1

    return arr #return arrays of lights switched

def get_lights_on(num):
    arr = switch_lights(num) #get array of lights switched
    count = 0
    for item in arr: #count the # of lights on
        if item == 1:
            count += 1

    return count #return sum of lights on

print(switch_lights(100)) #print switched lights array for visual purposes
print(str(get_lights_on(100)) + ' light bulbs are on') #print results



"""
Quick solution

There is a pattern if you write out, numbers that are perfect squares have the
lights on

"""
# def lights_array(num):
#
#     count = 0
#     n = 1
#     while n**2 <= num:
#         n += 1
#         count += 1
#     return count
#
# print(str(lights_array(100)) + ' light bulbs are on!')
