import java.util.*;
import java.io.*;

/**
 * BOJ 4153: 직각삼각형
 * - 메모리: 14048 KB
 * - 시간: 124 ms
 *
 * 주어진 3개의 숫자에 대해 직각삼각형인지 판별하는 문제
 *
 * [후기]
 * solved.ac 기준 Class 2+를 채우고 싶어서 푼 문제
 * 다른 사람들 풀이 보니까 삼항연산자를 많이 썼던데, 찾아보니까 성능상으로는 차이가 별로 없고 (기계어로 변환할 때 동일하게 바뀔 수도 있다함)
 * 삼항연산자가 더 간결하고 가독성이 좋을 수 있다고 한다.
 */

public class BOJ_4153 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int a, b, c;
		while (true) {
			st = new StringTokenizer(br.readLine(), " ");

			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());

			if (a == 0 || b == 0 || c == 0)
				break;

			if (a * a + b * b == c * c || b * b + c * c == a * a || c * c + a * a == b * b)
				System.out.println("right");
			else
				System.out.println("wrong");
		}

	}
}
