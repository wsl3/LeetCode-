import java.lang.reflect.Array;
import java.util.*;


public class Main{
    public static void main(String[] args){
        System.out.println(Character.getNumericValue('6'));
    }
}

// 8ms beat 83.5%
class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[][] row = new int[10][10];
        int[][] row2 = new int[10][10];
        int[][] clo = new int[10][10];
        int i,j,index,temp_index;
        // 检查行列
        for(i=0;i<9;i++){
            for(j=0;j<9;j++){
                if(board[i][j]!='.'){
                    index = Character.getNumericValue(board[i][j]);
                    row[i][index]++;
                    row2[j][index]++;
                    temp_index = i/3*3+j/3;
                    clo[temp_index][index]++;
                    if(row[i][index] >= 2 || row2[j][index]>=2 || clo[temp_index][index]>=2){
                        return false;
                    }

                }
            }
        }
        return true;
    }
}