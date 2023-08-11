import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        Queue<Integer> q = new LinkedList<>();
        int answer = 0;
        int temp, size;
        
        q.add(0);
        
        for(int n : numbers){
            size = q.size();
            for(int i=0; i < size; i++){
                temp = q.poll();
                q.add(temp+n);
                q.add(temp-n);
            }
        }
        
        for(int n : q){
            if(n == target){
                answer += 1;
            }
        }
        
        return answer;
    }
}