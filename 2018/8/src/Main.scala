import scala.io.Source

object Main extends App {

  val filename = "input"

  var data = Source.fromFile(filename).getLines().next().split(" ").map(_.toInt)

  def parse(input: Seq[Int], index: Int): (Int, Int) = {
    val (numChildren, numMetadata) = (input(index), input(index + 1))
    println(numChildren, numMetadata, index)
    var children: Seq[Int] = Seq.empty[Int]
    var eaten = index + 2
    for (_ <- 0 until numChildren) {
      val output = parse(input, eaten)
      children = children :+ output._1
      println("children output ", output._1)
      eaten = output._2
    }
    println("children", children mkString "\n")

    val metadata = for (i <- 0 until numMetadata)
      yield input(eaten + i)
    println("metadata", metadata mkString " ")
    (children.sum + metadata.sum, eaten + numMetadata)
  }

  println("final result:", parse(data, 0))

}