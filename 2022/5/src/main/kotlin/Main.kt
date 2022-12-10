import java.io.File

fun main() {
    val lines = File("src/main/kotlin/input").readLines()
    val stacks = getStacks(lines)
    moveStuff(lines, stacks, reverse = true) // Change to false for part B
    stacks.forEach { print(it[0]) }
}

private fun moveStuff(
    lines: List<String>,
    stacks: MutableList<MutableList<Char>>,
    reverse: Boolean
) {
    lines.forEach { line ->
        if (line.startsWith("move")) {
            val (count, _, from, _, to) = line.split("move ")[1].split(" ")
            if (reverse) {
                stacks[to.toInt() - 1].addAll(0, stacks[from.toInt() - 1].take(count.toInt()).reversed())
            } else {
                stacks[to.toInt() - 1].addAll(0, stacks[from.toInt() - 1].take(count.toInt()))
            }
            stacks[from.toInt() - 1].subList(0, count.toInt()).clear()
        }
    }
}

private fun getStacks(
    lines: List<String>,
): MutableList<MutableList<Char>> {
    val stacks = mutableListOf<MutableList<Char>>()

    for (line in lines) {
        if (line.isEmpty()) {
            break
        }
        (1..line.length step 4).forEach { index ->
            val crate = line[index]
            if (crate != ' ' && !crate.isDigit()) {
                while (stacks.size < index / 4 + 1) {
                    stacks.add(mutableListOf())
                }
                stacks[(index - 1) / 4].add(crate)
            }
        }
    }
    return stacks
}