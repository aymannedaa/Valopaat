# a function for scaling 0...1 to 0...255 which corresponds the brightness of the light
def brightness(input_value):
    return (1/255) * input_value