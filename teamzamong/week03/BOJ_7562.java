import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * BOJ 7562: 나이트의 이동
 * - 메모리: 42064 KB
 * - 시간: 316 ms
 *
 * [문제]
 * 체스판 위에 있는 나이트가 있다. 나이트가 한 번에 이동할 수 있는 칸은 정해져 있다. (dr, dc 참조)
 * 주어진 칸으로 이동하기 위한 나이트의 최소 이동 횟수는?
 *
 * [풀이]
 * - 최소 이동 횟수 => BFS로 풀기!
 * - BFS로 탐색할 때, 몇 번째 level인지 또한 관리해야 한다.
 */

public class BOJ_7562 {

    static int[] dr = {1, 2, 2, 1, -1, -2, -2, -1};
    static int[] dc = {2, 1, -1, -2, -2, -1, 1, 2};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine().trim()); // 테스트케이스 개수

        StringTokenizer st;
        Coords knight, target;
        for (int t = 0; t < T; ++t) {
            int l = Integer.parseInt(br.readLine().trim()); // 체스판 한 변의 길이

            st = new StringTokenizer(br.readLine(), " ");
            knight = new Coords(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

            st = new StringTokenizer(br.readLine(), " ");
            target = new Coords(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

            System.out.println(getMoveCount(l, knight, target));
        }
    }

    // BFS를 사용해 최소 이동 횟수 구하기
    static int getMoveCount(int l, Coords knight, Coords target) {
        Queue<Coords> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[l][l];

        queue.offer(knight);
        visited[knight.r][knight.c] = true;

        int count = 0;

        while (!queue.isEmpty()) {
            // BFS 이동 시, 몇 번의 level을 거쳐서 이동했는지 확인하기 위해 size 활용
            // size는 그 위치까지 가기 위한 나이트의 최소 이동 횟수와 같음
            int size = queue.size();

            for (int i = 0; i < size; ++i) {
                Coords curr = queue.poll();

                if (curr.equals(target)) return count;

                int r = curr.r;
                int c = curr.c;

                for (int d = 0; d < 8; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (!inRange(l, nr, nc) || visited[nr][nc]) continue;

                    Coords n = new Coords(nr, nc);

                    queue.offer(n);
                    visited[nr][nc] = true;
                }
            }
            ++count;
        }

        return count;
    }

    static boolean inRange(int l, int r, int c) {
        return r >= 0 && c >= 0 && r < l && c < l;
    }

    // 좌표 관리 위한 클래스
    static class Coords {
        int r, c;

        Coords(int r, int c) {
            this.r = r;
            this.c = c;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;

            if (o == null || getClass() != o.getClass()) return false;

            Coords coords = (Coords) o;
            return r == coords.r && c == coords.c;
        }

    }

}
