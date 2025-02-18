import streamlit as st
import numpy as np
import plotly.graph_objects as go
from utils import (
    calculate_round_bar, calculate_square_bar, calculate_flat_bar,
    calculate_weight, calculate_price, mm_to_inch, inch_to_mm,
    calculate_round_dimension_from_weight,
    calculate_square_dimension_from_weight,
    calculate_flat_dimension_from_weight
)

st.set_page_config(
    page_title="Steel Bar Calculator",
    page_icon="🔧",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        text-align: right;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("Steel Bar Calculator")
st.markdown("Calculate dimensions, surface area, volume, weight, and price for different types of steel bars.")

# Create two columns for input and output
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader("Input Parameters")

    # Calculation mode
    calc_mode = st.radio(
        "Calculation Mode",
        ["Dimensions to Weight", "Weight to Dimensions"],
        horizontal=True
    )

    # Bar type selection
    bar_type = st.selectbox(
        "Select Bar Type",
        ["Round Bar", "Square Bar", "Flat Bar"],
        help="Choose the type of steel bar you want to calculate"
    )

    # Unit selection
    unit = st.radio("Select Unit", ["mm", "inch"], horizontal=True)

    # Material properties
    density = st.number_input(
        "Material Density (g/cm³)",
        min_value=0.1,
        value=7.85,  # Default steel density
        step=0.01,
        format="%.3f",
        help="Standard steel density is 7.85 g/cm³"
    )

    price_per_kg = st.number_input(
        "Price per kg (Rs.)",
        min_value=0.0,
        value=100.0,
        step=0.1,
        format="%.2f"
    )

    if calc_mode == "Dimensions to Weight":
        # Input fields based on bar type
        if bar_type == "Round Bar":
            diameter = st.number_input(
                f"Diameter ({unit})",
                min_value=0.1,
                value=10.0,
                step=0.1,
                format="%.2f"
            )
            length = st.number_input(
                f"Length ({unit})",
                min_value=0.1,
                value=100.0,
                step=0.1,
                format="%.2f"
            )
            surface_area, volume = calculate_round_bar(diameter, length, unit)

        elif bar_type == "Square Bar":
            side = st.number_input(
                f"Side ({unit})",
                min_value=0.1,
                value=10.0,
                step=0.1,
                format="%.2f"
            )
            length = st.number_input(
                f"Length ({unit})",
                min_value=0.1,
                value=100.0,
                step=0.1,
                format="%.2f"
            )
            surface_area, volume = calculate_square_bar(side, length, unit)

        else:  # Flat Bar
            width = st.number_input(
                f"Width ({unit})",
                min_value=0.1,
                value=20.0,
                step=0.1,
                format="%.2f"
            )
            thickness = st.number_input(
                f"Thickness ({unit})",
                min_value=0.1,
                value=10.0,
                step=0.1,
                format="%.2f"
            )
            length = st.number_input(
                f"Length ({unit})",
                min_value=0.1,
                value=100.0,
                step=0.1,
                format="%.2f"
            )
            surface_area, volume = calculate_flat_bar(width, thickness, length, unit)

    else:  # Weight to Dimensions mode
        target_weight = st.number_input(
            "Target Weight (kg)",
            min_value=0.1,
            value=1.0,
            step=0.1,
            format="%.3f"
        )

        length = st.number_input(
            f"Length ({unit})",
            min_value=0.1,
            value=100.0,
            step=0.1,
            format="%.2f"
        )

        if bar_type == "Round Bar":
            diameter = calculate_round_dimension_from_weight(target_weight, length, density, unit)
            surface_area, volume = calculate_round_bar(diameter, length, unit)
            st.info(f"Required diameter: {diameter:.2f} {unit}")

        elif bar_type == "Square Bar":
            side = calculate_square_dimension_from_weight(target_weight, length, density, unit)
            surface_area, volume = calculate_square_bar(side, length, unit)
            st.info(f"Required side length: {side:.2f} {unit}")

        else:  # Flat Bar
            width = st.number_input(
                f"Width ({unit})",
                min_value=0.1,
                value=20.0,
                step=0.1,
                format="%.2f"
            )
            thickness = calculate_flat_dimension_from_weight(target_weight, length, width, density, unit)
            surface_area, volume = calculate_flat_bar(width, thickness, length, unit)
            st.info(f"Required thickness: {thickness:.2f} {unit}")

# Calculate weight and price
weight = calculate_weight(volume, density)
total_price = calculate_price(weight, price_per_kg)

# Display results
with col2:
    st.subheader("Results")

    # Create metrics for results
    st.metric(
        "Surface Area",
        f"{surface_area/1000:.2f} cm² ({surface_area/645.16:.2f} sq. inch)"
    )

    st.metric(
        "Volume",
        f"{volume/1000:.2f} cm³ ({volume/16387.064:.2f} cubic inch)"
    )

    st.metric(
        "Weight",
        f"{weight:.2f} kg ({weight*2.20462:.2f} lbs)"
    )

    st.metric(
        "Total Price",
        f"Rs. {total_price:.2f}"
    )

    # Visual representation
    if bar_type == "Round Bar":
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=[0, 100],
            y=[50, 50],
            mode='lines',
            line=dict(color='blue', width=10),
            name='Round Bar'
        ))
    elif bar_type == "Square Bar":
        fig = go.Figure(data=[
            go.Scatter(
                x=[0, 100, 100, 0, 0],
                y=[0, 0, 100, 100, 0],
                fill="toself",
                mode='lines',
                line=dict(color='blue'),
                name='Square Bar'
            )
        ])
    else:
        fig = go.Figure(data=[
            go.Scatter(
                x=[0, 100, 100, 0, 0],
                y=[0, 0, 20, 20, 0],
                fill="toself",
                mode='lines',
                line=dict(color='blue'),
                name='Flat Bar'
            )
        ])

    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        height=200,
        width=300
    )
    st.plotly_chart(fig)

# Add information about the calculator
st.markdown("""
---
### How to use this calculator:

#### Dimensions to Weight Mode:
1. Select the type of bar (Round, Square, or Flat)
2. Choose your preferred unit of measurement (mm or inch)
3. Enter the dimensions of the bar
4. Specify the material density (default is steel at 7.85 g/cm³)
5. Enter the price per kg
6. Results will update automatically in real-time

#### Weight to Dimensions Mode:
1. Select the type of bar
2. Enter the target weight in kg
3. Specify the length and any other required dimensions
4. The calculator will determine the missing dimension needed to achieve the target weight
""")