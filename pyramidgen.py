import openpyxl
import numpy as np



# Set the size of the square matrix
def genpyr(n):
    # Save the voxel data to an Excel file
    wb = openpyxl.Workbook()
    ws = wb.active
    # Set the header row
    ws.append(['x', 'y', 'z'])


    zax=0
    # Add a row for each voxel with its coordinates and color
    for c in range(n, 0, -1):
        # code block to be executed
        for i in range(n-zax):
            for j in range(n-zax):
                ws.append([j, i, zax])
        zax=zax+1


    wb.save('pyramid_voxels.xlsx')





