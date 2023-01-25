import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * BOJ 7569: 토마토
 * - 메모리: 96572 KB
 * - 시간: 656 ms
 *
 * [문제]
 * 토마토가 3차원 배열 안에 있다. 비어있는 칸, 익은 토마토, 안 익은 토마토가 들어있다.
 * 보관 후 하루가 지나면, 익은 토마토의 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토가 익는다고 할 때,
 *  며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라
 *
 * [풀이]
 * - 3차원 배열에서 6개 방향으로 이동하는 BFS
 * - 3차원 배열을 int가 아니라 boolean으로 잡으면 시간이 줄어듦. 30ms 정도긴 하지만...
 * - 나이트의 이동과 동일하게 최소 일수(이동 횟수)를 구하는 문제니까 level 관리해줘야 함
 */

public class BOJ_7569 {

    static int M, N, H;

    static int[] dm = {1, -1, 0, 0, 0, 0};
    static int[] dn = {0, 0, 1, -1, 0, 0};
    static int[] dh = {0, 0, 0, 0, 1, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        boolean[][][] tomatoes = new boolean[H][N][M];

        int total = 0;
        Queue<Tomato> ripeTomatoes = new ArrayDeque<>();

        for (int h = 0; h < H; ++h) {
            for (int n = 0; n < N; ++n) {
                st = new StringTokenizer(br.readLine(), " ");

                for (int m = 0; m < M; ++m) {
                    int val = Integer.parseInt(st.nextToken());

                    if (val != 0) {
                        tomatoes[h][n][m] = true;
                        if (val == 1) { // 익은 토마토인 경우
                            ripeTomatoes.offer(new Tomato(m, n, h));
                            ++total;
                        }
                    } else { // 덜 익은 토마토인 경우
                        ++total;
                    }
                }
            }
        }

        // 이미 다 익은 상태인 경우
        if (total == ripeTomatoes.size()) {
            System.out.println(0);
            return;
        }

        System.out.println(getDaysTilRipe(ripeTomatoes, tomatoes, total));
    }

    static int getDaysTilRipe(Queue<Tomato> ripeTomatoes, boolean[][][] tomatoes, int total) {
        int days = 0;

        while (!ripeTomatoes.isEmpty()) {
            int size = ripeTomatoes.size();

            for (int i = 0; i < size; ++i) {
                Tomato curr = ripeTomatoes.poll();
                --total;

                int cm = curr.m;
                int cn = curr.n;
                int ch = curr.h;

                for (int d = 0; d < 6; ++d) {
                    int nm = cm + dm[d];
                    int nn = cn + dn[d];
                    int nh = ch + dh[d];

                    if (!inRange(nm, nn, nh) || tomatoes[nh][nn][nm]) {
                        continue;
                    }

                    ripeTomatoes.offer(new Tomato(nm, nn, nh));
                    tomatoes[nh][nn][nm] = true;
                }
            }

            if (total == 0) return days;

            ++days;
        }

        return -1;
    }

    static boolean inRange(int m, int n, int h) {
        return m >= 0 && n >= 0 && h >= 0 && m < M && n < N && h < H;
    }

    // 토마토 좌표 관리 위한 클래스
    static class Tomato {
        int m, n, h;

        Tomato(int m, int n, int h) {
            this.m = m;
            this.n = n;
            this.h = h;
        }

        @Override
        public String toString() {
            return "Tomato [m=" + m + ", n=" + n + ", h=" + h + "]";
        }

    }

}
