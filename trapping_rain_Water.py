from typing import List

def trap(height: List[int]) -> int:
    ret = 0
    stack = []

    for h in range(len(height)):

        # stack is only filled with decreasing heights, an increase will cause pops
        while stack and height[stack[-1]] < height[h]:
            # find divets
            divet = stack.pop()

            # if stack is empty, no divet was formed.
            if not stack:
                break

            # if divet was formed, fill it.
            """        
            h is the right border and stack[-1] is the left border of the divet.

            The idea is to keep moving to the left until the left is bigger than the right,
            and add rain caught as you go.

            This is essentially whats happening:

            |               h
            |   |           |
            |   |   |   -1  |
            |   |   |   |   |

            |                h
            |   |  -1   d   |
            |   |   |   1   |
            |   |   |   |   |

            |   -1  d   d   h
            |   |   2   2   |
            |   |   |   1   |
            |   |   |   |   |



            """
            lowest_border = min(height[stack[-1]], height[h])
            rain_filled = lowest_border - height[divet]
            width = h - stack[-1] - 1
            ret += rain_filled * (width)

        stack.append(h)

    return ret

arr =[3,0,0,2,0,4]
print(trap(arr))
