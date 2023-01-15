import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2003{

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int p1 = 0;
		int p2 = 0;
		int sum = 0;
		int cnt = 0;
		
		while(p1 < N && p2 < N) {
			sum = 0;
			for (int i = p1; i <= p2; i++) {
				sum += arr[i];
			}
			if(sum == M) {
				cnt++;
				p1++;
			}
			else if(sum < M) p2++;
			else p1++;
		}
		System.out.println(cnt);

	}
}
