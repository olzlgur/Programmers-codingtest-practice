import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        char ex = words[0].charAt(words[0].length()-1);
        ArrayList<String> record = new ArrayList<>();
        record.add(words[0]);
        
        for(int i=1; i<words.length; i++){
            if(ex != words[i].charAt(0) ||record.contains(words[i])){             
              answer[1] = (int) ((i+1) / n) + 1;
              answer[0] = (i+1) % n;  
             if(answer[0] == 0){
                 answer[0] = n;
                 answer[1] -= 1;
             }
              break;
            }   
            ex = words[i].charAt(words[i].length()-1);  
            record.add(words[i]);
        }

        return answer;
    }
}