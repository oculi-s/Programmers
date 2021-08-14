class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var a = IntArray(0)
        for (c in commands){
            a += array.slice((c[0]-1)..c[1]-1).sorted()[c[2]-1]
        }
        return a
    }
}