import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;
/*
https://www.acmicpc.net/problem/7562
메모리 : 75096 KB / 시간 : 392 ms

최소 이동횟수를 구하는 것이므로 BFS를 이용하여 풀이
visited 배열을 만들어서 이동횟수를 체크 
*/
public class BOJ_7562 {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;

        int[] dx = {-2,-1,1,2,2,1,-1,-2};
        int[] dy = {-1,-2,-2,-1,1,2,2,1};

        for (int test_case = 0; test_case < T; test_case++) {
            int l = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine());
            int cur_x = Integer.parseInt(st.nextToken());
            int cur_y = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int target_x = Integer.parseInt(st.nextToken());
            int target_y = Integer.parseInt(st.nextToken());

            Queue<int[]> que = new LinkedList<>();
            int[][] visited = new int[l][l];


            que.add(new int[]{cur_x, cur_y});
            while(!que.isEmpty()){
                int[] temp = que.poll();
                cur_x = temp[0];
                cur_y = temp[1];
                if(cur_x == target_x && cur_y == target_y) break;

                for (int i = 0; i < 8; i++) {
                    int nx = cur_x + dx[i];
                    int ny = cur_y + dy[i];

                    if(nx >= 0 && nx < l && ny >= 0 && ny < l && visited[nx][ny] == 0){
                        visited[nx][ny] = visited[cur_x][cur_y]+1;
                        que.add(new int[]{nx,ny});
                    }
                }
            }
            System.out.println(visited[target_x][target_y]);

        }
    }

}
