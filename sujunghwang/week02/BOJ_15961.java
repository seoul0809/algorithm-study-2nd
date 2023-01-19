import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
/*
https://www.acmicpc.net/problem/15961
메모리 : 171108 KB, 시간 : 552 ms

초밥의 개수를 for문을 돌려서 찾으려고 하면 시간 초과나기 때문에
길이가 초밥의 가짓수+1인 배열을 만들어서 체크한다.
*/
public class BOJ_15961 {

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		int len = N+k-1;
		int[] sushi = new int[len];

		for (int i = 0; i < N; i++) {
			sushi[i] = Integer.parseInt(br.readLine());
		}

		for (int i = 0; i < k-1; i++) {
			sushi[N+i] = sushi[i];
		}

		int[] check = new int[d+1];
		check[c] = 1;
		int max = 1;

		for (int i = 0; i < k; i++) {
			if(check[sushi[i]] == 0) max++;
			check[sushi[i]]++;
		}

		int p1 = 0;
		int sum = max;

		for (int i = k; i < len; i++) {
			check[sushi[p1]]--;
			if(check[sushi[p1++]]==0) sum--;

			if(check[sushi[i]]==0) sum++;
			check[sushi[i]]++;

			max = max < sum ? sum : max;
		}
		System.out.println(max);

	}

}
