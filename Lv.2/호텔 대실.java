// https://school.programmers.co.kr/learn/courses/30/lessons/155651
import java.util.*;
import java.time.LocalTime;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 1;
        Queue<LocalTime> q = new LinkedList<>();
        LocalTime temp1, temp2;
        Arrays.sort(book_time, Comparator.comparing(x -> x[0]));
        temp1 = LocalTime.parse(book_time[0][1]);
        if(temp1.isAfter(LocalTime.parse("23:49"))){
            q.add(LocalTime.parse("23:59"));
        }else {
            temp1 = temp1.plusMinutes(10);    
            q.add(temp1);
        }
        
        for(int i=1; i<book_time.length; i++){
            temp1 = LocalTime.parse(book_time[i][0]);
           
           for(int j=0; j<q.size(); j++){
               temp2 = q.poll();
               if(!temp1.isBefore(temp2)){
                  break;
               }
               q.add(temp2);
           }
            temp1 = LocalTime.parse(book_time[i][1]);
            if(temp1.isAfter(LocalTime.parse("23:49"))){
                 q.add(LocalTime.parse("23:59"));
            }else {
                temp1 = temp1.plusMinutes(10);   
                q.add(temp1);
             }
            answer = Math.max(answer, q.size());
        }
        
        return answer;
    }
}
