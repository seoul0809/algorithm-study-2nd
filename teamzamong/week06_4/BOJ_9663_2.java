import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * BOJ 9663: N-Queen
 * - 메모리: 14848 KB
 * - 시간: 2480 ms
 *
 * N * N 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓을 수 있는 방법의 수
 * - 1 <= N < 15
 *
 * [설계]
 * 퀸은 가로, 세로, 대각선 방향으로 이동할 수 있다. 따라서, 퀸들이 같은 행, 열, 대각선에 없도록 배치하면 된다.
 * 모든 행에 퀸이 한 개씩 있어야 N * N 체스판 위에 퀸 N개를 놓을 수 있다.
 *
 * 같은 열 및 대각선에 이미 퀸이 놓여있는지 확인하기 위해 추가 1차원 배열을 사용했다.
 * 대각선에 있는 각 좌표 (r, c)에 대해 같은 대각선 상에 있다면 r - c 값이 동일하다.
 * 
 * 1. colState[c]
 *   - c: 체스판 각 열의 인덱스
 *   - colState[c]: 각 열에 대해 퀸이 놓였는지 여부
 *   
 * 2. rightDiagState[d]: 
 *   - d: 좌표 (r, c)가 있을 때, r - c
 *   - rightDiagState[d]: 오른쪽 위 대각선에 대해 퀸이 놓였는지 여부
 *   
 * 3. leftDiagState[d]:
 *   - d: 좌표 (r, c)가 있을 때, r - c + N - 1 
 *        r - c 값이 음수라서 이를 0 ~ 2 * N - 1 범위 내 값으로 변환
 *   - leftDiagState[d]: 왼쪽 위 대각선에 대해 퀸이 놓였는지 여부
 *
 * [후기]
 * https://blog.encrypted.gg/945 참조.
 * 같은 대각선에 퀸이 놓여져 있는지 여부를 반복문이 아니라 1차원 배열로 표현했더니 시간이 많이 줄어들었다.
 */
public class BOJ_9663_2 {

	static int N, count;
	static boolean[] colState;
	static boolean[] rightDiagState;
	static boolean[] leftDiagState;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine().trim());
		colState = new boolean[N];
		rightDiagState = new boolean[2 * N];
		leftDiagState = new boolean[2 * N];

		solve(0);

		System.out.println(count);
	}

	static void solve(int row) {
		if (row == N) { // 기저 조건: 모든 행에 퀸을 놓았을 때
			++count;
			return;
		}

		for (int col = 0; col < N; ++col) { // 모든 열에 대해 퀸을 놓을 수 있는지 확인
			// 1) 같은 열 2) 같은 오른쪽 위 대각선 3) 같은 왼쪽 위 대각선에 이미 퀸이 놓여진 경우
			if (colState[col] || rightDiagState[row + col] || leftDiagState[row - col + N - 1])
				continue;

			// 각 배열에 퀸 존재 여부 표시
			colState[col] = true;
			rightDiagState[row + col] = true;
			leftDiagState[row - col + N - 1] = true;

			solve(row + 1);

			colState[col] = false;
			rightDiagState[row + col] = false;
			leftDiagState[row - col + N - 1] = false;
		}
	}
}