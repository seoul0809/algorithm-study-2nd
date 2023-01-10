import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
https://www.acmicpc.net/problem/2805
시간-540ms / 메모리-1193308KB
 */

public class BOJ_2805 {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
			
		st = new StringTokenizer(br.readLine());
		
		int[] trees = new int[N];
		int low = 0;
		int high = 0;
		
		for (int i = 0; i < N; i++) {
			int temp = Integer.parseInt(st.nextToken());
			trees[i] = temp;
			high = high < temp? temp : high;
		}
		
		int mid = 0;
		
		while(low < high) {
			long sum = 0;
			mid = (low+high)/2;
			for (int i : trees) {
				sum += i > mid? i-mid:0;
			}
			if(sum < M) high = mid; 
			else low = mid+1;
		}
		System.out.println(low-1);
	}

}
