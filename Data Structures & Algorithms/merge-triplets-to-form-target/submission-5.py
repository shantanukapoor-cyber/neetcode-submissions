class Solution:
    def mergeTriplets(self, triplets, target):
        tx, ty, tz = target

        found_x = found_y = found_z = False

        for a, b, c in triplets:

            # Poison filter:
            # any coordinate exceeding target can never participate.
            if a > tx or b > ty or c > tz:
                continue

            if a == tx:
                found_x = True

            if b == ty:
                found_y = True

            if c == tz:
                found_z = True

            # Early exit saves work on large inputs.
            if found_x and found_y and found_z:
                return True

        return False