import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * BOJ 15961: 회전초밥
 * - 메모리: 170872 KB
 * - 시간: 564 ms
 *
 * [문제]
 * 원형으로 배치된 N개의 회전 초밥이 있다. 초밥의 가짓수는 d개이다.
 * 손님이 임의 한 위치로부터 k개의 접시를 연속으로 먹으면, 초밥 c를 추가로 제공한다고 할 때,
 * 손님이 먹을 수 있는 초밥 가짓수의 최댓값은?
 *
 * [풀이]
 * - k개로 초밥의 개수가 정해져 있기 때문에 투포인터보다는 슬라이딩 윈도우로 부르는 게 맞을 거 같음
 *   (둘 차이는 투포인터는 구간의 길이가 변하고, 슬라이딩 윈도우는 고정임)
 * - 보너스 초밥를 어떤 식으로 처리해줄까가 조금 까다롭게 느껴졌던 문제
 */

public class BOJ_15961 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] sushi = new int[N + k - 1]; // 원형 배열 계산하기 위해 배열 늘림
        for (int i = 0; i < N; ++i) {
            sushi[i] = Integer.parseInt(br.readLine().trim());
        }
        for (int i = 0; i < k - 1; ++i) {
            sushi[N + i] = sushi[i];
        }

        System.out.println(getMaxSushiVariety(N, d, k, c, sushi));

    }

    private static int getMaxSushiVariety(int N, int d, int k, int c, int[] sushi) {
        int[] count = new int[d + 1]; // i번째 원소 = 먹은 i번째 스시 종류의 개수

        int maxVar = 0; // 최대 먹을 수 있는 초밥의 종류 개수
        int var = 0; // 현재 먹을 수 있는 초밥의 종류 개수
        
        for (int i = 0; i < k; ++i) {
            if (count[sushi[i]]++ == 0) {
                ++var;
            }
        }
        
        // 보너스 초밥 처리
        if (count[c] > 0) { // 이미 보너스 초밥과 같은 종류 먹음
            maxVar = var;
        } else {
            maxVar = var + 1;
        }

        // 슬라이딩 윈도우 방식으로 윈도우를 옮겨가면서 먹을 수 있는 초밥 종류의 개수 계산
        for (int i = 1; i < N; ++i) {
            if (--count[sushi[i - 1]] == 0) {
                --var;
            }

            if (count[sushi[i + k - 1]]++ == 0) {
                ++var;
            }

            // 보너스 초밥 처리: 이미 먹은 종류일 경우와 처음 보는 경우 나눠서 처리
            if (count[c] > 0 && var > maxVar) {
                maxVar = var;
            } else if (count[c] == 0 && var + 1 > maxVar) {
                maxVar = var + 1;
            }
        }

        return maxVar;
    }
}
