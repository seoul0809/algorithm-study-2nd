import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * BOJ 1644: 소수의 연속합
 * - 메모리: 27084 KB
 * - 시간: 200 ms
 *
 * [문제]
 * 자연수 N이 주어졌을 때, 이 자연수를 자신보다 작거나 같은 연속된 소수의 합으로 나타낼 수 있는 경우의 수
 *
 * [풀이]
 * 1. 1~N 범위 내에 있는 모든 소수 구하기 => 에라토스테네스의 체
 * 2. 소수의 연속합 구하기 => 투포인터
 */

public class BOJ1644 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine().trim());

        System.out.println(getSubtotalCount(N));
    }

    // 범위 내에 있는 소수들의 부분합 중 합이 N인 것의 개수 구하기
    private static int getSubtotalCount(int N) {
        List<Integer> primes = findPrimes(N);

        int size = primes.size();

        // 투포인터를 사용해 부분합 개수 구하기
        int count = 0;
        int start = 0;
        int end = 0;
        int subtotal = 0;

        while (true) {
            if (subtotal >= N) { // 만약 부분합이 N보다 크거나 같다면, 범위 줄이기
                subtotal -= primes.get(start++);
            } else if (end == size) {
                break;
            } else { // 만약 부분합이 N보다 작다면, 범위 늘리기 (더 큰 숫자를 더하기)
                subtotal += primes.get(end++);
            }

            if (subtotal == N) {
                ++count;
            }
        }

        return count;
    }


    // 에라토테네스의 체를 사용해서 1~N 사이의 소수 찾기
    private static List<Integer> findPrimes(int N) {
        List<Integer> primes = new ArrayList<>();

        boolean[] notPrime = new boolean[N + 1];
        notPrime[1] = true;

        for (int i = 2; i * i <= N; ++i) {
            if (notPrime[i]) { // 이미 소수 아닌 것으로 판명났을 경우, 확인 X
                continue;
            }

            for (int j = i * i; j <= N; j += i) {
                notPrime[j] = true;
            }
        }

        for (int i = 2; i <= N; ++i) {
            if (!notPrime[i]) {
                primes.add(i);
            }
        }

        return primes;
    }
}
