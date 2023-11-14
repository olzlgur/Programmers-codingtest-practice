// [프로그래머스] 숫자 변환하기 url: https://school.programmers.co.kr/learn/courses/30/lessons/154538
import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int answer = -1;
        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(
        (list1, list2) -> Integer.compare(list1.get(1), list2.get(1)));
        List<Integer> temp = new ArrayList<>();
        int num, cnt;
        
        temp.add(y);
        temp.add(0);
        pq.add(new ArrayList<>(temp));
        
        while(!pq.isEmpty()){
            temp = pq.poll();
            num = temp.get(0);
            cnt = temp.get(1);
            
            if(num == x){
                return cnt;
            }
            
            if(num > n){
                temp.set(0, num-n);
                temp.set(1, cnt+1);
                pq.add(new ArrayList<>(temp));
            }
            
            if(num % 2 == 0){
                temp.set(0, num/2);
                temp.set(1, cnt+1);
                pq.add(new ArrayList<>(temp));
            }
            
            if(num % 3 == 0){
                temp.set(0, num/3);
                temp.set(1, cnt+1);
                pq.add(new ArrayList<>(temp));
            }
        }
        
        return answer;
    }
}

// x를 y로 변환
// x + n, x * 2, 
