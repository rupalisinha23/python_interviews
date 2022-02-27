class Solution:
    def real_floodfill(self, image, sr, sc, rows, cols, old, new):
        if not 0 <= sr < rows or not 0 <= sc < cols or image[sr][sc] == -1 or image[sr][sc] != old:
            return
        image[sr][sc] = -1
        self.real_floodfill(image, sr+1, sc, rows, cols, old, new)
        self.real_floodfill(image, sr-1, sc, rows, cols, old, new)
        self.real_floodfill(image, sr, sc+1, rows, cols, old, new)
        self.real_floodfill(image, sr, sc-1, rows, cols, old, new)
        image[sr][sc] = new

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old = image[sr][sc]
        rows, cols = len(image), len(image[0])
        self.real_floodfill(image, sr, sc, rows, cols, old, newColor)
        return image
