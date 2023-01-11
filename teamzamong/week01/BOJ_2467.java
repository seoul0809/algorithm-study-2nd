import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * BOJ 2467: 용액
 * - 메모리: 28556KB
 * - 시간: 356ms
 *
 * 정렬된 숫자가 주어졌을 때, 두 숫자의 합이 0에 가장 가까운 경우의 수를 찾는 문제.
 * 이분탐색 문제라고 했지만, 투 포인터로도 풀림...
 *
 * 1. 양쪽 끝에서 시작해서 두 숫자의 합을 구함
 * 2. 두 숫자의 합이 제일 0에 가깝다면, 그 값과 두 숫자를 답으로 저장
 * 3. 두 숫자의 합이 0보다 클 경우 오른쪽 끝을 왼쪽으로, 0보다 작을 경우 왼쪽 끝을 오른쪽으로 이동
 * 4. 포인터가 서로 겹치지 않을 때까지 이 과정을 반복 (같은 숫자를 재사용할 수 없기 때문)
 */

public class BOJ_2467 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 처리. 정렬된 상태로 들어와서 정렬 필요 X
        int N = Integer.parseInt(br.readLine().trim());
        int[] liquids = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; ++i) {
            liquids[i] = Integer.parseInt(st.nextToken());
        }

        int[] ans = findLiquidPair(liquids);

        System.out.println(ans[0] + " " + ans[1]);

    }

    // 투 포인터 방식을 활용해 0에 가까운 합이 나오는 것을 찾기
    // 두 숫자의 합은 int 범위를 넘지 않고, Integer 최댓값보다도 작음
    private static int[] findLiquidPair(int[] liquids) {
        int[] ans = new int[2];
        int best = Integer.MAX_VALUE;

        int start = 0;
        int end = liquids.length - 1;

        while (start < end) {
            int sum = liquids[start] + liquids[end];

            if (Math.abs(sum) < best) { // 현재 선택된 두 숫자의 합이 기존 정답보다 0에 더 가깝다면 갱신
                best = Math.abs(sum);
                ans[0] = liquids[start];
                ans[1] = liquids[end];
            }

            if (sum > 0) {
                --end;
            } else {
                ++start;
            }
        }

        return ans;
    }

}
