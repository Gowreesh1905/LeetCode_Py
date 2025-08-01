class Solution(object):
    def dfs(self,vis,node,adj):
        vis[node]=1

        for i in adj[node]:
            if vis[i]==0:
                self.dfs(vis,i,adj)


    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        adj=[[] for i in range( len(isConnected)+1)]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] and i!=j:
                    adj[i+1].append(j+1)

        vis=[0]*len(adj)
        conn=0
        for i in range(1,len(adj)):
            if vis[i]==0:
                conn+=1
                self.dfs(vis,i,adj)

        return conn