import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	static int N, AnsL, AnsM, AnsH;
	static long arr[], min;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		arr = new long[N];
		min = Long.MAX_VALUE;

		for (int i = 0; i < N; i++) {
			arr[i] = Long.parseLong(st.nextToken());
		}

		Arrays.sort(arr);

		Solution();

		System.out.println(arr[AnsL] + " " + arr[AnsM] + " " + arr[AnsH]);

	}

	private static void Solution() {

		for (int low = 0; low < N - 2; low++) {

			int mid = low + 1;
			int high = N - 1;

			while (mid != high) {

				long sum = arr[low] + arr[mid] + arr[high];

				if (Math.abs(sum) < min) {
					min = Math.abs(sum);
					AnsL = low;
					AnsM = mid;
					AnsH = high;
				}

				if (sum >= 0) {
					high--;
				} else {
					mid++;
				}

			}

		}

	}

}