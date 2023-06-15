import java.util.*;
import java.io.*;

/**
 * BOJ 2798: 블랙잭
 * - 메모리: 14060 KB
 * - 시간: 124 ms
 *
 * N장의 카드 중 3장의 카드를 골라, 카드의 합이 M을 넘지 않으면서 M과 최대한 가깝도록 할 때,
 * 최대한 가까운 카드 3장의 합 구하기
 * - 3 <= N <= 100
 * - 10 <= M <= 300,000
 * - 1 <= 카드 값 <= 100,000
 *
 * [설계]
 * N <= 100, 선택해야 하는 카드의 개수가 3장이기 때문에 Brute Force 방식으로 풀 수 있다.
 * 모든 카드 중 3장을 골라 그 합 중 M을 넘지 않으면서 최대한 가까운 값을 구하면 된다.
 *
 * [후기]
 * - 본능적으로 조합으로 풀었는데, 잘 생각해보니 3중 for문으로 풀었어도 시간 상 문제는 없었을 것이다.
 */

public class BOJ_2798 {
	static int maxValue = Integer.MIN_VALUE;
	static int[] cards;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		cards = new int[n];
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < n; ++i) {
			cards[i] = Integer.parseInt(st.nextToken());
		}

		comb(0, 0, 0, n, m);

		System.out.println(maxValue);
	}

	static void comb(int start, int idx, int sum, int n, int m) {
		if (idx == 3) {
			if (sum <= m && maxValue < sum)
				maxValue = sum;
			return;
		}

		for (int i = start; i < n; ++i) {
			comb(i + 1, idx + 1, sum + cards[i], n, m);
		}
	}
}
