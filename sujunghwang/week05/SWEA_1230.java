/*
명령어에 따라 주어진 암호문을 편집하는 문제
리스트로 변환해서 암호문 편집을 편하게 할 수 있게 함
*/
import java.io.*;
import java.util.*;

public class SWEA_1230 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int tc = 1; tc <= 10; tc++) {
            int N = Integer.parseInt(br.readLine());
            String org = br.readLine();
            int cnt = Integer.parseInt(br.readLine());
            String chg = br.readLine();
            List<String> listOrg = new ArrayList<>();
            listOrg.addAll(Arrays.asList(org.split(" ")));
            List<String> listChg = new ArrayList<>();
            listChg.addAll(Arrays.asList(chg.split(" ")));
            List<String> temp = new ArrayList<>();

            for (int i = 0; i < cnt; i++) {
                if(listChg.get(0).equals("I")){
                    int x = Integer.parseInt(listChg.get(1));
                    int y = Integer.parseInt(listChg.get(2));
                    for (int j = 0; j < y; j++) {
                        listOrg.add(x+j,listChg.get(j+3));
                    }
                    for (int j = 0; j < 3+y; j++) {
                        listChg.remove(0);
                    }
                } else if(listChg.get(0).equals("D")){
                    int x = Integer.parseInt(listChg.get(1));
                    int y = Integer.parseInt(listChg.get(2));

                    for (int j = 0; j < 3; j++) {
                        listChg.remove(0);
                    }
                    for (int j = 0; j < y; j++) {
                        listOrg.remove(x);
                    }
                } else if(listChg.get(0).equals("A")){
                    int y = Integer.parseInt(listChg.get(1));
                    for (int j = 0; j < y; j++) {
                        listOrg.add(listChg.get(j + 2));
                    }
                    for (int j = 0; j < 2+y; j++) {
                        listChg.remove(0);
                    }
                }
            }
            System.out.println("#"+tc+" ");
            for (int i = 0; i < 10; i++) {
                System.out.print(listOrg.get(i)+" ");
            }
            System.out.println();
        }

    }
}
