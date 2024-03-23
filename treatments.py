#!/usr/bin/python3
#
# This file is part of the GPM phenotyping scripts.
#
# Copyright (c) 2023 Jason Toney
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Define treatment maps for fungicides in a 96-well plate."""

# This is dumb, find a better way to handle older plate maps
OLD_MAPS = False
# Definitions of treatments
CNTL = "Control"
SHAM = "SHAM 100 ug/mL"
AZX1 = "Azoxystrobin 10 ug/mL"
BOS1 = "Boscalid 1 ug/mL"
BOS2 = "Boscalid 10 ug/mL"
BOS3 = "Boscalid 100 ug/mL"
DFC1 = "Difenoconazole 25 ug/mL"
DFC2 = "Difenoconazole 250 ug/mL"
DFC3 = "Difenoconazole 2500 ug/mL"
FLU1 = "Fluopyram 1 ug/mL"
FLU2 = "Fluopyram 10 ug/mL"
FLU3 = "Fluopyram 100 ug/mL"
FTF1 = "Flutriafol 25 ug/mL"
FTF2 = "Flutriafol 250 ug/mL"
FTF3 = "Flutriafol 2500 ug/mL"
MCB1 = "Myclobutanil 25 ug/mL"
MCB2 = "Myclobutanil 250 ug/mL"
MCB3 = "Myclobutanil 2500 ug/mL"
MDS1 = "Mandestrobin 10 ug/mL"
PYL1 = "Pyraclostrobin 10 ug/mL"
if OLD_MAPS:
    QXF1 = "Quinoxyfen 0.01 ug/mL"
    QXF2 = "Quinoxyfen 0.1 ug/mL"
    QXF3 = "Quinoxyfen 1 ug/mL"
else:
    QXF1 = "Quinoxyfen 0.001 ug/mL"
    QXF2 = "Quinoxyfen 0.01 ug/mL"
    QXF3 = "Quinoxyfen 0.1 ug/mL"
    QXF4 = "Quinoxyfen 1 ug/mL"
    QXF5 = "Quinoxyfen 10 ug/mL"
    QXF6 = "Quinoxyfen 100 ug/mL"
TEB1 = "Tebuconazole 25 ug/mL"
TEB2 = "Tebuconazole 250 ug/mL"
TEB3 = "Tebuconazole 2500 ug/mL"
TFX1 = "Trifloxystrobin 10 ug/mL"


# maps of treatment blocks
def get_treatments(plate, block):
    """Returns the treatment in its corresponding well."""
    # Handle batches, eg. plate1a-1, plate1a-2, ...
    plate = plate.split("-")[0]
    if plate == "plate1a":
        treatments = [
            CNTL, AZX1, BOS2, FLU1, FLU3, DFC2, FTF1, FTF3, MCB2, TEB1, TEB3, QXF2,
            CNTL, AZX1, BOS2, FLU1, FLU3, DFC2, FTF1, FTF3, MCB2, TEB1, TEB3, QXF2,
            CNTL, AZX1, BOS2, FLU1, FLU3, DFC2, FTF1, FTF3, MCB2, TEB1, TEB3, QXF2,
            CNTL, AZX1, BOS2, FLU1, FLU3, DFC2, FTF1, FTF3, MCB2, TEB1, TEB3, QXF2,
            SHAM, BOS1, BOS3, FLU2, DFC1, DFC3, FTF2, MCB1, MCB3, TEB2, QXF1, QXF3,
            SHAM, BOS1, BOS3, FLU2, DFC1, DFC3, FTF2, MCB1, MCB3, TEB2, QXF1, QXF3,
            SHAM, BOS1, BOS3, FLU2, DFC1, DFC3, FTF2, MCB1, MCB3, TEB2, QXF1, QXF3,
            SHAM, BOS1, BOS3, FLU2, DFC1, DFC3, FTF2, MCB1, MCB3, TEB2, QXF1, QXF3,
        ]
    elif plate == "plate1b":
        treatments = [
            TEB1, TEB3, SHAM, FTF1, FTF3, QXF2, BOS1, BOS3, DFC2, FLU1, FLU3, MCB2,
            TEB1, TEB3, SHAM, FTF1, FTF3, QXF2, BOS1, BOS3, DFC2, FLU1, FLU3, MCB2,
            TEB1, TEB3, SHAM, FTF1, FTF3, QXF2, BOS1, BOS3, DFC2, FLU1, FLU3, MCB2,
            TEB1, TEB3, SHAM, FTF1, FTF3, QXF2, BOS1, BOS3, DFC2, FLU1, FLU3, MCB2,
            TEB2, CNTL, AZX1, FTF2, QXF1, QXF3, BOS2, DFC1, DFC3, FLU2, MCB1, MCB3,
            TEB2, CNTL, AZX1, FTF2, QXF1, QXF3, BOS2, DFC1, DFC3, FLU2, MCB1, MCB3,
            TEB2, CNTL, AZX1, FTF2, QXF1, QXF3, BOS2, DFC1, DFC3, FLU2, MCB1, MCB3,
            TEB2, CNTL, AZX1, FTF2, QXF1, QXF3, BOS2, DFC1, DFC3, FLU2, MCB1, MCB3,
        ]
    elif plate == "plate2a":
        treatments = [
            TEB1, TEB3, MCB2, QXF1, QXF3, DFC2, BOS1, BOS3, FTF2, FLU1, FLU3, SHAM,
            TEB1, TEB3, MCB2, QXF1, QXF3, DFC2, BOS1, BOS3, FTF2, FLU1, FLU3, SHAM,
            TEB1, TEB3, MCB2, QXF1, QXF3, DFC2, BOS1, BOS3, FTF2, FLU1, FLU3, SHAM,
            TEB1, TEB3, MCB2, QXF1, QXF3, DFC2, BOS1, BOS3, FTF2, FLU1, FLU3, SHAM,
            TEB2, MCB1, MCB3, QXF2, DFC1, DFC3, BOS2, FTF1, FTF3, FLU2, CNTL, AZX1,
            TEB2, MCB1, MCB3, QXF2, DFC1, DFC3, BOS2, FTF1, FTF3, FLU2, CNTL, AZX1,
            TEB2, MCB1, MCB3, QXF2, DFC1, DFC3, BOS2, FTF1, FTF3, FLU2, CNTL, AZX1,
            TEB2, MCB1, MCB3, QXF2, DFC1, DFC3, BOS2, FTF1, FTF3, FLU2, CNTL, AZX1,
        ]
    elif plate == "plate2b":
        treatments = [
            TEB1, TEB3, QXF2, BOS1, BOS3, DFC2, MCB1, MCB3, SHAM, FTF1, FTF3, FLU2,
            TEB1, TEB3, QXF2, BOS1, BOS3, DFC2, MCB1, MCB3, SHAM, FTF1, FTF3, FLU2,
            TEB1, TEB3, QXF2, BOS1, BOS3, DFC2, MCB1, MCB3, SHAM, FTF1, FTF3, FLU2,
            TEB1, TEB3, QXF2, BOS1, BOS3, DFC2, MCB1, MCB3, SHAM, FTF1, FTF3, FLU2,
            TEB2, QXF1, QXF3, BOS2, DFC1, DFC3, MCB2, CNTL, AZX1, FTF2, FLU1, FLU3,
            TEB2, QXF1, QXF3, BOS2, DFC1, DFC3, MCB2, CNTL, AZX1, FTF2, FLU1, FLU3,
            TEB2, QXF1, QXF3, BOS2, DFC1, DFC3, MCB2, CNTL, AZX1, FTF2, FLU1, FLU3,
            TEB2, QXF1, QXF3, BOS2, DFC1, DFC3, MCB2, CNTL, AZX1, FTF2, FLU1, FLU3,
        ]
    elif plate == "plate3a":
        treatments = [
            MCB1, MCB3, FTF2, TEB1, TEB3, DFC2, QXF1, QXF3, SHAM, BOS1, BOS3, FLU2,
            MCB1, MCB3, FTF2, TEB1, TEB3, DFC2, QXF1, QXF3, SHAM, BOS1, BOS3, FLU2,
            MCB1, MCB3, FTF2, TEB1, TEB3, DFC2, QXF1, QXF3, SHAM, BOS1, BOS3, FLU2,
            MCB1, MCB3, FTF2, TEB1, TEB3, DFC2, QXF1, QXF3, SHAM, BOS1, BOS3, FLU2,
            MCB2, FTF1, FTF3, TEB2, DFC1, DFC3, QXF2, CNTL, AZX1, BOS2, FLU1, FLU3,
            MCB2, FTF1, FTF3, TEB2, DFC1, DFC3, QXF2, CNTL, AZX1, BOS2, FLU1, FLU3,
            MCB2, FTF1, FTF3, TEB2, DFC1, DFC3, QXF2, CNTL, AZX1, BOS2, FLU1, FLU3,
            MCB2, FTF1, FTF3, TEB2, DFC1, DFC3, QXF2, CNTL, AZX1, BOS2, FLU1, FLU3,
        ]
    elif plate == "plate3b":
        treatments = [
            CNTL, AZX1, QXF2, FLU1, FLU3, DFC2, BOS1, BOS3, TEB2, FTF1, FTF3, MCB2,
            CNTL, AZX1, QXF2, FLU1, FLU3, DFC2, BOS1, BOS3, TEB2, FTF1, FTF3, MCB2,
            CNTL, AZX1, QXF2, FLU1, FLU3, DFC2, BOS1, BOS3, TEB2, FTF1, FTF3, MCB2,
            CNTL, AZX1, QXF2, FLU1, FLU3, DFC2, BOS1, BOS3, TEB2, FTF1, FTF3, MCB2,
            SHAM, QXF1, QXF3, FLU2, DFC1, DFC3, BOS2, TEB1, TEB3, FTF2, MCB1, MCB3,
            SHAM, QXF1, QXF3, FLU2, DFC1, DFC3, BOS2, TEB1, TEB3, FTF2, MCB1, MCB3,
            SHAM, QXF1, QXF3, FLU2, DFC1, DFC3, BOS2, TEB1, TEB3, FTF2, MCB1, MCB3,
            SHAM, QXF1, QXF3, FLU2, DFC1, DFC3, BOS2, TEB1, TEB3, FTF2, MCB1, MCB3,
        ]
    elif plate == "plate4a":
        treatments = [
            QXF1, QXF3, FLU2, BOS1, BOS3, DFC2, FTF1, FTF3, TEB2, CNTL, AZX1, MCB2,
            QXF1, QXF3, FLU2, BOS1, BOS3, DFC2, FTF1, FTF3, TEB2, CNTL, AZX1, MCB2,
            QXF1, QXF3, FLU2, BOS1, BOS3, DFC2, FTF1, FTF3, TEB2, CNTL, AZX1, MCB2,
            QXF1, QXF3, FLU2, BOS1, BOS3, DFC2, FTF1, FTF3, TEB2, CNTL, AZX1, MCB2,
            QXF2, FLU1, FLU3, BOS2, DFC1, DFC3, FTF2, TEB1, TEB3, SHAM, MCB1, MCB3,
            QXF2, FLU1, FLU3, BOS2, DFC1, DFC3, FTF2, TEB1, TEB3, SHAM, MCB1, MCB3,
            QXF2, FLU1, FLU3, BOS2, DFC1, DFC3, FTF2, TEB1, TEB3, SHAM, MCB1, MCB3,
            QXF2, FLU1, FLU3, BOS2, DFC1, DFC3, FTF2, TEB1, TEB3, SHAM, MCB1, MCB3,
        ]
    elif plate == "plate4b":
        treatments = [
            MCB1, MCB3, FLU2, BOS1, BOS3, DFC2, FTF1, FTF3, TEB2, CNTL, AZX1, MCB2,
            MCB1, MCB3, FLU2, BOS1, BOS3, DFC2, FTF1, FTF3, TEB2, CNTL, AZX1, MCB2,
            MCB1, MCB3, FLU2, BOS1, BOS3, DFC2, FTF1, FTF3, TEB2, CNTL, AZX1, MCB2,
            MCB1, MCB3, FLU2, BOS1, BOS3, DFC2, FTF1, FTF3, TEB2, CNTL, AZX1, MCB2,
            MCB2, FLU1, FLU3, BOS2, DFC1, DFC3, FTF2, TEB1, TEB3, SHAM, MCB1, MCB3,
            MCB2, FLU1, FLU3, BOS2, DFC1, DFC3, FTF2, TEB1, TEB3, SHAM, MCB1, MCB3,
            MCB2, FLU1, FLU3, BOS2, DFC1, DFC3, FTF2, TEB1, TEB3, SHAM, MCB1, MCB3,
            MCB2, FLU1, FLU3, BOS2, DFC1, DFC3, FTF2, TEB1, TEB3, SHAM, MCB1, MCB3,
        ]
    elif plate == "plate5a":
        treatments = [
            FTF1, FTF3, QXF2, TEB1, TEB3, FLU2, BOS1, BOS3, SHAM, MCB1, MCB3, DFC2,
            FTF1, FTF3, QXF2, TEB1, TEB3, FLU2, BOS1, BOS3, SHAM, MCB1, MCB3, DFC2,
            FTF1, FTF3, QXF2, TEB1, TEB3, FLU2, BOS1, BOS3, SHAM, MCB1, MCB3, DFC2,
            FTF1, FTF3, QXF2, TEB1, TEB3, FLU2, BOS1, BOS3, SHAM, MCB1, MCB3, DFC2,
            FTF2, QXF1, QXF3, TEB2, FLU1, FLU3, BOS2, CNTL, AZX1, MCB2, DFC1, DFC3,
            FTF2, QXF1, QXF3, TEB2, FLU1, FLU3, BOS2, CNTL, AZX1, MCB2, DFC1, DFC3,
            FTF2, QXF1, QXF3, TEB2, FLU1, FLU3, BOS2, CNTL, AZX1, MCB2, DFC1, DFC3,
            FTF2, QXF1, QXF3, TEB2, FLU1, FLU3, BOS2, CNTL, AZX1, MCB2, DFC1, DFC3,
        ]
    elif plate == "plate5b":
        treatments = [
            TEB1, TEB3, DFC2, BOS1, BOS3, FTF2, QXF1, QXF3, FLU2, MCB1, MCB3, SHAM,
            TEB1, TEB3, DFC2, BOS1, BOS3, FTF2, QXF1, QXF3, FLU2, MCB1, MCB3, SHAM,
            TEB1, TEB3, DFC2, BOS1, BOS3, FTF2, QXF1, QXF3, FLU2, MCB1, MCB3, SHAM,
            TEB1, TEB3, DFC2, BOS1, BOS3, FTF2, QXF1, QXF3, FLU2, MCB1, MCB3, SHAM,
            TEB2, DFC1, DFC3, BOS2, FTF1, FTF3, QXF2, FLU1, FLU3, MCB2, CNTL, AZX1,
            TEB2, DFC1, DFC3, BOS2, FTF1, FTF3, QXF2, FLU1, FLU3, MCB2, CNTL, AZX1,
            TEB2, DFC1, DFC3, BOS2, FTF1, FTF3, QXF2, FLU1, FLU3, MCB2, CNTL, AZX1,
            TEB2, DFC1, DFC3, BOS2, FTF1, FTF3, QXF2, FLU1, FLU3, MCB2, CNTL, AZX1,
        ]
    elif plate == "plate6a":
        treatments = [
            MCB1, MCB3, FTF2, TEB1, TEB3, QXF2, CNTL, AZX1, DFC2, FLU1, FLU3, BOS2,
            MCB1, MCB3, FTF2, TEB1, TEB3, QXF2, CNTL, AZX1, DFC2, FLU1, FLU3, BOS2,
            MCB1, MCB3, FTF2, TEB1, TEB3, QXF2, CNTL, AZX1, DFC2, FLU1, FLU3, BOS2,
            MCB1, MCB3, FTF2, TEB1, TEB3, QXF2, CNTL, AZX1, DFC2, FLU1, FLU3, BOS2,
            MCB2, FTF1, FTF3, TEB2, QXF1, QXF3, SHAM, DFC1, DFC3, FLU2, BOS1, BOS3,
            MCB2, FTF1, FTF3, TEB2, QXF1, QXF3, SHAM, DFC1, DFC3, FLU2, BOS1, BOS3,
            MCB2, FTF1, FTF3, TEB2, QXF1, QXF3, SHAM, DFC1, DFC3, FLU2, BOS1, BOS3,
            MCB2, FTF1, FTF3, TEB2, QXF1, QXF3, SHAM, DFC1, DFC3, FLU2, BOS1, BOS3,
        ]
    elif plate == "plate6b":
        treatments = [
            MCB1, MCB3, SHAM, DFC1, DFC3, FTF2, TEB1, TEB3, FLU2, BOS1, BOS3, QXF2,
            MCB1, MCB3, SHAM, DFC1, DFC3, FTF2, TEB1, TEB3, FLU2, BOS1, BOS3, QXF2,
            MCB1, MCB3, SHAM, DFC1, DFC3, FTF2, TEB1, TEB3, FLU2, BOS1, BOS3, QXF2,
            MCB1, MCB3, SHAM, DFC1, DFC3, FTF2, TEB1, TEB3, FLU2, BOS1, BOS3, QXF2,
            MCB2, CNTL, AZX1, DFC2, FTF1, FTF3, TEB2, FLU1, FLU3, BOS2, QXF1, QXF3,
            MCB2, CNTL, AZX1, DFC2, FTF1, FTF3, TEB2, FLU1, FLU3, BOS2, QXF1, QXF3,
            MCB2, CNTL, AZX1, DFC2, FTF1, FTF3, TEB2, FLU1, FLU3, BOS2, QXF1, QXF3,
            MCB2, CNTL, AZX1, DFC2, FTF1, FTF3, TEB2, FLU1, FLU3, BOS2, QXF1, QXF3,
        ]
    elif plate == "plate7":
        treatments = [
            PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5, CNTL,
            PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5, CNTL,
            PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5, CNTL,
            PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5, CNTL,
            PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5, CNTL,
            PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5, CNTL,
            PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5, CNTL,
            PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5, CNTL,
        ]
    elif plate == "plate8":
        treatments = [
            CNTL, PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5,
            CNTL, PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5,
            CNTL, PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5,
            CNTL, PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5,
            CNTL, PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5,
            CNTL, PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5,
            CNTL, PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5,
            CNTL, PYL1, QXF4, QXF1, SHAM, MDS1, QXF3, AZX1, QXF2, QXF6, TFX1, QXF5,
        ]
    elif plate == "plate9":
            AZX1, PYL1, QXF2, QXF4, SHAM, QXF3, CNTL, TFX1, MDS1, QXF6, QXF5, QXF1,
            AZX1, PYL1, QXF2, QXF4, SHAM, QXF3, CNTL, TFX1, MDS1, QXF6, QXF5, QXF1,
            AZX1, PYL1, QXF2, QXF4, SHAM, QXF3, CNTL, TFX1, MDS1, QXF6, QXF5, QXF1,
            AZX1, PYL1, QXF2, QXF4, SHAM, QXF3, CNTL, TFX1, MDS1, QXF6, QXF5, QXF1,
            AZX1, PYL1, QXF2, QXF4, SHAM, QXF3, CNTL, TFX1, MDS1, QXF6, QXF5, QXF1,
            AZX1, PYL1, QXF2, QXF4, SHAM, QXF3, CNTL, TFX1, MDS1, QXF6, QXF5, QXF1,
            AZX1, PYL1, QXF2, QXF4, SHAM, QXF3, CNTL, TFX1, MDS1, QXF6, QXF5, QXF1,
            AZX1, PYL1, QXF2, QXF4, SHAM, QXF3, CNTL, TFX1, MDS1, QXF6, QXF5, QXF1,
    elif plate == "plate10":
            MDS1, QXF4, AZX1, QXF6, QXF1, SHAM, QXF3, CNTL, TFX1, PYL1, QXF2, QXF5,
            MDS1, QXF4, AZX1, QXF6, QXF1, SHAM, QXF3, CNTL, TFX1, PYL1, QXF2, QXF5,
            MDS1, QXF4, AZX1, QXF6, QXF1, SHAM, QXF3, CNTL, TFX1, PYL1, QXF2, QXF5,
            MDS1, QXF4, AZX1, QXF6, QXF1, SHAM, QXF3, CNTL, TFX1, PYL1, QXF2, QXF5,
            MDS1, QXF4, AZX1, QXF6, QXF1, SHAM, QXF3, CNTL, TFX1, PYL1, QXF2, QXF5,
            MDS1, QXF4, AZX1, QXF6, QXF1, SHAM, QXF3, CNTL, TFX1, PYL1, QXF2, QXF5,
            MDS1, QXF4, AZX1, QXF6, QXF1, SHAM, QXF3, CNTL, TFX1, PYL1, QXF2, QXF5,
            MDS1, QXF4, AZX1, QXF6, QXF1, SHAM, QXF3, CNTL, TFX1, PYL1, QXF2, QXF5,
    elif plate == "plate11":
            AZX1, TFX1, QXF5, PYL1, QXF6, QXF4, CNTL, QXF1, QXF2, SHAM, MDS1, QXF3,
            AZX1, TFX1, QXF5, PYL1, QXF6, QXF4, CNTL, QXF1, QXF2, SHAM, MDS1, QXF3,
            AZX1, TFX1, QXF5, PYL1, QXF6, QXF4, CNTL, QXF1, QXF2, SHAM, MDS1, QXF3,
            AZX1, TFX1, QXF5, PYL1, QXF6, QXF4, CNTL, QXF1, QXF2, SHAM, MDS1, QXF3,
            AZX1, TFX1, QXF5, PYL1, QXF6, QXF4, CNTL, QXF1, QXF2, SHAM, MDS1, QXF3,
            AZX1, TFX1, QXF5, PYL1, QXF6, QXF4, CNTL, QXF1, QXF2, SHAM, MDS1, QXF3,
            AZX1, TFX1, QXF5, PYL1, QXF6, QXF4, CNTL, QXF1, QXF2, SHAM, MDS1, QXF3,
            AZX1, TFX1, QXF5, PYL1, QXF6, QXF4, CNTL, QXF1, QXF2, SHAM, MDS1, QXF3,
    elif plate == "plate12":
            QXF4, CNTL, MDS1, SHAM, QXF5, QXF1, QXF3, QXF6, QXF2, PYL1, TFX1, AZX1,
            QXF4, CNTL, MDS1, SHAM, QXF5, QXF1, QXF3, QXF6, QXF2, PYL1, TFX1, AZX1,
            QXF4, CNTL, MDS1, SHAM, QXF5, QXF1, QXF3, QXF6, QXF2, PYL1, TFX1, AZX1,
            QXF4, CNTL, MDS1, SHAM, QXF5, QXF1, QXF3, QXF6, QXF2, PYL1, TFX1, AZX1,
            QXF4, CNTL, MDS1, SHAM, QXF5, QXF1, QXF3, QXF6, QXF2, PYL1, TFX1, AZX1,
            QXF4, CNTL, MDS1, SHAM, QXF5, QXF1, QXF3, QXF6, QXF2, PYL1, TFX1, AZX1,
            QXF4, CNTL, MDS1, SHAM, QXF5, QXF1, QXF3, QXF6, QXF2, PYL1, TFX1, AZX1,
            QXF4, CNTL, MDS1, SHAM, QXF5, QXF1, QXF3, QXF6, QXF2, PYL1, TFX1, AZX1,
    return treatments[block]
