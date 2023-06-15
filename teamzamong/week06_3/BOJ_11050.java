import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * BOJ 11050: 이항 계수 1
 * - 메모리: 14152 KB
 * - 시간: 128 ms
 *
 * 자연수 N, K에 대하여 이항 계수 (N K)를 구하는 문제
 * - 1 <= N <= 10
 * - 0 <= K <= N
 *
 * [후기]
 * 이항 계수란 N! / ((N-K)! * K!)로, 경우의 수 계산할 때 많이 본 친구다.
 * N의 범위가 워낙 작기 때문에 굳이 별개의 배열에다가 factorial 값을 저장하지 않아도 될 것 같지만, 그 편이 편해서 했다.
 */

public class BOJ_11050 {
	static int[] factorial;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		factorial = new int[N + 1];
		calcFactorial(N);

		System.out.println(factorial[N] / (factorial[N - K] * factorial[K]));
	}

	static void calcFactorial(int N) {
		factorial[0] = 1;

		for (int i = 1; i <= N; ++i) {
			factorial[i] = factorial[i - 1] * i;
		}
	}
}
