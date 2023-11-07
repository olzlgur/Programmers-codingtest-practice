// 프로그래머스 게임 맵 최단거리 https://school.programmers.co.kr/learn/courses/30/lessons/1844
import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        Queue<Integer> q = new LinkedList<>();
        int[] temp = new int[2];
        int n = maps.length;
        int m = maps[0].length;
        int[][] visited = new int[n][m];
        int cost, y, x, ty, tx;
        int[] dx = new int[]{0, 0, 1, -1};
        int[] dy = new int[]{1, -1, 0, 0};
        
        visited[0][0] = 1;
        q.add(0);
        q.add(0);
        q.add(0);
        
        while(!q.isEmpty()){
            y = q.poll();
            x = q.poll();
            cost = q.poll();
            
            
            if (y == n-1 && x == m-1){
                answer = cost + 1;
                break;
            }
            for(int i=0; i<4; i++){
                ty = y + dy[i];
                tx = x + dx[i];
                
                if(0 <= ty && ty < n && 0 <= tx && tx < m && maps[ty][tx] != 0 && visited[ty][tx] == 0){
                    q.add(ty);
                    q.add(tx);
                    q.add(cost+1);
                    visited[ty][tx] = 1;
                }
            }
            
        }
        
        
        return answer;
    }
}
