import numpy as np

def mm_to_inch(mm):
    return mm / 25.4

def inch_to_mm(inch):
    return inch * 25.4

def calculate_round_bar(diameter, length, unit='mm'):
    if unit == 'inch':
        diameter = inch_to_mm(diameter)
        length = inch_to_mm(length)

    radius = diameter / 2
    surface_area = np.pi * diameter * length + 2 * np.pi * (radius ** 2)
    volume = np.pi * (radius ** 2) * length

    return surface_area, volume

def calculate_square_bar(side, length, unit='mm'):
    if unit == 'inch':
        side = inch_to_mm(side)
        length = inch_to_mm(length)

    surface_area = 4 * side * length + 2 * (side ** 2)
    volume = side * side * length

    return surface_area, volume

def calculate_flat_bar(width, thickness, length, unit='mm'):
    if unit == 'inch':
        width = inch_to_mm(width)
        thickness = inch_to_mm(thickness)
        length = inch_to_mm(length)

    surface_area = 2 * (width * length + thickness * length + width * thickness)
    volume = width * thickness * length

    return surface_area, volume

def calculate_weight(volume, density):
    # Convert volume from mm³ to cm³
    volume_cm3 = volume / 1000
    # Calculate weight in grams
    weight_g = volume_cm3 * density
    # Convert to kg
    weight_kg = weight_g / 1000
    return weight_kg

def calculate_price(weight_kg, price_per_kg):
    return weight_kg * price_per_kg

def calculate_round_dimension_from_weight(weight_kg, length, density, unit='mm'):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate diameter using the volume formula: V = πr²L
    radius = np.sqrt(volume / (np.pi * length))
    diameter = 2 * radius

    if unit == 'inch':
        diameter = mm_to_inch(diameter)
        length = mm_to_inch(length)

    return diameter

def calculate_square_dimension_from_weight(weight_kg, length, density, unit='mm'):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate side using the volume formula: V = s²L
    side = np.sqrt(volume / length)

    if unit == 'inch':
        side = mm_to_inch(side)
        length = mm_to_inch(length)

    return side

def calculate_flat_dimension_from_weight(weight_kg, length, width, density, unit='mm'):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate thickness using the volume formula: V = w*t*L
    thickness = volume / (width * length)

    if unit == 'inch':
        thickness = mm_to_inch(thickness)
        width = mm_to_inch(width)
        length = mm_to_inch(length)

    return thickness