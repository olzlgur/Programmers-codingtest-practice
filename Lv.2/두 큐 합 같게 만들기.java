import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0, temp;
        long sum = 0, sumQ1 = 0 ;
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        
        for(int i=0; i<queue1.length; i++){
            sum += (queue1[i] + queue2[i]);
            sumQ1 += queue1[i];
            q1.add(queue1[i]);
            q2.add(queue2[i]);
        }
        if(sum%2 != 0 ){
            return -1;
        }
        sum /= 2;
        while(sumQ1 != sum && answer<=queue1.length*4){
            if(sumQ1 < sum){
                temp = q2.poll();
                sumQ1 += temp;
                q1.add(temp);
                
            } else if(sum < sumQ1){
                temp = q1.poll();
                sumQ1 -= temp;
                q2.add(temp);
            }  else {
                return -1;
            }
            answer++;
        }
        
        if(answer > queue1.length*4 ){
            return -1;
        }
        return answer;
    }
}
