class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        boxTypes.sort(key=lambda x : -x[1]) #유닛크기로 정렬
        
        maxi = 0
        
        for box in boxTypes:
            num_boxes, num_units = box[0], box[1]
            if truckSize >= num_boxes:
                maxi += num_boxes * num_units
                truckSize -= num_boxes
                continue
            else:
                maxi += truckSize * num_units
                break
                
        return maxi
        
