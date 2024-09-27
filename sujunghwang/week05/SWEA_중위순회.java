package B형특강;

import java.io.BufferedReader;
import java.io.InputStreamReader;
/*
이진탐색트리로 풀 수 있는 문제
왼쪽은 현재 노드*2, 오른쪽은 현재노드*2+1인 것을 이용하면 쉽게 풀 수 있음
*/
public class SWEA_중위순회 {
    static char[] arr;
    static int n;
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 1; tc <= 10; tc++) {
            sb.append("#" + tc+ " ");

            n = Integer.parseInt(br.readLine());
            arr = new char[n+1];
            for (int i = 1; i <= n; i++) {
                arr[i] = br.readLine().split(" ")[1].charAt(0);
            }
            dfs(1);
            sb.append("\n");
        }
        System.out.println(sb);
    }
    public static void dfs(int cur){

        if(cur > n) return;

        dfs(cur*2);
        sb.append(arr[cur]);
        dfs(cur*2 + 1);
    }
}
