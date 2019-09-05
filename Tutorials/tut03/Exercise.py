import math
import calendar
"""Displays Tutorial 3 Exercises"""
print("Int: "  + str(abs(round(-4.3))))
print("Float: " + str(math.fabs(round(-4.3))))
print("Ceiling: " + str(math.ceil(math.sin(math.radians(34.5)))))
print("Number of Leap years: " + str(calendar.leapdays(2000,2050)))
print("Day of the week: " + str(calendar.weekday(2019,9,13)))
print("Capitalised \'boolean\': " + "boolean".capitalize())
print("First occurrence of \'2\' in \'C02 H20\': " + str("C02 H20".find("2")))
print("Last occurrence of \'2\' in \'C02 H20\': " + str("C02 H20".rfind("2")))
print("Second occurrence of \'2\' in \'C02 N02 H20\': " + str("C02 N02 H20".find("2","C02 N02 H20".find("2") + 1)))
print("Does \'Boolean\' begin with a lowercase: " + str("Boolean".startswith("B")))
print("MoNDaY to lowercase: " + "MoNDaY".lower().capitalize())
print("Remove leading whitespace from \' Monday\': " + " Monday".lstrip())
