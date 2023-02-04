/*
https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=java
begin에서 target으로 바뀌는 최소 변환 횟수를 구하는 문제
변환 규칙 : 한 번에 한 개의 알파벳만 바꿀 있고 words 배열안에 있는 단어들로만 가능
*/

class Solution {
    boolean[] visited;
    int answer = 0;
    
    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        dfs(begin, target, words, 0);
        return answer;
    }
    
    // 변환 횟수 구하기
    public void dfs(String begin, String target, String[] words, int cnt){
        if(begin.equals(target)){
            answer = cnt;
            return;
        }
        
        for(int i = 0, len = words.length; i < len; i++){
            if(visited[i]) continue;

            if(check(begin, words[i])){
                visited[i] = true;
                dfs(words[i], target, words, cnt+1);
                visited[i] = false;
            }
        }
    }
  
    // 다른 알파벳 개수 체크
    public boolean check(String begin, String target){
        int cnt = 0;
        for(int i = 0, len = begin.length(); i < len; i++){
            if(begin.charAt(i) != target.charAt(i)) cnt++;
        }
        return cnt == 1;
    }
}
