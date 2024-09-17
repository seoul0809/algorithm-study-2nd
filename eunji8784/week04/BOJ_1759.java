import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1759 {
	
	static int L, C, cnt;
	static char[] arr, selected;
	static char lst[] = {'a', 'e', 'i', 'o', 'u'};

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		L = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		selected = new char[L];
		arr = new char[C];
		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < C; i++) {
			arr[i] = st.nextToken().charAt(0);
		}
		Arrays.sort(arr);
		cnt = 0;
		Com(0, 0, 0);
		
	}

	private static void Com(int index, int count, int cnt) {
		
		boolean flag = false;
		
		if (count == L) {
			if (cnt < 1 || L - cnt < 2 ) {
				return;
			}
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < L; i++) {
				sb.append(selected[i]);
			}
			System.out.println(sb.toString());
			return;
		}
		
		for (int i = index; i < C; i++) {
			selected[count] = arr[i];
			for (char tmp : lst) {
				if (selected[count] == tmp) {
					flag = true;
					cnt++;
				}
			}
			Com(i + 1, count + 1, cnt);
			if (flag) {
				cnt--;
				flag = false;
			}
		}
		
	}

}
