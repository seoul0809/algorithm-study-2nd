import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * BOJ 2146: 다리 만들기
 * - 메모리: 139112 KB
 * - 시간: 284 ms
 *
 * [설계]
 * 1. 2차원 배열 내에 섬들을 구별할 수 있도록 색칠해주어야 함
 *    - 한 점에서 섬 전체를 찾으면 되는 것이므로 DFS가 메모리도 적게 쓰고 더 빠름
 * 2. 섬 간 최소 거리 찾기: BFS
 * 
 * [후기]
 * 1학기 때 풀었던 문제의 기억으로 푼 문제. 다리만들기2는 이렇게 못 풀었던 걸로 기억해서 나중에 시간 나면 다시 풀어야겠다는 생각이 들었다.
 */

public class BOJ_2146 {

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int min = Integer.MAX_VALUE;


    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine().trim());
        int[][] map = new int[N][N];

        StringTokenizer st;
        for (int r = 0; r < N; ++r) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int c = 0; c < N; ++c) {
                map[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        // 지도 위에 섬 표시
        int islandIdx = 2;
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                if (map[r][c] == 1) {
                    findIslands(islandIdx++, r, c, map, N);
                }
            }
        }

        // 모든 칸에 대해 다른 최소 거리 찾기
        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                if (map[r][c] > 1) {
                    min = Math.min(min, findShortestBridgeLength(r, c, map, N));
                }
            }
        }

        System.out.println(min);
    }

    // 지도에 있는 섬 표시
    static void findIslands(int idx, int r, int c, int[][] map, int N) {
        map[r][c] = idx;

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (inRange(nr, nc, N) && map[nr][nc] == 1) {
                findIslands(idx, nr, nc, map, N);
            }
        }
    }

    // 섬 간 최소 거리 찾기
    static int findShortestBridgeLength(int r, int c, int[][] map, int N) {
        Queue<Coords> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][N];

        queue.offer(new Coords(r, c, 0));
        visited[r][c] = true;

        while (!queue.isEmpty()) {
            Coords curr = queue.poll();
            int cr = curr.r;
            int cc = curr.c;
            int cCount = curr.count;

            for (int d = 0; d < 4; ++d) {
                int nr = cr + dr[d];
                int nc = cc + dc[d];

                if (!inRange(nr, nc, N) || visited[nr][nc] || map[nr][nc] == map[r][c]) continue;

                if (map[nr][nc] != 0) return cCount; // 다른 섬에 도달했을 때

                queue.offer(new Coords(nr, nc, cCount + 1));
                visited[nr][nc] = true;
            }
        }

        // 다른 섬에 도달할 수 없는 경우
        return Integer.MAX_VALUE;
    }

    static boolean inRange(int r, int c, int N) {
        return r >= 0 && c >= 0 && r < N && c < N;
    }

    static class Coords {
        int r, c, count;

        Coords(int r, int c, int count) {
            this.r = r;
            this.c = c;
            this.count = count;
        }
    }
}
