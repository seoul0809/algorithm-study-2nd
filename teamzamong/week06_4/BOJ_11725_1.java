import java.util.*;
import java.io.*;

/*
BOJ 11725: 트리의 부모 찾기
- 메모리: (BFS) 55972 KB / (DFS) 63568 KB
- 시간: (BFS) 608 ms / (DFS) 696 ms

[문제]
루트 없는 트리가 주어졌을 때, 각 노드의 부모를 구하라.
트리의 루트는 1이다.

입력
- 노드 개수: N (2 ≤ N ≤ 100,000)
- 트리 상 연결된 두 정점: N-1개 주어짐

[설계]
입력으로 들어온 간선 정보로 그래프를 만든 뒤, 루트인 1번 노드부터 순회하면 되는 문제다.

각 노드를 Node 클래스로 표현해 다음과 같이 풀었다.
- int index: 해당 노드의 번호
- Node parent: 부모 노드
- List<Node> connected: 연결된 노드 목록

추가적인 Node[], visited[]을 사용해 노드 목록 및 방문 여부를 판단했다.

[후기]
LinkedList 말고 ArrayList 쓰는 게 빠르다. 거의 200ms 차이 나는 걸 기억하자.

BFS보다 DFS가 시간과 메모리를 더 많이 먹는다.
트리 구조에 따라 다르긴 하겠지만, 트리 순회 시 최악의 경우 N-1번의 depth가 발생할 수도 있기 때문에 BFS가 낫다.

의외인 점은, 당연히 2번 풀이보다 메모리도 시간도 더 오래 걸릴 거라 예상했다.
왜냐하면 추가로 Node[]도 쓰고, Node 객체로 써서 참조도 계속 발생하니까.
근데 BFS는 아주 조금 빠르다... 대체 왜 때문일까... static 변수를 계속 갖다써서 그런 거라고 예상 중이다.
BFS 시간 차이는 미미하고 DFS 시간 차는 많이 나니까 다음부터는 Node보다는 2번 풀이처럼 풀자. 끝!
 */

public class BOJ_11725_1 {

	static Node[] nodes;
	static boolean[] visited;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine().trim());

		nodes = new Node[N + 1];
		visited = new boolean[N + 1];

		for (int i = 0; i <= N; ++i) {
			nodes[i] = new Node(i);
		}

		for (int i = 0; i < N - 1; ++i) {
			st = new StringTokenizer(br.readLine(), " ");

			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			nodes[a].connected.add(nodes[b]);
			nodes[b].connected.add(nodes[a]);
		}

		// dfs(nodes[1]);
		bfs(nodes[1]);

		StringBuilder sb = new StringBuilder();
		for (int i = 2; i <= N; ++i) {
			sb.append(nodes[i].parent.index).append("\n");
		}

		System.out.println(sb);
	}

	static void bfs(Node start) {
		Queue<Node> queue = new ArrayDeque<>();

		queue.offer(start);
		visited[start.index] = true;

		while (!queue.isEmpty()) {
			Node curr = queue.poll();

			for (Node next : curr.connected) {
				if (visited[next.index])
					continue;

				next.parent = curr;
				queue.offer(next);
				visited[next.index] = true;
			}
		}
	}

	static void dfs(Node curr) {
		visited[curr.index] = true;

		for (Node next : curr.connected) {
			if (visited[next.index])
				continue;

			next.parent = curr;
			dfs(next);
		}
	}

	static class Node {
		int index;
		Node parent;
		List<Node> connected = new LinkedList<>();

		Node(int index) {
			this.index = index;
		}
	}
}

