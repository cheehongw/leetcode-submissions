class Solution {
    
    int[][] shortestPaths;
    
    public int networkDelayTime(int[][] times, int n, int k) {
        shortestPaths = new int[n][n];        
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                shortestPaths[i][j] = i == j ? 0 : 9000000;
            }
        }
        
        for (int[] edge : times) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            int cost = edge[2];
            
            shortestPaths[u][v] = Math.min(shortestPaths[u][v], cost);
            
        }
        
        
        
        for (int l = 0; l < n; l++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    shortestPaths[i][j] = Math.min(shortestPaths[i][j], shortestPaths[i][l] + shortestPaths[l][j]);
                    
                }       
            }
        }
        
        int curr_highest = 0;
        for (int i = 0; i < n; i++) {
            if (shortestPaths[k - 1][i] >= 9000000) {
                curr_highest = -1;
                break;
            }
            
            curr_highest = Math.max(curr_highest, shortestPaths[k - 1][i]);
        }
        
        //System.out.println(curr_highest);
        return curr_highest;
        
        
    }
}
