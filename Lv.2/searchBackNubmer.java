// [프로그래머스] url: https://school.programmers.co.kr/learn/courses/30/lessons/154539
import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        Arrays.fill(answer, -1);
        List<Integer> temp = new ArrayList<>();
        List<Integer> compare;
        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(
    (list1, list2) -> Integer.compare(list1.get(1), list2.get(1)))
;
        int position = 1;
        
        temp.add(0);
        temp.add(numbers[0]);
    
        pq.add(new ArrayList<>(temp));
        
        while(position < numbers.length){
            while(!pq.isEmpty()){
                compare = pq.poll(); 
                if( compare.get(1) < numbers[position]){
                    answer[compare.get(0)] = numbers[position];
                } else {
                    pq.add(new ArrayList<>(compare));
                    break;
                }
            }
            temp.set(0, position);
            temp.set(1, numbers[position]);
            pq.add(new ArrayList<>(temp));
            
            position += 1;
        }
        
        
        
        return answer;
    }
}
