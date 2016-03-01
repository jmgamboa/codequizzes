def lights_array(num):

    count = 0
    n = 1
    while n**2 <= num:
        n += 1
        count += 1
    return count

print(str(lights_array(100)) + ' light bulbs are on!')
