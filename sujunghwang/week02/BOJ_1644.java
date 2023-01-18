import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BOJ_1644 {
/*
 https://www.acmicpc.net/problem/1644
 메모리 : 27288KB, 시간 : 280ms
 
 에라토스테네스의 체를 이용해서 1~N까지의 소수를 모두 구하고, 
 구해진 소수 중 큰 값부터 loop 돌면서 해당 수를 포함해서 N을 만들 수 있는지 보기
 */
	public static void main(String[] args) throws Exception{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		boolean sosu[] = new boolean[N+1];
		
		for (int i = 2; i < N+1; i++) {
			if(sosu[i]) continue;
			for (int j = i*2; j < N+1; j+=i) {
				sosu[j] = true;
			}
		}
		
		List<Integer> list = new ArrayList<>();
		
		for (int i = N; i > 1; i--) {
			if(!sosu[i]) list.add(i);
		}
		int sum = 0;
		int cnt = 0;
		for (int i = 0, len = list.size(); i < len; i++) {
			sum = 0;
			int temp = i;
			while(sum <= N && temp < len) {
				sum += list.get(temp++);
				if(sum == N) {
					cnt++;
					break;
				}
			}
		}
		System.out.println(cnt);
	}

}
