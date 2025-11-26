#!/usr/bin/env python3
# Created by: Patrick
# Created on: 11/24/2025
# This program prints all RGB color values using nested loops.


def main():
    # Loop through all possible values for red, green, and blue

    for r in range(0, 256):
        for g in range(0, 256):
            for b in range(0, 256):
                # Print the RGB value with the corresponding color

                print(f"\033[38;2;{r};{g};{b}mRGB({r}, {g}, {b})\033[0m")
                # Reset color after each print

                print("\033[0m", end="")


if __name__ == "__main__":
    main()
