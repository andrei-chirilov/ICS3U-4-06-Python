#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program calculates all RGB numbers


def main():
    red = 0
    green = 0
    blue = 0

    print("Welcome, this might take awhile so grab a drink and some popcorn.")
    input("Press enter to begin")

    for red in range(255):
        for green in range(255):
            for blue in range(255):
                print("RGB: (" + str(red) + ", " + str(green) + ", " +
                      str(blue) + ")")


if __name__ == "__main__":
    main()
