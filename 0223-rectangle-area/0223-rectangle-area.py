class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_first = abs(ax1 - ax2) * abs(ay1 - ay2)
        area_second = abs(bx1 - bx2) * abs(by1 - by2)
        x_dis = (min(ax2, bx2) -max(ax1, bx1))
        y_dis = (min(ay2, by2) -max(ay1, by1))
        Area = 0
        if x_dis > 0 and y_dis > 0:
            Area = x_dis * y_dis
        return (area_first + area_second - Area)