class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # positions :     0 3 5 8 10
        # speeds    :     1 3 1 4  2
        # eta       :    12 3 7 1  1
        # --------------------------
        # (12) (3 7) (1 1)

        # O(nlogn) - time complexity

        dist_left = [target - pos for pos in position]
        eta = [d / s for d,s in zip(dist_left, speed)]
        pos_eta = list(zip(position, eta))

        pos_eta.sort(key=lambda t: t[0])

        stack = []
        
        for pos, eta in pos_eta:
            while (stack and stack[-1] <= eta):
                # car infront has a further eta than car behind,
                # car behind can catch up and form a fleet with curr car
                stack.pop()
    
            stack.append(eta)

        return len(stack)
