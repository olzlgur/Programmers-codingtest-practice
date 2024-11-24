
// https://school.programmers.co.kr/learn/courses/30/lessons/159993
import java.util.*;
class Solution {
    public int solution(String[] maps) {
        int answer = 0;
        int startY = 0, startX = 0, ty = 0, tx = 0;
        Queue<Integer[]> q = new LinkedList<>();
        int[][] visited = new int[maps.length][maps[0].length()];
        Integer[] temp = new Integer[3];
        int[] dirY = new int[]{0,0,1,-1};
        int[] dirX = new int[]{1,-1,0,0};
        int maxY = maps.length, maxX = maps[0].length();
        
        for(int i=0; i<maxY; i++){
            for(int j=0; j<maxX; j++){
                if(maps[i].charAt(j) == 'S'){
                    startY = i;
                    startX = j;
                }
            }
        }
        q.add(new Integer[]{0, startY, startX});
        
        visited[startY][startX] = 1;
        startY = -1;
        startX = -1;
        while(!q.isEmpty()){
           temp = q.poll();
            for(int i=0; i<4; i++){
                ty = dirY[i] + temp[1];
                tx = dirX[i] + temp[2];
                
                
                if(0<= ty && ty < maxY && 0 <= tx && tx < maxX && 
                   visited[ty][tx] == 0 && maps[ty].charAt(tx) != 'X'){
                    if(maps[ty].charAt(tx) == 'L'){
                        startY = ty;
                        startX = tx;
                        answer = temp[0] + 1;
                        q = new LinkedList<>();
                        break;                            
                    }
                    q.add(new Integer[]{temp[0]+1, ty, tx});
                    visited[ty][tx] = 1;
                } 
            }
            
        }
        if(startY == -1){
            return -1;
        }
        
        q.add(new Integer[]{answer, startY, startX});
        visited = new int[maxY][maxX];
        visited[startY][startX] = 1;
        
        while(!q.isEmpty()){
           temp = q.poll();
            for(int i=0; i<4; i++){
                ty = dirY[i] + temp[1];
                tx = dirX[i] + temp[2];
                
                if(0<= ty && ty < maxY && 0 <= tx && tx < maxX && 
                   visited[ty][tx] == 0 && maps[ty].charAt(tx) != 'X'){
                    if(maps[ty].charAt(tx) == 'E'){
                        return temp[0] +1;                         
                    }
                    q.add(new Integer[]{temp[0]+1, ty, tx});
                    visited[ty][tx] = 1;
                } 
            }
            
        }
        
        return -1;
    }
}

// 직사각형 미로, 통로는 벽 또는 길
// 미로 빠져나가는 레버 당긴 후 미로 출구 가야함
// 
