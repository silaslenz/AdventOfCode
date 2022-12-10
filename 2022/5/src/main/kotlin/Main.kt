import java.io.File

fun main() {
    val lines = File("src/main/kotlin/input").readLines()
    val stacks = getStacks(lines)
    moveStuff(lines, stacks, reverse = true) // Change to false for part B
    stacks.forEach { print(it[0]) }
}

operator fun <T> List<T>.component6() = this[5]
private fun moveStuff(
    lines: List<String>,
    stacks: MutableList<MutableList<Char>>,
    reverse: Boolean
) {
    lines.forEach { line ->
        if (line.startsWith("move")) {
            val (_, count, _, from, _, to) = line.split(" ")
            val countInt = count.toInt()
            val fromInt = from.toInt() - 1
            val toInt = to.toInt() - 1

            val cratesToMove = stacks[fromInt].take(countInt).toMutableList()
            if (reverse) cratesToMove.reverse()

            stacks[toInt].addAll(0, cratesToMove)
            stacks[fromInt].subList(0, countInt).clear()
        }
    }
}

private fun getStacks(lines: List<String>): MutableList<MutableList<Char>> {
    val stacks = mutableListOf<MutableList<Char>>()

    for (line in lines) {
        if (line.isEmpty()) {
            break
        }
        (1..line.length step 4).forEach { index ->
            val crate = line[index]
            if (crate != ' ' && !crate.isDigit()) {
                val stackIndex = (index - 1) / 4
                while (stacks.size <= stackIndex) {
                    stacks.add(mutableListOf())
                }
                stacks[stackIndex].add(crate)
            }
        }
    }
    return stacks
}