"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

# from pycrazyswarm import Crazyswarm
from crazyflie_py import Crazyswarm


TAKEOFF_DURATION = 2.5
HOVER_DURATION = 5.0


def main():
    swarm = Crazyswarm()
    allcfs = swarm.allcfs
    timeHelper = swarm.timeHelper
    for cf in allcfs.crazyflies:
        cf.takeoff(targetHeight=1.0, duration=TAKEOFF_DURATION)

    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    
    for cf in allcfs.crazyflies:
        cf.land(targetHeight=0.04, duration=2.5)
    timeHelper.sleep(TAKEOFF_DURATION)


if __name__ == "__main__":
    main()
