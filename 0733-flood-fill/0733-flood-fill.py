class Solution(object):
    def fill(self,image,sr,sc,color,newColor):
    
        if (sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color): 
            return
        image[sr][sc] = newColor
        self.fill(image, sr + 1, sc, color, newColor)
        self.fill(image, sr - 1, sc, color, newColor)
        self.fill(image, sr, sc + 1, color, newColor)
        self.fill(image, sr, sc - 1, color, newColor)
        return image

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image
    
    