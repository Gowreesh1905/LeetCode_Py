class Solution(object):
    def bfs(self,i,j,vis,grid):
        q=[(i,j)]
        vis[i][j]=1
        m=len(grid)
        n=len(grid[0])
        while len(q)!=0:
            a,b=q.pop(0)

            for k in range(-1,2):
                for l in range(-1,2):
                    if (k==0 and l!=0) or (k!=0 and l==0):
                        pass
                    
                    else:
                        continue
                    x=a+k
                    y=b+l

                    if x>=0 and x<m and y>=0 and y<n and int(grid[x][y])==1 and vis[x][y]==0 :
                        vis[x][y]=1
                        q.append((x,y))
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m=len(grid)
        n=len(grid[0])
        vis=[[0 for i in range(n)] for i in range(m)]
        isn=0
        for i in range(m):
            for j in range(n):
                if vis[i][j]==0 and int(grid[i][j])==1:
                    isn+=1
                    self.bfs(i,j,vis,grid)

        return isn


