import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
/*
 https://www.acmicpc.net/problem/2473
 메모리 : 17300KB / 시간 : 256ms
 
 3개를 고르는 것이라서 이중 for문 돌리고 이분탐색으로 남은 한 개를 고르려고 했지만 시간복잡도가 O(n2logn)가 되므로 불가능.
 투포인터를 사용하여 풀이
 */
public class BOJ_2473 {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		long[] arr = new long[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			arr[i] = Long.parseLong(st.nextToken());
		}
		
		Arrays.sort(arr);
		
		long sum = 0L;
		long min = 3000000000L;
		long a = 0L;
		long b = 0L;
		long c = 0L;
		
		loop:for (int i = 0; i < N-2; i++) {
			int low = i;
			int high = N-1;
			int mid = i+1;
			while(mid < high) {
				sum = arr[low] + arr[mid] + arr[high];
				if(min > Math.abs(sum)) {
					min = Math.abs(sum);
					a = arr[low];
					b = arr[mid];
					c = arr[high];
				}
				if(sum == 0) {
					break loop;
				} else if(sum > 0) high--;
				else mid++;
			}
		}
		
		System.out.println(a+" "+b+" "+c);

	}

}
