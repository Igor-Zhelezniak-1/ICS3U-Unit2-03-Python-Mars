#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is mars program

import constants


def main():
    # this function calculates the time to Mars

    # input
    print("The distance to mars is 106340000000 m.")
    distance = int(input("Enter distance to mars (m): "))

    # process
    time = distance / constants.SPEED

    # output
    print(
        "If distance is {0} m, it will take light {1} seconds to get there.".format(
            distance, time
        )
    )
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
