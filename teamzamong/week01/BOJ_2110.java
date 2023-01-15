import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * BOJ 2110: 공유기 설치
 * - 메모리: 28520KB
 * - 시간: 320ms
 *
 * [문제]
 * 집 N개가 수직선 위에 있고, 공유기 C개를 N개의 집에 적당히 설치한다고 할 때, 
 * 가장 인접한 두 공유기 사이의 거리의 최댓값.
 * 
 * [풀이]
 * - Parametric Search: 조건을 만족하는 최솟값/최댓값을 구하는 문제를 결정 문제로 변환해 이분탐색을 수행하는 방법
 * => 가장 인접한 두 공유기 사이의 거리가 X일 때, 설치해야 할 공유기의 개수가 C개인가?
 *
 * 이분탐색의 범위를 인덱스가 아닌 두 공유기 사이의 거리의 최댓값과 최솟값으로 설정해 풀이하는 문제
 *
 */


public class BOJ_2110 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int[] coords = new int[N];

        for (int i = 0; i < N; ++i) {
            coords[i] = Integer.parseInt(br.readLine().trim());
        }
        Arrays.sort(coords);

        System.out.println(binarySearch(coords, C));
    }

    private static int binarySearch(int[] coords, int C) {
        int start = 1;
        int end = coords[coords.length - 1] - coords[0];

        while (start < end) {
            int mid = (start + end + 1) / 2;

            if (parametricSearch(coords, mid, C)) {
                start = mid;
            } else {
                end = mid - 1;
            }
        }

        return start;
    }

    private static boolean parametricSearch(int[] coords, int dist, int C) {
        int count = 1;
        int idx = coords[0];

        for (int i = 1, end = coords.length; i < end; ++i) {
            if (coords[i] - idx >= dist) {
                ++count;
                idx = coords[i];
            }
        }

        return count >= C;
    }

}
