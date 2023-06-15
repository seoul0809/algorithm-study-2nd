import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/**
 * BOJ 10866: 덱
 * - 메모리: 19808 KB
 * - 시간: 236 ms
 *
 * 정수를 저장하는 덱을 구현한 후, 처리하는 문제
 *
 * [후기]
 * Java에도 Deque을 기본 제공하긴 하나, 배열로 직접 구현해봤다.
 * - front는 원소를 넣을 index를, back은 마지막 원소의 현재 위치를 가리키도록 했다.
 * - 원형 배열을 구현하는 것과 같게, % MAX_DEQUE_SIZE를 해줘서 계속 덱 크기 내에서 index가 왔다갔다 할 수 있도록 했다.
 */
public class BOJ_10866 {
	static final int MAX_DEQUE_SIZE = 10_001;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		Deque deque = new Deque();

		String command;
		int value;
		for (int i = 0; i < N; ++i) {
			st = new StringTokenizer(br.readLine(), " ");

			command = st.nextToken();

			switch (command) {
				case "push_front":
					value = Integer.parseInt(st.nextToken());
					deque.pushFront(value);
					break;
				case "push_back":
					value = Integer.parseInt(st.nextToken());
					deque.pushBack(value);
					break;
				case "pop_front":
					bw.write(deque.popFront() + "\n");
					break;
				case "pop_back":
					bw.write(deque.popBack() + "\n");
					break;
				case "size":
					bw.write(deque.getSize() + "\n");
					break;
				case "empty":
					bw.write((deque.isEmpty() ? 1 : 0) + "\n");
					break;
				case "front":
					bw.write(deque.getFront() + "\n");
					break;
				case "back":
					bw.write(deque.getBack() + "\n");
					break;
				default:
					// do nothing
			}
		}

		bw.flush();
		bw.close();
	}

	static class Deque {
		private final int[] elements;
		private int front;
		private int back;
		private int size;

		public Deque() {
			this.elements = new int[MAX_DEQUE_SIZE];
			this.front = 0;
			this.back = 0;
			this.size = 0;
		}

		public void pushFront(int X) {
			this.elements[this.front] = X;
			this.front = (this.front - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
			++this.size;
		}

		public void pushBack(int X) {
			this.back = (this.back + 1) % MAX_DEQUE_SIZE;
			this.elements[this.back] = X;
			++this.size;
		}

		public int popFront() {
			if (this.isEmpty())
				return -1;

			this.front = (this.front + 1) % MAX_DEQUE_SIZE;
			--this.size;

			return this.elements[this.front];
		}

		public int popBack() {
			if (this.isEmpty())
				return -1;

			int prevBack = this.back;
			this.back = (this.back - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
			--this.size;

			return this.elements[prevBack];
		}

		public int getSize() {
			return this.size;
		}

		public boolean isEmpty() {
			return this.front == this.back;
		}

		public int getFront() {
			if (this.isEmpty())
				return -1;
			return this.elements[(this.front + 1) % MAX_DEQUE_SIZE];
		}

		public int getBack() {
			if (this.isEmpty())
				return -1;
			return this.elements[this.back];
		}
	}
}
