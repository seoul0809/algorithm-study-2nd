import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N, M, lst[], Ans;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		lst = new int[N];
		Ans = 0;

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			lst[i] = Integer.parseInt(st.nextToken());
		}

		Solution();

		System.out.println(Ans);

	}

	private static void Solution() {

		int idxL = 0;
		int idxR = 0;
		int sum = lst[0];

		while (true) {

			if (sum >= M) {
				if (sum == M) {
					Ans++;
				}
				if (idxL + 1 <= idxR) {
					sum -= lst[idxL];
					idxL++;
					continue;
				}
			}
			idxR++;
			if (idxR == N) {
				break;
			}
			sum += lst[idxR];

		}

	}

}