import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/*
  https://www.acmicpc.net/problem/2110
  메모리 : 29028KB, 시간 : 312ms
  
  최대 거리를 타겟으로 이분탐색
 */

public class BOJ_2110 {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		Arrays.sort(arr);
		
		int low = 1;
		int high = arr[N-1] - arr[0];
		int ans = 0;
		
		while(low <= high) {
			int mid = (low+high)/2;
			int cnt = 1;
			int pre = arr[0];
			
			for (int i = 1; i < N; i++) {
				if(arr[i]-pre >= mid) {
					cnt++;
					pre = arr[i];
				}
			}
			
			if(cnt >= C) {
				ans = mid;
				low = mid + 1;
			} else high = mid -1;
		}
		
		System.out.println(ans);

	}

}
