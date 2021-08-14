class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var a = 0
        for (i in 0..signs.size-1){
            a += absolutes[i] * if (signs[i]) 1 else -1
        }
        return a
    }
}