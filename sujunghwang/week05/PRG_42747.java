/*
https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=java

주어진 배열에서 n보다 큰 값이 n개 이상인 값 중 최대값을 찾는 문제
주어진 배열을 역순으로 정렬해서 가장 큰 값을 max로 놓고 1씩 빼면서 배열에 있는 값들과 비교
*/

import java.util.Arrays;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int len = citations.length;

        Arrays.sort(citations);
        int[] ord = new int[len];
        for (int i = 0; i < len; i++) {
            ord[i] = citations[len-i-1];
        }
        int max = ord[0];

        for (int i = max; i >= 0; i--) {
            int cnt = 0;
            for (int j : ord) {
                if(j >= i) cnt++;
            }
            if(cnt >= i) {
                answer = i;
                break;
            }
        }

        return answer;
    }
}
