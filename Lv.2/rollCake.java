// [프로그래머스] 롤케익 자르기 url: https://school.programmers.co.kr/learn/courses/30/lessons/132265
class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        int len = topping.length;
        int[] left= new int[len];
        int[] right = new int[len];
        int[] visited = new int[len+1];
        
        left[0] = 1;
        right[len-1] = 1;
        visited[topping[0]] =1;
        
        for(int i=1; i < len; i++){
            if(visited[topping[i]] == 0){
                visited[topping[i]] = 1;
                left[i] = left[i-1] + 1; 
            } else{
                left[i] = left[i-1];
            }
        }
        
        visited = new int[len+1];
        visited[topping[len-1]] = 1;
        
        for(int i=len-2; 0 <= i; i--){
            if(visited[topping[i]] == 0){
                visited[topping[i]] = 1;
                right[i] = right[i+1] + 1; 
            } else{
                right[i] = right[i+1];
            }
        }
        
        for(int i=0; i<len-1; i++){
            if(left[i] == right[i+1]){
                answer += 1;
            }
        }
        
        return answer;
    }
}

// 롤 케이크 두조각 한조각씩 나눠 먹으려고 함
// 여러가지 토핑 일렬
// 동일한 가짓수
