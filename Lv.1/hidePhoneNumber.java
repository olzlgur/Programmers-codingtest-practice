[프로그래머스] url: https://school.programmers.co.kr/learn/courses/30/lessons/12948

class Solution {
    public String solution(String phone_number) {
        String answer = "*".repeat(phone_number.length()-4);
        
        return answer + phone_number.substring(phone_number.length()-4);
    }
}
