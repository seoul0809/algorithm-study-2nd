import java.io.*;

/**
 * BOJ 9663: N-Queen
 * - 메모리: 14412 KB
 * - 시간: 4984 ms
 *
 * N * N 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓을 수 있는 방법의 수
 * - 1 <= N < 15
 *
 * [설계]
 * 퀸은 가로, 세로, 대각선 방향으로 이동할 수 있다. 따라서, 퀸들이 같은 행, 열, 대각선에 없도록 배치하면 된다.
 * 모든 행에 퀸이 한 개씩 있어야 N * N 체스판 위에 퀸 N개를 놓을 수 있다.
 *
 * 굳이 2차원 배열을 쓰지 않고, 1차원 배열을 사용해 이를 표현할 수 있다.
 * - int[r] queens
 *   - r: 체스판 각 행의 인덱스 
 *   - int[r]: 체스판의 r번째 행에 놓인 퀸의 열 인덱스
 *
 * 이미 퀸이 놓였는지 여부는 다음과 같이 확인한다.
 * - 행: 행을 하나씩 증가하며 퀸을 놓기 때문에 확인 필요 X
 * - 열: 가능한 모든 열 인덱스를 확인해 놓였는지 확인
 * - 대각선: (r,c)에 대해 같은 대각선에 있는 (a,b)는 |r - a| == |c - b|를 만족한다.
 *
 * [후기]
 * 같은 대각선에 퀸이 놓여져 있는지 여부를 확인하기 위해 반복문을 사용했다.
 */
public class BOJ_9663_1 {

	static int N, count;
	static int[] queens;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine().trim());
		queens = new int[N];

		solve(0);

		System.out.println(count);
	}

	static void solve(int row) {
		if (row == N) { // 기저 조건: 모든 행에 퀸을 놓았을 때
			++count;
			return;
		}

		for (int col = 0; col < N; ++col) { // 모든 열에 대해 퀸을 놓을 수 있는지 확인
			if (!isPlaceable(row, col))
				continue;

			queens[row] = col;
			solve(row + 1);
		}
	}

	static boolean isPlaceable(int row, int col) {
		for (int r = 0; r < row; ++r) {
			// 1) 같은 열 2) 같은 대각선에 이미 퀸이 놓여진 경우
			if (queens[r] == col || row - r == Math.abs(queens[r] - col))
				return false;
		}
		return true;
	}
}
