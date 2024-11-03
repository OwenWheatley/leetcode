class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        tree = defaultdict(list)
        
        for child, par in enumerate(parent):
            if par != -1:
                tree[par].append(child)
        
        myMap = defaultdict(list)
        ans = [0] * n
        
        def dfs_adjust_parents(node: int) -> None:
            char = s[node]
            if myMap[char]:
                closest_ancestor = myMap[char][-1]
                if parent[node] != closest_ancestor:
                    tree[parent[node]].remove(node)
                    tree[closest_ancestor].append(node)
                    parent[node] = closest_ancestor
            
            myMap[char].append(node)
            
            for child in list(tree[node]):
                dfs_adjust_parents(child)
            
            myMap[char].pop()
        
        def dfs_calculate_sizes(node: int) -> int:
            size = 1
            for child in tree[node]:
                size += dfs_calculate_sizes(child)
            ans[node] = size
            return size
        
        dfs_adjust_parents(0)
        
        dfs_calculate_sizes(0)
        
        return ans