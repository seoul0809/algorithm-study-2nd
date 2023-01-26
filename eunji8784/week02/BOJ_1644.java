import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	static int N, Ans;
	static boolean isPrimeNum[];

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		Ans = 0;

		if (N != 1) {
			getPrimeNum();
			Solution();
		}

		System.out.println(Ans);

	}

	private static void Solution() {

		int idxL = 2;
		int idxR = 2;
		int sum = 2;

		while (true) {

			if (sum <= N) {
				if (sum == N) {
					Ans++;
				}
				idxR++;
				while (idxR <= N && isPrimeNum[idxR]) {
					idxR++;
				}
				if (idxR > N) {
					break;
				}
				sum += idxR;
			} else if (sum > N) {
				sum -= idxL;
				idxL++;
				while (isPrimeNum[idxL]) {
					idxL++;
				}
			}
            
		}

	}

	private static void getPrimeNum() {

		// 에라토스테네스의 체
		isPrimeNum = new boolean[N + 1];

		// true: 소수 X / false: 소수
		isPrimeNum[0] = true;
		isPrimeNum[1] = true;

		for (int i = 2; i <= Math.sqrt(N); i++) {
			for (int j = 2; j <= N / i; j++) {
				if (!isPrimeNum[i * j]) {
					isPrimeNum[i * j] = true;
				}
			}
		}

	}

}