"""An exercise in remainders and boolean logic."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


how_much: int = int(input("Enter an int:"))
 
if how_much % 2 == 0:
    print("TAR")
if how_much % 7 == 0:
    print("HEELS")
if how_much % 14 == 0:
    print("TAR HEELS")
else:
    print("CAROLINA")
