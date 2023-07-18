import java.util.*;
import java.util.Collections;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int tmp = 0;
        
        HashMap<Integer, Integer> map1 = new HashMap<Integer, Integer>();
        
        for(int t : tangerine) {
            if (map1.containsKey(t)) {
                map1.put(t, map1.get(t) + 1);
            } else {
                map1.put(t, 1);
            }
        }
        
        List<Integer> valueList = new ArrayList<>(map1.values());
        Collections.sort(valueList);
        Collections.reverse(valueList);
        
        for (Integer value : valueList) {
            answer += 1;
            tmp += value;
            if (k <= tmp) {
                return answer;
            }
        }
        
        return answer;
    }
}
