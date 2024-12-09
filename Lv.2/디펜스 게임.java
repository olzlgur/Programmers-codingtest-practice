import java.util.*;
class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        int sum = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for(int i=0; i < enemy.length; i++){

            pq.offer(enemy[i]); 
            sum += enemy[i]; 
            //System.out.println(pq);
            while(n < sum && 0 < k){
                k--; 
                sum -= pq.poll();
            }
            if(k == 0 && n < sum){
                return i;
            }
        }
        
        
        return enemy.length;
    }
}

// 병사 n명
// enenmy 적
// 남은 병사보다 라은두 적의 수가 많으면 종료
// 무적권은 최대 k번
//
