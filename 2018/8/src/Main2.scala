import scala.io.Source

object Main2 extends App {

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
    var metadata: Seq[Int] = Seq.empty[Int]
    if (numChildren == 0) {
      metadata = for (i <- 0 until numMetadata)
        yield input(eaten + i)
    } else {
      metadata = for (i <- 0 until numMetadata if (input(eaten + i)  - 1 < children.length))
        yield children(input(eaten + i)-1)
    }
    println("metadata", metadata mkString " ")
    (metadata.sum, eaten + numMetadata)
  }

  println("final result:", parse(data, 0))

}