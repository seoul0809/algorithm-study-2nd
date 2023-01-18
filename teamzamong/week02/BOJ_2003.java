import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * BOJ 2003: 수들의 합 2
 * - 메모리: 15056 KB
 * - 시간: 148 ms
 *
 * [문제]
 * N개의 수로 된 수열 A[1], A[2], ..., A[N]이 주어졌을 때,
 * 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수
 *
 * [풀이]
 * BOJ 1644 소수의 연속합 문제와 동일하게 투 포인터 방식으로 풀이하면 된다.
 * 만약 부분합이 N보다 크거나 같다면 범위를 줄이고, N보다 작다면 범위를 늘려서 확인한다.
 */

public class BOJ_2003 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        int[] nums = new int[N];
        for (int i = 0; i < N; ++i) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(getSubtotalCount(nums, M));
    }

    private static int getSubtotalCount(int[] nums, int M) {
        int count = 0, start = 0, end = 0, subtotal = 0;
        int length = nums.length;

        while (true) {
            if (subtotal >= M) {
                subtotal -= nums[start++];
            } else if (end == length) {
                break;
            } else {
                subtotal += nums[end++];
            }

            if (subtotal == M) {
                ++count;
            }
        }

        return count;
    }
}
