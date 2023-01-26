import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, d, k, c, belt[], max;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		// 접시 수
		N = Integer.parseInt(st.nextToken());
		// 초밥의 가짓수
		d = Integer.parseInt(st.nextToken());
		// 연속해서 먹는 접시의 수
		k = Integer.parseInt(st.nextToken());
		// 쿠폰 번호
		c = Integer.parseInt(st.nextToken());
		belt = new int[N];
		max = 1;

		for (int i = 0; i < N; i++) {
			belt[i] = Integer.parseInt(br.readLine());
		}

		Solution();
		System.out.println(max);

	}

	private static void Solution() {

		int startIdx = 0;
		int endIdx = 1;
		int count = 1;
		boolean check[] = new boolean[d + 1];
		int checkNum[] = new int[d + 1];
		check[belt[startIdx]] = true;
		checkNum[belt[startIdx]] += 1;
		int idx = 2;

		while (startIdx <= N - k) {

			if (!check[belt[endIdx]]) {
				count++;
				check[belt[endIdx]] = true;
			}

			checkNum[belt[endIdx]] += 1;

			if (idx == k) {
				int tmp = count;
				if (!check[c]) {
					tmp++;
				}
				max = Math.max(max, tmp);
				if (max == k + 1) {
					break;
				}
				if (checkNum[belt[startIdx]] < 2) {
					count--;
					check[belt[startIdx]] = false;
				}
				checkNum[belt[startIdx]] -= 1;
				startIdx++;
				endIdx++;
				continue;
			}

			endIdx++;
			idx++;

		}

	}

}