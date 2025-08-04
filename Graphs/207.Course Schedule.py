class Solution(object):
    def canFinish(self, V, edges):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj=[[] for i in range(V)]
        for i in edges:
            u=i[1]
            v=i[0]
            adj[u].append(v)
            
        q=[]
        res=[]
        indeg=[0]*V
        
        for i in adj:
            for j in i:
                indeg[j]+=1
                
        for i in range(V):
            if indeg[i]==0:
                q.append(i)
                
        while len(q)!=0:
            
            node=q.pop(0)
            res.append(node)
            for i in adj[node]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)

        if len(res)<V:
            return False

        return True