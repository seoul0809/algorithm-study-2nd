/*
https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=java

해시맵 genre_sum을 만들어서 각 장르별 재생 횟수의 합을 구해준다.
해시맵 order를 만들어서 각 장르별 재생 횟수와 인덱스를 저장해주는데 pq의 길이가 2가 넘어가면 poll로 삭제한다.
genre_sum을 value 기준으로 정렬하면 재생 횟수가 작은 순서대로 정렬된다.
이 때 정렬된 genre_sum의 key를 가지고 order의 value를 가져와서 list의 0번째에 넣어주면 재생횟수가 가장 큰 순서대로 정렬된 형태가 된다.
list를 배열로 바꿔서 return한다.
*/
import java.util.*;
class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        
        List<Integer> list = new ArrayList<>();

        Map<String, Integer> genre_sum = new HashMap<>();
        Map<String, PriorityQueue<int[]>> order = new HashMap<>();

        for (int i = 0, len = genres.length; i < len; i++) {
            String genre = genres[i];
            int play = plays[i];
            if(!genre_sum.containsKey(genre)) {
                genre_sum.put(genre, 0);
                order.put(genre, new PriorityQueue<>((o1, o2) -> o1[0]-o2[0]));
            }

            genre_sum.put(genre, genre_sum.get(genre)+play);
            order.get(genre).add(new int[] {play, i});
            if(order.get(genre).size() > 2){
                order.get(genre).poll();
            }
        }

        List<Map.Entry<String, Integer>> entryList = new LinkedList<>(genre_sum.entrySet());
        entryList.sort(Map.Entry.comparingByValue());

        for (Map.Entry<String, Integer> entry : entryList) {
            String s = entry.getKey();
            for (int[] o : order.get(s)) {
                list.add(0,o[1]);
            }
        }
        int size = list.size();
        answer = list.stream().mapToInt(i->i).toArray();
        
        
        return answer;
    }
}
