import java.util.*;
import java.io.*;

/**
 * BOJ 2098: 외판원 순회
 * - 메모리: 19936 KB
 * - 시간: 212 ms
 *
 * 1부터 N까지 번호가 매겨져 있는 도시들이 있다. 도시 사이에 길이 있을 수도 없을 수도 있다.
 * 어떤 외판원이 한 도시에서 출발해 N개의 도시를 모두 거쳐 오는 경로 중 최소 비용을 구하라.
 * 단, 방문한 도시는 또 방문할 수 없다. 도시 A에서 도시 B로 가는 비용과 도시 B에서 도시 A로 가는 비용은 다를 수 있다.
 * - 2 <= N <= 16
 *
 * [설계]
 * 완전 탐색으로 풀면 모든 경우의 수를 구하는 것과 같아 O(N!)이 걸리기 때문에 DP로 풀어야 한다.
 *
 * 1. 도시 1에서 시작하나, 도시 N에서 시작하나 결국 모든 도시를 방문하기 때문에 출발 도시는 어떤 것이 되든 상관 없다.
 * 2. 같은 도시에서 출발했을 때, 방문한 도시와 현재 도시가 같다면 남은 도시를 방문하고 돌아가는 최소 비용은 같다.
 *
 * 따라서 다음과 같은 2차원 DP 배열에 최소 비용을 저장해두고 사용하면 된다.
 * - dp[city][visited]
 *   - city: 현재 방문한 도시
 *   - visited: 여태까지 방문한 도시의 집합을 비트마스킹으로 표현한 값
 *   - dp[city][visitedCities]: visited에 표현된 도시를 방문한 상태일 때, 현재 도시에서 남은 도시를 방문하고 출발 도시로 돌아가는 최소 비용
 *
 * 주의할 점
 * - 방문한 도시 집합을 비트마스킹으로 표현하기: 공간 줄어듦
 * - 현재 도시에서 출발 도시까지 길이 없을 수 있으므로 예외 처리
 *
 * DP를 사용하면, 시간 복잡도가 O(N^2 * 2^N)으로 줄어든다.
 * - 가능한 방문 도시 상태 (2차원 DP 배열 채우기): O(N * 2^N) (N개의 도시, 2^N개의 부분집합)
 * - 각 상태에 대한 반복문: O(N)
 */
public class BOJ_2098 {
	private static final int INF = Integer.MAX_VALUE / 2; // overflow 발생하지 않으면서 양의 정수 범위 내인 INF 값 설정

	static int N; // 총 도시 개수
	static int[][] costs; // costs[r][c]: 도시 r에서 도시 c까지 이동하는데 드는 비용
	static int[][] dp; // dp[r][c]: c 집합 내에 있는 도시들을 방문한 상태일 때, 도시 r에서 남은 도시룰 방문하고 출발 도시로 돌아가는 최소 비용

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine().trim());

		// 두 도시 간 이동 거리 입력
		costs = new int[N][N];
		for (int r = 0; r < N; ++r) {
			st = new StringTokenizer(br.readLine(), " ");

			for (int c = 0; c < N; ++c) {
				costs[r][c] = Integer.parseInt(st.nextToken());
			}
		}

		// dp 배열 초기화
		dp = new int[N][(1 << N) - 1]; // 0 ~ (N-1)번째 도시까지 있으니까 (1 << N) - 1. <<이 연산 순서가 더 뒤라 괄호 필수
		for (int[] row : dp) {
			Arrays.fill(row, -1); // 아직 계산하지 않은 값은 -1로 초기화, INF로 하면 실제 비용 계산할 때 나오는 값과 같아 불필요한 연산 발생
		}

		System.out.println(tsp(0, 1));
	}

	/**
	 * DP를 사용해 현재 도시에서 방문하지 않은 도시를 모두 한 번씩 방문하고 출발 도시로 돌아가는 최소 비용을 구한다.
	 *
	 * @param currCity 현재 도시
	 * @param visited 여태까지 방문한 도시의 집합을 비트마스킹으로 표현한 값
	 * @return 현재 도시에서 방문하지 않은 도시를 방문하고 출발 도시로 돌아가는 최소 비용
	 */
	static int tsp(int currCity, int visited) {
		if (visited == ((1 << N) - 1)) { // 기저 조건: 모든 도시를 방문함
			if (costs[currCity][0] == 0) // 현재 도시에서 출발 도시까지 이동할 방법이 없는 경우, INF 반환
				return INF;
			return costs[currCity][0]; // 현재 도시에서 출발 도시까지 드는 비용
		}

		if (dp[currCity][visited] != -1) // 이미 현재 도시 + 방문한 도시 집합에 대한 이동 비용을 이미 계산한 경우
			return dp[currCity][visited];

		dp[currCity][visited] = INF; // 계산 진행 여부 표시

		// 방문하지 않은 다른 도시에 대해 DP 배열 계산하기
		for (int i = 0; i < N; ++i) {
			// 1) 이미 방문했던 도시거나 2) 현재 도시에서 이동할 수 없는 도시인 경우 계산 X
			if ((visited & (1 << i)) != 0 || costs[currCity][i] == 0)
				continue;

			// 아래 두 값 중 최솟값으로 DP 배열을 갱신한다.
			// 1) 현재 도시에서 방문하지 않은 도시를 모두 방문한 후, 출발 도시까지 돌아가는 최소 비용
			// 2) 새로운 도시 i를 방문했다 가정할 때, 도시 i에서 방문하지 않은 도시를 모두 방문한 후 출발 도시까지 돌아가는 최소 비용
			//    + 현재 도시에서 도시 i까지 이동 비용
			dp[currCity][visited] = Math.min(dp[currCity][visited],
				tsp(i, visited | (1 << i)) + costs[currCity][i]);
		}

		return dp[currCity][visited];
	}
}
