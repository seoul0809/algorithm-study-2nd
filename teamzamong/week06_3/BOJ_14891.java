import java.io.*;
import java.util.*;

/**
 * BOJ 14891: 톱니바퀴
 * - 메모리: 14312 KB
 * - 시간: 132 ms
 *
 * 4개의 톱니바퀴가 있을 때, 한 톱니바퀴를 돌린 후 다른 톱니바퀴의 상태를 찾는 문제
 * - 맞닿은 톱니의 극이 다를 때 반대 방향으로 회전
 * - 모든 톱니바퀴의 회전 방향을 정한 후, 한꺼번에 회전
 * - 마지막 상태 기준으로 점수 계산
 *
 * [설계]
 * 주어진 조건에 맞게 구현하는 문제
 * - 톱니를 어떤 자료구조로 표현할지 고민을 했는데, 처음에는 Deque가 좋아보였지만 맞닿은 톱니 위치를 찾아낼 수 있는 방법이 없어서 List 선택
 */

public class BOJ_14891 {

	public static void main(String[] args) throws Exception {
		Wheel[] wheels = new Wheel[4];

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int i = 0; i < 4; ++i) {
			wheels[i] = new Wheel(br.readLine());
		}

		int k = Integer.parseInt(br.readLine().trim());

		StringTokenizer st;
		int wheelIndex, wheelDir;
		for (int i = 0; i < k; ++i) {
			st = new StringTokenizer(br.readLine(), " ");
			wheelIndex = Integer.parseInt(st.nextToken());
			wheelDir = Integer.parseInt(st.nextToken());

			turnWheels(wheels, wheelIndex - 1, wheelDir);
		}

		System.out.println(getScore(wheels));
	}

	// 최종 점수 계산
	static int getScore(Wheel[] wheels) {
		int score = 0;

		for (int i = 0; i < 4; ++i) {
			if (wheels[i].getPoints().get(0).equals(1))
				score += Math.pow(2, i);
		}

		return score;
	}

	// 톱니바퀴 회전 시뮬레이션
	static void turnWheels(Wheel[] wheels, int wheelIndex, int wheelDir) {
		// 톱니바퀴 회전 방향 계산
		setWheelsDirection(wheels, wheelIndex, wheelDir);

		// 계산한 회전 방향에 따라 실제 회전 진행
		for (int i = 0; i < 4; ++i) {
			wheels[i].turn();
		}
	}

	// 톱니바퀴 회전 방향 계산
	static void setWheelsDirection(Wheel[] wheels, int wheelIndex, int wheelDir) {
		wheels[wheelIndex].setDirection(wheelDir);

		// 현재 톱니바퀴 기준 오른쪽에 있는 톱니바퀴 확인
		for (int i = wheelIndex + 1; i < 4; ++i) {
			// 만약 이전 톱니바퀴가 회전하지 않았다면 회전할 필요 X
			Wheel prevWheel = wheels[i - 1];
			if (prevWheel.getDirection() == 0)
				break;

			// 맞닿은 톱니의 극 확인, 같지 않다면 회전 방향 설정
			Wheel currWheel = wheels[i];
			if (!prevWheel.getPoints().get(2).equals(currWheel.getPoints().get(6)))
				currWheel.setDirection(prevWheel.getDirection() * -1);

		}

		// 왼쪽 톱니바퀴 확인
		for (int i = wheelIndex - 1; i >= 0; --i) {
			// 만약 이전 톱니바퀴가 회전하지 않았다면 회전할 필요 X
			Wheel prevWheel = wheels[i + 1];
			if (prevWheel.getDirection() == 0)
				break;

			// 맞닿은 톱니의 극 확인, 같지 않다면 회전 방향 설정
			Wheel currWheel = wheels[i];
			if (!prevWheel.getPoints().get(6).equals(currWheel.getPoints().get(2)))
				currWheel.setDirection(prevWheel.getDirection() * -1);
		}

	}

	static class Wheel {
		private final List<Integer> points = new LinkedList<>(); // 톱니바퀴 극 상태
		private int direction; // 회전 방향, 기본 0 (움직이지 않음)

		public Wheel(String state) {
			state.trim();
			for (int i = 0, end = state.length(); i < end; ++i) {
				points.add((int)(state.charAt(i)) - '0');
			}
		}

		public void turn() {
			switch (this.direction) {
				case -1:
					int t1 = this.points.remove(0);
					this.points.add(t1);
					break;
				case 1:
					int t2 = this.points.remove(7);
					this.points.add(0, t2);
					break;
				default:
					// do nothing
			}

			this.direction = 0; // 방향 초기화
		}

		public List<Integer> getPoints() {
			return this.points;
		}

		public int getDirection() {
			return this.direction;
		}

		public void setDirection(int direction) {
			this.direction = direction;
		}
	}
}

