"""
OpenFOAM 2D Cylindrical Thermal Case Generator
Author: Abhishek Singh (ORCID: 0009-0004-6913-096X)
"""
import os

def generate_openfoam_case():
    os.makedirs("openfoam_case/system", exist_ok=True)
    os.makedirs("openfoam_case/constant", exist_ok=True)
    os.makedirs("openfoam_case/0", exist_ok=True)
    
    with open("openfoam_case/system/controlDict", "w") as f:
        f.write("""/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2206                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile { version 2.0; format ascii; class dictionary; location "system"; object controlDict; }

application     laplacianFoam;
startFrom       startTime;
startTime       0;
stopAt          endTime;
endTime         0.01;
deltaT          1e-5;
writeControl    timeStep;
writeInterval   100;
""")
    print("OpenFOAM case hierarchy created successfully.")

if __name__ == "__main__":
    generate_openfoam_case()
