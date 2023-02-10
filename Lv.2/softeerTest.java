import java.io.*;
import java.util.*;

class Main {
    private static int[][] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int count = 0;
        List<Integer> answer = new ArrayList<>();
        int lines = Integer.parseInt(br.readLine());
        String result = "";
        visited = new int[lines][lines];
        int[][] area = new int[lines][lines];
        for (int i = 0; i < lines; i++) {
            area[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }
        for (int i = 0; i < area.length; i++) {
            for (int j = 0; j < area.length; j++) {
                if (area[i][j] == 1 && visited[i][j] == 0) {
                    answer.add(bfs(i, j, lines, area));
                    count += 1;
                }
            }
        }
        Collections.sort(answer);
        System.out.println(count);
        if(count != 0){
            for (Integer value : answer) {
                result += value.toString() + " ";
            }
					System.out.println(result.substring(0, result.length()-1));
        }
    }

    private static int bfs(int x, int y, int n, int[][] area) {
        int areaSize = 0;
        Queue<List<Integer>> queue = new LinkedList<>();
        queue.add(List.of(x, y));
        List<Integer> temp = new ArrayList<>();
        visited[x][y] = 1;
        while (queue.size() != 0) {
            temp = queue.poll();
            if (temp.get(0) + 1 < n && area[temp.get(0) + 1][temp.get(1)] == 1 && visited[temp.get(0) + 1][temp.get(1)] == 0) {
                queue.add(List.of(temp.get(0) + 1, temp.get(1)));
                visited[temp.get(0) + 1][temp.get(1)] = 1;
            }
            if (temp.get(1) + 1 < n && area[temp.get(0)][temp.get(1) + 1] == 1 && visited[temp.get(0)][temp.get(1) + 1] == 0) {
                queue.add(List.of(temp.get(0), temp.get(1) + 1));
                visited[temp.get(0)][temp.get(1) + 1] = 1;
            }
            areaSize += 1;
        }
        return areaSize;
    }
}