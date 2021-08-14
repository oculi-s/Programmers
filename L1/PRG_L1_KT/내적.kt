class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        var s = 0
        for (i in 1..a.size){
            s += a[i-1] * b[i-1]
        }
        return s
    }
}