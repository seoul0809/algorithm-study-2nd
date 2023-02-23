/*
https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=java

주어진 배열을 탐색하면서 현재 값보다 작은 값이 언제 나오는지 구하면 되는 문제
문제 카테고리는 스택/큐 였는데 모르겠어서 그냥 배열로 이중 for loop 돌림
효율성 문제 생길 줄 알았는데 안생겨서 그냥 넘어가기로 함
*/

class Solution {
    public int[] solution(int[] prices) {
        int len = prices.length;
        int[] answer = new int[len];
        
        for(int i = 0; i < len-1; i++){
            answer[i] = 1;
            for(int j = i+1; j < len-1; j++){
                if(prices[j] >= prices[i]){
                    answer[i] += 1;
                } else {
                    break;
                }
            }
        }
        
        return answer;
    }
}
