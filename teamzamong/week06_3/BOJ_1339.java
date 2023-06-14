import java.util.*;
import java.io.*;

/**
 * BOJ 1339: 단어 수학
 * - 메모리: 14284 KB
 * - 시간: 128 ms
 *
 * 알파벳 대문자로 이뤄진 N개의 단어가 주어졌을 때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하려고 한다.
 * - 같은 알파벳은 같은 숫자로 바꿔야 한다.
 * - 두 개 이상의 알파벳이 같은 숫자로 바뀌면 안 된다.
 * 이때, 최댓값을 구하자.
 *
 * [설계]
 * 자리만 가지고 계산했을 때, 가장 큰 값을 가진 알파벳에 제일 큰 숫자를 배정하면 된다.
 * 1. 주어진 단어에 대해 각 알파벳의 값을 구해 더한다.
 * 	  ex. ABC = A * 100 + B * 10 + C * 1
 * 2. 모든 단어에 대해 반복한 후, 알파벳별 최종값을 구한다.
 * 3. 최종값이 큰 순서대로 정렬한 후, 9부터 숫자를 배정해 합을 구한다.
 *
 * [기타]
 * - Collections.reverseOrder()를 쓰고 싶어서 Integer[]를 사용할까도 생각했지만, Arrays.fill()을 한 번 더해줘야 해서
 *   primitive type으로 처리함
 */
public class BOJ_1339 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int[] alphabets = new int[26];
		int n = Integer.parseInt(br.readLine().trim());

		String word;
		for (int i = 0; i < n; ++i) {
			word = br.readLine().trim();

			for (int j = 0, end = word.length(); j < end; ++j) {
				// 각 알파벳에 대해 자리에 따라 나오는 값 계산
				alphabets[word.charAt(j) - 'A'] += Math.pow(10, word.length() - 1 - j);
			}
		}

		Arrays.sort(alphabets); // 오름차순으로 정렬

		int number = 9; // 가장 큰 값을 가진 알파벳에 제일 큰 숫자 배정
		int maxValue = 0;
		for (int i = 25; i >= 0; --i) {
			if (alphabets[i] == 0)
				break;

			maxValue += alphabets[i] * number;
			--number;
		}

		System.out.println(maxValue);
	}
}