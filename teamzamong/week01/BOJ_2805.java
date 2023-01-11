import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * BOJ 2805: 나무 자르기
 * - 메모리: 123276KB
 * - 시간: 548ms
 *
 * [문제]
 * N개의 나무가 주어졌을 때, 절단기를 땅으로부터 H미터로 하여 나무를 자르려고 한다.
 * 이때, 최소 M 미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값.
 *
 * [풀이]
 * - Parametric Search: 조건을 만족하는 최솟값/최댓값을 구하는 문제를 결정 문제로 변환해 이분탐색을 수행하는 방법
 * => 절단기의 높이가 H일 때, 가져갈 수 있는 나무의 길이가 M 이상인가 아닌가?
 *
 * 이분탐색의 범위를 인덱스가 아닌 H의 최댓값과 최솟값으로 설정해 풀이하는 문제
 *
 * [느낀 점]
 * - 강의에서 마지막에 다룬 문제랑 같은 문제였다... 강의를 듣고 풀자!!
 * - Array.sort()를 한 이후에 이분탐색을 시도했을 경우 1000ms 정도 나왔는데, 최댓값만 구해서 진행한 경우 500ms대로 줄어들었다.
 *   나무길이-절단기높이 < 0인 경우 때문에 정렬을 했던 건데, 정렬(O(NlogN))보다 O(N)으로 반복문 돌리는 게 더 효율적인 게 맞다 :(
 */

public class BOJ_2805 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        long maxTree = 0;
        long[] trees = new long[N];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; ++i) {
            trees[i] = Long.parseLong(st.nextToken());
            if (trees[i] > maxTree) maxTree = trees[i];
        }

        System.out.println(binarySearch(trees, M, maxTree));
    }

    private static long binarySearch(long[] trees, int M, long max) {
        long start = 0;
        long end = max;

        while (start < end) {
            long mid = (start + end + 1) / 2; // +1 안 해주면 end-start = 1일 때 무한 루프 발생 가능

            if (parametricSearch(trees, mid, M)) {
                start = mid;
            } else {
                end = mid - 1; // mid 이상인 값은 답이 될 수 없음
            }
        }
        return start;
    }

    private static boolean parametricSearch(long[] trees, long cut, int M) {
        long total = 0;

        for (int i = trees.length - 1; i >= 0; --i) {
            if (trees[i] <= cut) continue;
            total += trees[i] - cut;
        }

        return total >= M;
    }

}
