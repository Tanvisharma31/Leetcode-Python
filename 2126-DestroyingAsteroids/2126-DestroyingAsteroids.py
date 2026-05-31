# Last updated: 5/31/2026, 9:23:31 AM
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        mx = max(asteroids)

        while asteroids:
            uneaten = []
            for aster in asteroids:
                if mass < aster:
                    uneaten.append(aster)
                else:
                    mass += aster
                    if mass >= mx:
                        return True
            if len(uneaten) == len(asteroids):
                return False
            
            asteroids = uneaten
        
        return True