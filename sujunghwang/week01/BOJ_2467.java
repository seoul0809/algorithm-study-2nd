import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2467 {

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 
		int N = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());

		int[] arr = new int[N];

		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int mid = 0;
		int ans = Integer.MAX_VALUE;
		int[] ans_arr = new int[2];
		loop:for (int i = 0; i < N-1; i++) {
			int low = i+1;
			int high = N;
			int target = arr[i] * -1;
			while(low < high) {
				mid = (low+high)/2;
				if(ans > Math.abs(arr[mid] + arr[i])) {
					ans = Math.abs(arr[mid] + arr[i]);
					ans_arr[0] = arr[i];
					ans_arr[1] = arr[mid];
				}
				if(arr[mid] == target) break loop;
				else if(arr[mid] > target) high = mid;
				else low = mid+1;
			}
		}
		System.out.println(ans_arr[0] + " " + ans_arr[1]);
		
	}

}
