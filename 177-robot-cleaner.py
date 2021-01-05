# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        self.dfs(robot, set(), (0, 0))

    def dfs(self, robot, seen, current_point, current_direction=0):
        seen.add(current_point)
        robot.clean()

        r, c = current_point

        # up, left, down, right
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # We try out every possible direction.
        # To compute the next point, we add to the current point
        # the instructions to get to the next direction.

        # Changing direction and moving are two different operations.
        # We have to move to check if the next room is valid
        # After moving, we keep the direction
        # 1 1
        # 1 1
        # Starting at 0,0 we will try to move up, left and then down.
        # Reaching 1,0, the direction will be down.
        # If we were to iterate over the direction array, we would:
        # 1. check if up is in the set, rotate left, direction is now right
        # 2. check if left is in the set, and move right.
        # Here, the set and the direction are diverging causing an infinite loop
        # To solve this, we keep track of the current direction and try the next one from the direction array
        # We also compute the next point corresponding to the next direction by adding the correct direction
        for i in range(len(directions)):
            new_direction = (current_direction + i) % 4

            nr = r + directions[new_direction][0]
            nc = c + directions[new_direction][1]

            if (nr, nc) not in seen and robot.move():
                self.dfs(robot, seen, (nr, nc), new_direction)

                # backtrack: move back to the previous room and reset direction
                # Turn 180 degrees
                robot.turnLeft()
                robot.turnLeft()
                # Go back to the previous room
                robot.move()
                # Turn back to 180 degres again to be at the same point before
                # we started to visit the new room
                robot.turnLeft()
                robot.turnLeft()

            # Next direction
            robot.turnLeft()
