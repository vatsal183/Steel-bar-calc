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
    cross_section_area = np.pi * (radius ** 2)
    volume = cross_section_area * length

    return cross_section_area, volume

def calculate_square_bar(side, length, unit='mm'):
    if unit == 'inch':
        side = inch_to_mm(side)
        length = inch_to_mm(length)

    cross_section_area = side * side
    volume = cross_section_area * length

    return cross_section_area, volume

def calculate_flat_bar(width, thickness, length, unit='mm'):
    if unit == 'inch':
        width = inch_to_mm(width)
        thickness = inch_to_mm(thickness)
        length = inch_to_mm(length)

    cross_section_area = width * thickness
    volume = cross_section_area * length

    return cross_section_area, volume

def calculate_weight(volume, density):
    # Convert volume from mm³ to cm³
    volume_cm3 = volume / 1000
    # Calculate weight in grams
    weight_g = volume_cm3 * density
    # Convert to kg
    weight_kg = weight_g / 1000
    return weight_kg

def calculate_price_per_kg(weight_kg, price_per_kg):
    return weight_kg * price_per_kg

def calculate_price_per_sq_inch(area_mm2, price_per_sq_inch):
    # Convert area from mm² to sq inch
    area_sq_inch = area_mm2 / 645.16
    return area_sq_inch * price_per_sq_inch

def calculate_round_dimension_from_weight(weight_kg, length, density):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate diameter using the volume formula: V = πr²L
    radius = np.sqrt(volume / (np.pi * length))
    diameter = 2 * radius
    return diameter

def calculate_round_length_from_weight(weight_kg, diameter, density):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate length using volume formula: V = πr²L
    radius = diameter / 2
    length = volume / (np.pi * radius * radius)
    return length

def calculate_square_dimension_from_weight(weight_kg, length, density):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate side using the volume formula: V = s²L
    side = np.sqrt(volume / length)
    return side

def calculate_square_length_from_weight(weight_kg, side, density):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate length using volume formula: V = s²L
    length = volume / (side * side)
    return length

def calculate_flat_thickness_from_weight(weight_kg, length, width, density):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate thickness using volume formula: V = w*t*L
    thickness = volume / (width * length)
    return thickness

def calculate_flat_length_from_weight(weight_kg, width, thickness, density):
    # Convert weight to volume in mm³
    volume = (weight_kg * 1000000) / density
    # Calculate length using volume formula: V = w*t*L
    length = volume / (width * thickness)
    return length