import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int left, right, min, ansL, ansR;
	static int[] arr;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		min = Integer.MAX_VALUE;
		left = 0;
		right = N - 1;
		ansL = 0;
		ansR = 0;
		Solution();
		System.out.println(arr[ansL] + " " + arr[ansR]);
	}

	private static void Solution() {

		while (left != right) {
			int sum = arr[left] + arr[right];
			if (min >= Math.abs(sum)) {
				min = Math.abs(sum);
				ansL = left;
				ansR = right;
			}
			if (sum >= 0) {
				right--;
			} else if (sum < 0) {
				left++;
			}
		}

	}

}