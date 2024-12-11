import java.util.*;
class Solution {
    public String[] solution(String[] orders, int[] course) {
        String[] answer;
        HashMap<String, Integer> map = new HashMap<>();
        List<String> list, result = new ArrayList<>();
        int maxNum;
        
        for(int i=0; i<course.length; i++){
            for(int j=0; j<orders.length; j++){
                if(course[i] <= orders[j].length()){
                    combination(orders[j], 0, "", map, course[i]);
                }
            }
        }
        Set<String> keySet = map.keySet();
        
      //  System.out.println(map);
        for(int i=0; i<course.length; i++){
            list = new ArrayList<>();
            maxNum = 0;
            
            for (String key : keySet) {	
               // System.out.println(list);
	            if(key.length() == course[i] && map.get(key) != 1){
                    if(map.get(key) > maxNum){
                        list = new ArrayList<>();
                        list.add(key);
                        maxNum = map.get(key);
                    } else if(map.get(key) == maxNum){
                        list.add(key);
                    }
                }	
            }
            result.addAll(list);
        }
        Collections.sort(result);
        System.out.println(result);
        answer = new String[result.size()];
        
        for(int i=0; i<result.size(); i++){
            answer[i] = result.get(i);
        }
        
        return answer;
    }
    
     public static void combination(String str, int idx,
        String result, HashMap<String, Integer> map, int length) {
        if (result.length() == length) {
             char[] temp = result.toCharArray();
            Arrays.sort(temp);
            result = new String(temp);
            if(map.containsKey(result)){
                map.replace(result, map.get(result)+1);
            } else{
                map.put(result, 1);
            }
            return; 
        }

        for (int i = idx; i < str.length(); i++) {
            combination(str, i + 1, result + str.charAt(i), map, length);
        }
        
        return;
    }
}

// 단품 메뉴 -> 코스
// 가장 많이 함께 주문한 메뉴 코스
// 2가지 이상, 2명 이상 손님 주문
// 손님당 2개 이상 메뉴 주문
