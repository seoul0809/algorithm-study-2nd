import java.io.*;
import java.util.*;

/**
 * BOJ 1715: 카드 정렬하기
 * - 메모리: 25608 KB
 * - 시간: 400 ms
 *
 * 카드 묶음 2개가 있을 때, 두 묶음을 합쳐 하나로 만드는 데 A+B (A, B: 각 묶음의 카드 수)번의 비교가 필요하다.
 * N개의 숫자 카드 묶음의 각각 크기가 주어졌을 때, 하나의 묶음으로 만들기 위해 최소한 몇 번 비교가 필요한지 구하기
 * - 1 <= N <= 100,000
 * - 1 <= 숫자 카드 묶음의 크기 < 1,000
 *
 * [설계]
 * 언제나 가장 작은 카드 묶음 2개만 골라서 비교하면 최소 횟수로 하나의 묶음을 만들 수 있다.
 *
 * 주의할 점은 다음과 같다.
 * - 카드 묶음이 하나일 때는 비교가 필요 없다.
 * - 기존의 카드 묶음 + 새로 만들어진 카드 묶음 중에서 가장 작은 카드 묶음 2개를 골라야 한다.
 *
 * PriorityQueue를 사용해서 언제나 가장 작은 카드 묶음 2개를 갖고 올 수 있도록 했다.
 */

public class BOJ_1715 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine().trim());

		// 카드 묶음이 하나인 경우, 비교할 필요 X
		if (n == 1) {
			System.out.println(0);
			return;
		}

		PriorityQueue<Integer> pq = new PriorityQueue<>();
		for (int i = 0; i < n; ++i) {
			pq.add(Integer.parseInt(br.readLine().trim()));
		}

		System.out.println(getLeastCardCompareCount(pq));
	}

	// 카드 묶음을 비교하기 위한 최소 횟수 가져오기
	// int 범위 내에서 해결 가능
	static int getLeastCardCompareCount(PriorityQueue<Integer> pq) {
		int score = 0;

		while (pq.size() > 1) { // 한 개 이상의 카드 묶음이 있을 때
			// 가장 작은 카드 묶음 2개 가져와서 비교하기
			int cardA = pq.poll();
			int cardB = pq.poll();

			score += cardA + cardB;
			pq.add(cardA + cardB); // 새로 만들어진 카드 묶음을 PQ에 넣어 다시 비교할 수 있도록 함
		}

		return score;
	}
}
