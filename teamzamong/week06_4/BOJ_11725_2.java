import java.util.*;
import java.io.*;

/*
BOJ 11725: 트리의 부모 찾기
- 메모리: (BFS) 57732 KB / (DFS) 64696 KB
- 시간: (BFS) 612 ms / (DFS) 636 ms

[문제]
루트 없는 트리가 주어졌을 때, 각 노드의 부모를 구하라.
트리의 루트는 1이다.

입력
- 노드 개수: N (2 ≤ N ≤ 100,000)
- 트리 상 연결된 두 정점: N-1개 주어짐

[설계]
입력으로 들어온 간선 정보로 그래프를 만든 뒤, 루트인 1번 노드부터 순회하면 되는 문제다.
노드 개수에 비해 간선의 개수가 적기 때문에 인접 리스트를 사용해 풀었다.
- adjList[n]: n번째 노드가 연결된 다른 노드 목록
- parents[n]: n번째 노드의 부모 노드
- visited[n]: n번째 노드 순회 여부
 */

public class BOJ_11725_2 {

	static List<Integer>[] adjList;
	static int[] parents;
	static boolean[] visited;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine().trim());

		adjList = new List[N + 1];
		parents = new int[N + 1];
		visited = new boolean[N + 1];

		for (int i = 1; i <= N; ++i) {
			adjList[i] = new ArrayList<>();
		}

		for (int i = 0; i < N - 1; ++i) {
			st = new StringTokenizer(br.readLine(), " ");

			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			adjList[a].add(b);
			adjList[b].add(a);
		}

		bfs(1);
		// dfs(1);

		StringBuilder sb = new StringBuilder();
		for (int i = 2; i <= N; ++i) {
			sb.append(parents[i]).append("\n");
		}

		System.out.print(sb);
	}

	static void bfs(int start) {
		Queue<Integer> queue = new ArrayDeque<>();
		queue.offer(start);
		visited[start] = true;

		while (!queue.isEmpty()) {
			int curr = queue.poll();

			for (int next : adjList[curr]) {
				if (visited[next])
					continue;

				visited[next] = true;
				parents[next] = curr;

				queue.offer(next);
			}
		}
	}

	static void dfs(int curr) {
		visited[curr] = true;

		for (int next : adjList[curr]) {
			if (visited[next])
				continue;

			parents[next] = curr;
			dfs(next);
		}
	}
}

