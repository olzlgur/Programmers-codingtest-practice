import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Queue<List<Integer>> q = new LinkedList<>();
        List<Integer> answer = new ArrayList<>();
        int size = 0;
        int cnt = 0;
        int idx1 = 0;
        
        for(int idx=0; idx <progresses.length; idx++){
            List<Integer> tmp = new ArrayList<>();
            tmp.add(progresses[idx]);
            tmp.add(speeds[idx]);
            q.add(tmp);
        }
        
        while (q.size() !=0){
            List<Integer> first = new ArrayList<>();
            first = q.poll();
            size = q.size();
            if(100 <= first.get(0)+first.get(1)) {
                answer.add(1);
                for(idx1=0; idx1 < size; idx1++){
                    List<Integer> tmp = new ArrayList<>();
                    tmp = q.poll();
                    if(tmp.get(0)+tmp.get(1) < 100) {
                        tmp.set(0, tmp.get(0)+tmp.get(1));
                        q.add(tmp);
                        break;
                    } 
                    answer.set(cnt, answer.get(cnt)+1);
                }
                for(int idx2=idx1+1; idx2 < size; idx2++){
                    List<Integer> tmp = q.poll();
                    tmp.set(0, tmp.get(0)+tmp.get(1));
                    q.add(tmp);
                }
                cnt += 1;
            } else {
                first.set(0, first.get(0)+first.get(1));
                q.add(first);
                for(idx1=0; idx1 < size; idx1++){
                    List<Integer> tmp = new ArrayList<>();
                    tmp = q.poll();
                    tmp.set(0, tmp.get(0)+tmp.get(1));
                    q.add(tmp);
                }
            }
        }
        
        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
