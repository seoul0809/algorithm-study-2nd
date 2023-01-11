import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * BOJ 2473: 세 용액
 * - 메모리: 15892KB
 * - 시간: 208ms
 *
 * 정렬되지 않은 숫자가 주어졌을 때, 세 숫자의 합이 0에 가장 가까운 경우의 수를 찾는 문제.
 * 
 * BOJ2467 용액과 다른 점은 1) 입력이 정렬되지 않음 2) 숫자를 3개 골라야 함.
 * 동일하게 투포인터 방식으로 풀 수 있지만, 그 대신 한 숫자를 기준점으로 잡은 후 남은 숫자에 대해서 투포인터 방식으로 두 숫자를 찾으면 됨.
 */

public class BOJ_2473 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력 처리
        // 1) 입력이 정렬되지 않았기 때문에 정렬 처리
        // 2) 용액의 합이 int 범위 넘어갈 수 있어서 입력부터 long으로 처리하기로 선택
        int N = Integer.parseInt(br.readLine().trim());
        long[] liquids = new long[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; ++i) {
            liquids[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(liquids);

        long[] ans = findLiquidTriad(liquids);

        System.out.println(ans[0] + " " + ans[1] + " " + ans[2]);
    }

    // 투 포인터 방식을 활용해 0에 가까운 합이 나오는 것을 찾기
    // 세 숫자를 고를 때, 한 숫자를 기준점으로 잡은 후 투포인터로 나머지 두 숫자를 찾음
    private static long[] findLiquidTriad(long[] liquids) {
        long[] ans = new long[3];
        long best = Long.MAX_VALUE;
        int length = liquids.length;

        // 마지막 숫자 2개 제외 모든 숫자를 기준점으로 잡아 계산
        for (int i = 0, fin = length - 2; i < fin; ++i) {
            int start = i + 1;
            int end = length - 1;

            while (start < end) {
                long sum = liquids[i] + liquids[start] + liquids[end];

                if (Math.abs(sum) < best) {
                    best = Math.abs(sum);
                    ans[0] = liquids[i];
                    ans[1] = liquids[start];
                    ans[2] = liquids[end];
                }

                if (sum > 0) {
                    --end;
                } else {
                    ++start;
                }
            }
        }

        return ans;
    }

}
