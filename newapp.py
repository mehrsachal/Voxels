import pandas as pd
import numpy as np

def excel_to_arrays(file_name):
    # Read the Excel file using Pandas
    data = pd.read_excel(file_name)

    # Extract the required columns
    easting = data['Easting'].to_numpy()
    northing = data['Northing'].to_numpy()
    elevation = data['Elevation'].to_numpy()
    size_x = data['SizeX'].to_numpy()
    size_y = data['SizeY'].to_numpy()
    size_z = data['SizeZ'].to_numpy()

    # Create an array of coordinates
    coordinates = np.column_stack((easting, northing, elevation))

    # Create an array of sizes
    sizes = np.column_stack((size_x, size_y, size_z))

    # Return the arrays
    return coordinates, sizes
