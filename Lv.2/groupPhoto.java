// 입력 형식
// 입력은 조건의 개수를 나타내는 정수 n과 n개의 원소로 구성된 문자열 배열 data로 주어진다. data의 원소는 각 프렌즈가 원하는 조건이 N~F=0과 같은 형태의 문자열로 구성되어 있다. 제한조건은 아래와 같다.
// 1 <= n <= 100
// data의 원소는 다섯 글자로 구성된 문자열이다. 각 원소의 조건은 다음과 같다.
// 첫 번째 글자와 세 번째 글자는 다음 8개 중 하나이다. {A, C, F, J, M, N, R, T} 각각 어피치, 콘, 프로도, 제이지, 무지, 네오, 라이언, 튜브를 의미한다. 첫 번째 글자는 조건을 제시한 프렌즈, 세 번째 글자는 상대방이다. 첫 번째 글자와 세 번째 글자는 항상 다르다.
// 두 번째 글자는 항상 ~이다.
// 네 번째 글자는 다음 3개 중 하나이다. {=, <, >} 각각 같음, 미만, 초과를 의미한다.
// 다섯 번째 글자는 0 이상 6 이하의 정수의 문자형이며, 조건에 제시되는 간격을 의미한다. 이때 간격은 두 프렌즈 사이에 있는 다른 프렌즈의 수이다.
// 출력 형식
// 모든 조건을 만족하는 경우의 수를 리턴한다.
// 예제 입출력
// n	data	answer
// 2	["N~F=0", "R~T>2"]	3648
// 2	["M~C<2", "C~M>1"]	0
// 예제에 대한 설명
// 첫 번째 예제는 문제에 설명된 바와 같이, 네오는 프로도와의 간격이 0이기를 원하고 라이언은 튜브와의 간격이 2보다 크기를 원하는 상황이다.
// 두 번째 예제는 무지가 콘과의 간격이 2보다 작기를 원하고, 반대로 콘은 무지와의 간격이 1보다 크기를 원하는 상황이다. 이는 동시에 만족할 수 없는 조건이므로 경우의 수는 0이다.

import java.util.*;
class Solution {
    public boolean [] visited = new boolean[8];
    public int maxDepth = 8;
    public String[] friends = {"A", "C", "F", "J", "M", "N", "R", "T"};
    public int answer = 0;
    public String[] temp;
    List<String> outputList;
    
    public void check(String[] output, String[] datas){
        int checkNumber, conditionNumber;
        char condition;
        outputList = Arrays.asList(output);
        boolean flag = true;
        for(String data : datas){
            
            checkNumber = Math.abs(outputList.indexOf(String.valueOf(data.charAt(0)))
                                   - outputList.indexOf(String.valueOf(data.charAt(2))))-1;
            conditionNumber = Integer.parseInt(data.substring(4));
            condition = data.charAt(3);
            
            if(condition == '='){
                if (conditionNumber != checkNumber){
                    flag = false;
                    break;
                }
            } else if(condition == '<'){  
                if(conditionNumber <= checkNumber){
                    flag = false;
                    break;
                }
            } else{
                if(conditionNumber >= checkNumber){
                    flag = false;
                    break;
                }
            } 
        }
        if(flag){
            answer += 1;
        }
    }
    
    public void per(String[] output, int depth, String[] data) {
	if(depth == maxDepth) {
		check(output, data);
        temp = output;
		return;
	}

	for(int i = 0; i < maxDepth; i++) {
		if(visited[i] != true) {
			visited[i] = true;
			output[depth] = friends[i];
			per(output, depth + 1, data);    
			visited[i] = false;
		}
	}
}
    public int solution(int n, String[] data) {
        String[] output = new String[8];
        per(output, 0, data);
        
        return answer;
    }
}
