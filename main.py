import ui
import sys


def main():
    if len(sys.argv) == 2:
        ui.path = sys.argv[1]
    ui.start_main_loop()


if __name__ == "__main__":
    main()
