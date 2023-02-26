import java.util.*;

class PRG_1844 {

  static int[] dr = { -1, 1, 0, 0 };
  static int[] dc = { 0, 0, -1, 1 };

  public int solution(int[][] maps) {
    int n = maps.length;
    int m = maps[0].length;

    boolean[][] visited = new boolean[n][m];
    Queue<int[]> queue = new ArrayDeque<>();
    queue.offer(new int[] { 0, 0 });

    int count = 0;
    while (!queue.isEmpty()) {

      int size = queue.size();
      for (int i = 0; i < size; ++i) {
        int[] curr = queue.poll();

        if (curr[0] == n - 1 && curr[1] == m - 1)
          return count + 1;

        for (int d = 0; d < 4; ++d) {
          int nr = curr[0] + dr[d];
          int nc = curr[1] + dc[d];

          if (!inRange(nr, nc, n, m) || maps[nr][nc] == 0 || visited[nr][nc])
            continue;

          visited[nr][nc] = true;
          queue.offer(new int[] { nr, nc });
        }
      }
      ++count;
    }

    return -1;
  }

  static boolean inRange(int r, int c, int n, int m) {
    return r >= 0 && c >= 0 && r < n && c < m;
  }
}