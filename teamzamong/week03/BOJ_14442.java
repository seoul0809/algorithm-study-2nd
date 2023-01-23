import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * BOJ 14442: 벽 부수고 이동하기 2
 * - 메모리: 337544 KB
 * - 시간: 1680 ms
 *
 * [설계]
 * 1. 두 점 간 최단 거리를 찾기 위해 BFS 활용
 * 2. 벽을 부수고 이동하는 최단 거리를 고려하기 위해서 3차원 배열을 사용
 * 	  - visited[N][M][K]: 행, 열, 벽 부순 횟수
 * 
 * [후기]
 * 시간 적게 걸린 다른 풀이를 봤더니 3차원이 아닌 2차원 방문 배열을 사용했던데 이해가 잘 안 된당...
 */

public class BOJ_14442 {

	static final int[] dr = { -1, 1, 0, 0 };
	static final int[] dc = { 0, 0, -1, 1 };

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		char[][] map = new char[N][];
		for (int r = 0; r < N; ++r) {
			map[r] = br.readLine().toCharArray();
		}

		System.out.println(bfs(map, N, M, K));
	}

	// (0,0)에서 (N-1, M-1)까지 최단 거리를 구하기 위해서 BFS 활용
	// 벽 부순 횟수를 관리하기 위해서 3차원 방문 배열 사용
	static int bfs(char[][] map, int N, int M, int K) {
		Queue<Coord> queue = new ArrayDeque<>();
		boolean[][][] visited = new boolean[N][M][K + 1]; // 행, 열, 벽 부순 횟수

		queue.offer(new Coord(0, 0, 0, 1));
		visited[0][0][0] = true;

		while (!queue.isEmpty()) {
			Coord curr = queue.poll();
			int cr = curr.r;
			int cc = curr.c;
			int ck = curr.k;
			int cm = curr.m;

			if (cr == N - 1 && cc == M - 1) 
				return cm;

			for (int d = 0; d < 4; ++d) {
				int nr = cr + dr[d];
				int nc = cc + dc[d];

				if (!inRange(nr, nc, N, M))
					continue;

				if (map[nr][nc] == '0' && !visited[nr][nc][ck]) { // 벽을 부술 필요가 없는 경우
					queue.offer(new Coord(nr, nc, ck, cm + 1));
					visited[nr][nc][ck] = true;
				} else if (map[nr][nc] == '1' && ck + 1 <= K && !visited[nr][nc][ck + 1]){ // 벽을 부술 수 있는 경우
					queue.offer(new Coord(nr, nc, ck + 1, cm + 1));
					visited[nr][nc][ck + 1] = true;
				}

			}
		}

		return -1;
	}

	static boolean inRange(int r, int c, int N, int M) {
		return r >= 0 && c >= 0 && r < N && c < M;
	}

	static class Coord {
		int r, c, k, m; // row, column, 벽 부순 횟수, 이동 횟수

		Coord(int r, int c, int k, int m) {
			this.r = r;
			this.c = c;
			this.k = k;
			this.m = m;
		}
	}

}
