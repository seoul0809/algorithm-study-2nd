import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 https://www.acmicpc.net/problem/1806
 메모리 : 24460KB, 시간 : 288ms
 
 투포인터로 시작점과 끝점을 설정
 0.5초 제한이기 때문에 for문으로 sum을 구하면 안됨, 문제 제목처럼 누적합 이용
 sum이 S보다 작으면 sum에 값 누적 후 끝점++
 sum이 S보다 크거나 같으면 sum에서 값을 빼준 후 시작점++
 */

public class BOJ_1806 {

	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int sum = 0;
		int min = N+1;
		
		int p1 = 0;
		int p2 = 0;
		
		while(p1 <= N && p2 <= N) {
			if(sum >= S) min =  min > p2-p1? p2-p1 : min;
			
			if(sum < S) sum += arr[p2++];
			else sum -= arr[p1++];
		}
		
		System.out.println(min==N+1?0:min);

	}

}
