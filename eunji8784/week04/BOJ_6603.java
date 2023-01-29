import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_6603 {
	
	static int k, S[], selected[];

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		while (true) {
			
			st = new StringTokenizer(br.readLine(), " ");
			k = Integer.parseInt(st.nextToken());
			if (k == 0) {
				break;
			}
			S = new int[k];
			selected = new int[6];
			for (int i = 0; i < k; i++) {
				S[i] = Integer.parseInt(st.nextToken());
			}
			
			Combination(0, 0);
			System.out.println();
			
		}

	}

	private static void Combination(int index, int count) {
		
		if (count == 6) {
			for (int i = 0; i < 6; i++) {
				System.out.print(selected[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = index; i < k; i++) {
			selected[count] = S[i];
			Combination(i + 1, count + 1);
		}
		
	}

}
