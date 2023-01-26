import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static long M, Ans;
	static long[] trees;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		trees = new long[N];
		long max = Integer.MIN_VALUE;

		st = new StringTokenizer(br.readLine(), " ");

		for (int i = 0; i < N; i++) {
			trees[i] = Integer.parseInt(st.nextToken());
			max = Math.max(trees[i], max);
		}

		Ans = Solution(0, max);

		System.out.println(Ans);

	}

	private static long Solution(long low, long high) {

		while (low <= high) {
			long mid = (low + high) / 2;
			long sum = 0;
			for (int i = 0; i < N; i++) {
				if (trees[i] > mid) {
					sum += trees[i] - mid;
				}
			}
			
			if (sum < M) {
				high = mid - 1;
			} else {
				low = mid + 1;
			}
		}
		
		return high;

	}

}