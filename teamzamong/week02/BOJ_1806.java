import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * BOJ 1806: 부분합
 * - 메모리: 23876 KB
 * - 시간: 304 ms
 *
 * [문제]
 * 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어졌을 때,
 * 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하여라
 *
 * [풀이]
 * BOJ 2003 수들의 합2 문제와 동일하게 투 포인터 방식으로 풀이하면 된다.
 * 다만 주의할 점은, S와 값이 같은 부분합을 구하는 것이 아니라 값이 S 이상인 것을 구해야 한다.
 */

public class BOJ_1806 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] nums = new int[N];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; ++i) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(getSubtotalMinLength(nums, S));
    }

    private static int getSubtotalMinLength(int[] nums, int S) {
        int min = Integer.MAX_VALUE;
        int start = 0, end = 0, subtotal = 0;
        int length = nums.length;

        while (true) {
            if (subtotal >= S) {
                if (end - start < min) {
                    min = end - start;
                }
                subtotal -= nums[start++];
            } else if (end == length) {
                break;
            } else {
                subtotal += nums[end++];
            }
        }

        return min == Integer.MAX_VALUE ? 0 : min;
    }
}
