import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;
/*
토마토 (https://www.acmicpc.net/problem/7569)
메모리 : 127176 KB,	시간 : 808 ms

토마토가 모두 익는 최소 일수를 구하는 문제이므로 BFS를 이용
입력을 받으면서 큐에 익은 토마토들의 위치를 추가
익지 않은 토마토의 개수를 cnt 변수에 저장하고 마지막에 익힌 토마토의 개수와 비교해서 모두 익힐 수 있는지 없는 지 체크
맨 처음 입력 받은 배열을 이용해서 최소 일수 구하기
*/
public class BOJ_7569 {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int H = Integer.parseInt(st.nextToken());

        int[][][] box = new int[H][N][M];
        int start_h = 0;
        int start_x = 0;
        int start_y = 0;
        int cnt = 0;
        Queue<int[]> que = new LinkedList<>();

        for (int i = 0; i < H; i++) {
            for (int x = 0; x < N; x++) {
                st = new StringTokenizer(br.readLine());
                for (int y = 0; y < M; y++) {
                    int temp = Integer.parseInt(st.nextToken());
                    box[i][x][y] = temp;
                    if(temp == 1){
                        que.add(new int[] {i,x,y});
                    } else if(temp == 0) cnt++;
                }
            }
        }


        if(cnt == 0) System.out.println(0);
        else {
            int[] dh = {0,0,0,0,1,-1};
            int[] dx = {0,1,0,-1,0,0};
            int[] dy = {-1,0,1,0,0,0};
            int cnt_0 = 0;
            int day = 0;

            while (!que.isEmpty()){
                int[] temp = que.poll();
                if (cnt_0 == cnt) break;
                for (int i = 0; i < 6; i++) {
                    int nh = temp[0] + dh[i];
                    int nx = temp[1] + dx[i];
                    int ny = temp[2] + dy[i];
                    if(nh < H && nh >= 0 && nx < N && nx >= 0 && ny < M && ny >= 0){
                        if(box[nh][nx][ny] == 0) {
                            cnt_0++;
                            que.add(new int[]{nh,nx,ny});
                            box[nh][nx][ny] = box[temp[0]][temp[1]][temp[2]] + 1;
                        }
                        day = Math.max(day, box[nh][nx][ny]);
                    }
                }

            }

            if (cnt_0 != cnt) System.out.println(-1);
            else System.out.println(day-1);

        }

    }
}
