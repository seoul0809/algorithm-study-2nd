package B형특강;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class SWEA_공통조상 {

    static int V, E, A, B;
    static Node[] nodes;
    static List<Integer> ancestorA, ancestorB;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringTokenizer st;

        for (int tc = 1; tc <= T; tc++) {
            // 정점의 개수 V(10 ≤ V ≤ 10000), 간선의 개수 E, 공통 조상을 찾는 두 개의 정점 번호 (A,B).
            st = new StringTokenizer(br.readLine());
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            nodes = new Node[V+1];
            ancestorA = new ArrayList<>();
            ancestorB = new ArrayList<>();

            for (int i = 0; i < V + 1; i++) {
                nodes[i] = new Node();
            }

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < E; i++) {
                int p = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());

                nodes[p].children.add(c);
                nodes[c].parents = p;
            }

            // 조상 리스트
            traverse(A, ancestorA);
            traverse(B, ancestorB);

            int ans = 0;
            for (int i = 0; i < V; i++) {
                if(!ancestorA.get(i).equals(ancestorB.get(i))) break;
                ans = ancestorA.get(i);
            }
            System.out.printf("#%d %d %d\n", tc, ans, dfs(ans));
        }
    }

    // 서브트리 개수 구하기
    public static int dfs(int idx){
        if(nodes[idx].children.size() == 0) return 1;
        int res = 1;
        // 자식 노드의 서브트리 개수를 구하는 방법
        for (int child : nodes[idx].children) {
            res += dfs(child);
        }
        return res;
    }

    public static void traverse(int idx, List<Integer> ancestor){
        int parent = nodes[idx].parents;
        if(parent != 0){
            traverse(parent, ancestor);
        }
        // 루트 노드부터 순서대로 조상 추가됨
        ancestor.add(idx);
    }

    public static class Node {
        List<Integer> children;
        int parents;

         Node() {
            this.children = new ArrayList<>();
            this.parents = 0;
        }
    }
}
/*

*/

