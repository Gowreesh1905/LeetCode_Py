class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        m=len(image)
        n=len(image[0])
        vis=[[0 for i in range(n)] for j in range(m)]
        clr0=image[sr][sc]

        image[sr][sc]=color

        q=[(sr,sc)]
        vis[sr][sc]=1
        dir_i=[-1,0,1,0]
        dir_j=[0,1,0,-1]
        while len(q)!=0:
            i,j=q.pop(0)

            for k in range(4):
                new_i=i+dir_i[k]
                new_j=j+dir_j[k]

                if new_i >=0 and new_i<m and new_j >=0 and new_j<n and vis[new_i][new_j]==0 and image[new_i][new_j]==clr0:
                    vis[new_i][new_j]=1
                    image[new_i][new_j]=color
                    q.append((new_i,new_j))


        return image




        
        