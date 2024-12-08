import java.util.*;
class Solution {
    public int solution(String[] board) {
        
        Queue<int[]> q = new LinkedList<>();
        int maxY = board.length, maxX = board[0].length(), sY = 0, sX = 0
            , ty, tx, ky, kx;
        int[][] visited = new int[maxY][maxX];
        int[] dirY = new int[]{0, 0, 1, -1};
        int[] dirX = new int[]{1, -1, 0, 0};
        int[] temp;
        int answer = maxY * maxX;
        
        for (int i = 0; i < maxY; i++) {
            Arrays.fill(visited[i], maxY*maxX);
        }
        
        for(int i=0; i<maxY; i++){
            for(int j=0; j<maxX; j++){
                if(board[i].charAt(j) == 'R'){
                    sY = i;
                    sX = j;
                    break;
                }
            }
        }
        
        q.add(new int[]{0, sY, sX, 0});
        q.add(new int[]{1, sY, sX, 0});
        q.add(new int[]{2, sY, sX, 0});
        q.add(new int[]{3, sY, sX, 0});
       // visited[sY][sX] = 1;
        
        while(!q.isEmpty()){
            temp = q.poll();
            
            ty = temp[1] + dirY[temp[0]];
            tx = temp[2] + dirX[temp[0]];
            
            if(0 <= ty && ty < maxY && 0 <= tx && tx < maxX &&
               board[ty].charAt(tx) != 'D'){
                    temp[1] = ty;
                    temp[2] = tx;
                    q.add(temp);
                    continue;
            } 
            if(board[temp[1]].charAt(temp[2]) == 'G'){
                visited[temp[1]][temp[2]] = Math.min(temp[3]+1, 
                                                     visited[temp[1]][temp[2]]);
                answer = Math.min(answer, temp[3]+1);
                continue;
            }
            if(temp[3]+1 < visited[temp[1]][temp[2]]){
                visited[temp[1]][temp[2]] = temp[3] +1;
                for(int i=0; i<4; i++){
                  q.add(new int[]{i, temp[1], temp[2], temp[3]+1}); 
                }
            }
        }
        if(answer == maxX*maxY){
            return -1;
        }
            return answer;
    }
}
        
    
   
