import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/*
https://www.acmicpc.net/problem/6603
메모리 : 15164 KB,	시간 : 164 ms

n개의 수 중에서 6개의 숫자 조합을 찾는 문제
*/
public class BOJ_6603 {
    static StringBuilder sb = new StringBuilder();
    static int len, arr[], result[];
    static boolean[] visit;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            String temp = br.readLine();
            if (temp.equals("0")) break;

            StringTokenizer st = new StringTokenizer(temp);
            len = Integer.parseInt(st.nextToken());
            arr = new int[len];

            for (int i = 0; i < len; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
            result = new int[6];
            visit = new boolean[len];

            dfs(0,0);
            sb.append("\n");
        }
        System.out.print(sb);
    }

    public static void dfs(int count, int start){
        if (count==6){
            for (int i : result) {
                sb.append(i+" ");
            }
            sb.append("\n");
            return;
        }
        for (int i = start; i < len; i++) {
            if (!visit[i]){
                visit[i] = true;
                result[count] = arr[i];
                dfs(count+1, i);
                visit[i] = false;
            }
        }
    }
}

