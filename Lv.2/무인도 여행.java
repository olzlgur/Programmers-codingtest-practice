// https://school.programmers.co.kr/learn/courses/30/lessons/154540
import java.util.*;

class Solution {
    public int[] solution(String[] maps) {
        ArrayList<Integer> arr = new ArrayList<>();
        int[][] visited = new int[maps.length][maps[0].length()];
        Queue<int[]> q = new LinkedList<>();
        int[] temp = new int[3];
        int[] dirX = new int[]{0, 0, 1, -1};
        int[] dirY = new int[]{1, -1, 0, 0};
        int tn, ty = 0, tx = 0, maxY = maps.length, maxX = maps[0].length();
        
        for(int i=0; i<maxY; i++){
            for(int j=0; j<maxX; j++){
                if(visited[i][j] == 0 &&  maps[i].charAt(j) != 'X'){
                    visited[i][j] = 1;
                    q.add(new int[]{Integer.valueOf(maps[i].charAt(j)), i, j});
                    tn = Integer.valueOf(maps[i].charAt(j)) - 48;
                    while(!q.isEmpty()){
                        temp = q.poll();
                        for(int k=0; k<4; k++){
                            ty = temp[1] + dirY[k];
                            tx = temp[2] + dirX[k];
                            if(0 <= ty && ty < maxY && 0 <= tx && tx < maxX
                              && visited[ty][tx] == 0 && maps[ty].charAt(tx) != 'X'){
                                q.add(new int[] {temp[0] + 
                                    Integer.valueOf(maps[ty].charAt(tx)), ty, tx});
                                tn = tn + Integer.valueOf(maps[ty].charAt(tx)) - 48;
                                visited[ty][tx] = 1;
                            }
                        }
                    }   
                    arr.add(tn);
                }
                
            }
        }
        if(arr.size() == 0){
            return new int[]{-1};
        }
        
        Collections.sort(arr);
        int[] array = new int[arr.size()];
        
        for (int i = 0; i < arr.size(); i++) {
            array[i] = arr.get(i);
        }
        return array;
    }
}

// 지도에는 바다와 무인도들에 대한 정보 표시
// X or 1~9
// 
