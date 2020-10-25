import argparse


parser = argparse.ArgumentParser(description="Simple Python Script to convert APT1050 file to APT0850. ")
parser.add_argument("InputFile", help="Path for orginal input APT1050 file")
parser.add_argument("OutputFile", help="Path for new output APT0850 file")
parser.add_argument('-r', '--region', help="Region name (ex. EP - Poland) (def. EP)", required=False, default="EP" )


print("aptconv - Script to convert AP1050 file to APT0850")
print("Created by ORMO. Fall 2020 \n")

args = parser.parse_args()
print("Input XP_10 Filename: ", args.InputFile)
print("Output XP 8 Filename: ", args.OutputFile)
print("Region:", args.region)





navDataString = open(args.InputFile, "r", encoding="utf8").read().strip("\n")
navDataNew = open(args.OutputFile, "w", encoding="utf8")
#navDataString = navData.readlines()                                                 #reading the orginal file APT1100
navDataNew.write("I\n" + "850 Version - data cycle 2013.10, build 20131336, metadata AptXP900.  Copyright © 2013, Robin A. Peel (robin@x-plane.com).   This data is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.  You should have received a copy of the GNU General Public License along with this program (""AptNavGNULicence.txt""); if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.\n\n")
#adding a usual sentence to begin APT0850 file
navDataTable = navDataString.split("\n")
isValid = True


#def airportBlock():

for line in range(3, len(navDataTable)-1):
    eachValueTable = navDataTable[line].split(" ")
    firstValue = eachValueTable[0]


    if (firstValue == " "):
        isValid = False
    elif (firstValue.isdigit() == True):
        firstValueInt = int(firstValue)
        if (firstValueInt == 1):
            if ((len(eachValueTable) > 7) and (eachValueTable[7].startswith(args.region) == True)):
                navDataNew.write("\n")
                isValid = True
                print(isValid, line)
            else:
                isValid = False
                print(isValid, line)

    if (isValid == True):
        if (firstValueInt < 1000):
            if (firstValueInt == 16 and firstValueInt == 17):
                navDataNew.write("\n")
                eachLineString = ' '.join(map(str, eachValueTable))
                navDataNew.write(eachLineString +"\n")
            else:
                eachLineString = ' '.join(map(str, eachValueTable))
                navDataNew.write(eachLineString +"\n")

#navDataString.close()
print("App done\n%d lines checked " % line)
navDataNew.write("99\n")
navDataNew.close()
