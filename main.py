from scenes import scenes
import sys


def main():
    """This function selects the corresponding scene based on the argument, or prints an error to the user"""
    if len(sys.argv) > 1:
        scene_name = sys.argv[1]
        if scene_name in scenes:
            simulation = scenes[scene_name]()
            simulation.mainloop()
        else:
            print("Invalid scene name.")
    else:
        print("Please provide a scene name.")


if __name__ == '__main__':
    main()
