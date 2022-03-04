class Solution {
    
    Double[][] receive_amt;
    
    public double champagneTower(int poured, int query_row, int query_glass) {
        receive_amt = new Double[query_row + 1][query_glass + 1];
        double receive = received(poured, query_row, query_glass);
        
        return receive > 1 ? 1 : receive;
    }
    
    public double received(int poured, int query_row, int query_glass) {
        if (query_row == 0) {
            return poured;
        }
        
        if (receive_amt[query_row][query_glass] != null) return receive_amt[query_row][query_glass];
        
        double left = query_glass - 1 < 0 ? 0 : spillOver(poured, query_row - 1, query_glass - 1) ;
        double right = query_glass == query_row ? 0 : spillOver(poured, query_row - 1, query_glass);
        
        receive_amt[query_row][query_glass] = left + right;
        
        return receive_amt[query_row][query_glass];
        
    }
    
    public double spillOver(int poured, int query_row, int query_glass) {
        
        double received = received(poured, query_row, query_glass);
        
        double spillOver = received > 1 ? (received - 1)/ 2 : 0;
        
        return spillOver;
    }
    
    
}
