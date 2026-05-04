class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # by position desc
        fleets = 0
        max_time = -1.0

        for p, s in cars:
            t = (target - p) / s
            if t > max_time:          # strict peak => new fleet
                fleets += 1
                max_time = t          # becomes the fleet's arrival time
            # else: merges (including equality)

        return fleets
