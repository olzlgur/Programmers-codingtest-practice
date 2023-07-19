import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        HashMap<String, Integer> checkMerchan1 = new HashMap<String, Integer>();
        HashMap<String, Integer> checkMerchan2 = new HashMap<String, Integer>();
        Queue<String> queue = new LinkedList<>();
        int cnt = 0;
        int sumN = Arrays.stream(number).sum();
        String tmp; 
        
        for (int i=0; i< want.length; i++){
            checkMerchan1.put(want[i], number[i]);
            checkMerchan2.put(want[i], 0);
        }
        
        for (int i=0; i< discount.length; i++) {
            queue.add(discount[i]);
            if(checkMerchan2.containsKey(discount[i])) {
                checkMerchan2.put(discount[i], checkMerchan2.get(discount[i]) + 1);
                if(checkMerchan2.get(discount[i]) <= checkMerchan1.get(discount[i])) {
                    cnt += 1;
                }
            }
            if(queue.size() == 11) {
                tmp = queue.poll();
                if (checkMerchan2.containsKey(tmp)) {
                    checkMerchan2.put(tmp, checkMerchan2.get(tmp) -1);
                    if(checkMerchan2.get(tmp) < checkMerchan1.get(tmp)) {
                        cnt -= 1;
                    }
                }
            }
            if(cnt == sumN) {
                answer += 1;
            }
        }
        
        
        return answer;
    }
}