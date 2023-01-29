import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, S, min;
	static int[] lst;
	static boolean flag;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		min = Integer.MAX_VALUE;
		lst = new int[N];
		flag = false;

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			lst[i] = Integer.parseInt(st.nextToken());
		}

		Solution();

		if (flag) {
			System.out.println(min);
		} else {
			System.out.println(0);
		}
	}

	private static void Solution() {

		int start = 0;
		int end = 0;

		int sum = lst[0];

		while (true) {

			if (sum < S) {
				if (end == N - 1) {
					break;
				}
				end++;
				sum += lst[end];
			} else if (sum >= S) {
				int tmp = end - start + 1;
				min = Math.min(min, tmp);
				
				if (start == end) {
					start++;
					end++;
					sum = lst[start];
				} else {
					sum -= lst[start];
					start++;
				}

				flag = true;
			}

			if (sum >= S) {
				int tmp = end - start + 1;
				min = Math.min(min, tmp);
			}

			if (start == N - 1 && end == N - 1) {
				break;
			}

		}

	}

}