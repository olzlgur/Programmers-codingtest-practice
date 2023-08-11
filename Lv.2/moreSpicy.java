import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pQ = new PriorityQueue<>();
        int answer = 0;
        int tmp1, tmp2;
        
        for(int sc : scoville) {
            pQ.add(sc);
        }
        
        while(pQ.size() != 1){
            tmp1 = pQ.poll();
            
            if( K <= tmp1 ) {
                return answer;
            }
            tmp2 = pQ.poll();
            pQ.add(tmp1 + (tmp2*2));
            
            answer += 1;   
        }
        if(pQ.poll() <K) {
            return -1;
        }
        return answer;
    }
