# AdventOfCode
2018 edition of http://adventofcode.com/

Doing one previously unfamiliar language each day:

| Day | Language | Timings (s) | Comments |
| --- | -------- | ----------- | -------- |
| 1 | Rust | P1: 0.01, P2: 0.17 | A bit verbose, but some cool modern features (interresting error handling, nice data structures, map/filter etc). Seems a bit like a mixture between Kotlin and C++. Slow compile times. Turning on compiler optimizations makes an order of magnitude difference in runtime (timings are with -O), slightly faster than an equivalent Python implementation. |
| 2 | Typescript(Node) | P1: 0.14, P2: 0.11 | Not as terrible to program in as expected, but still a bit wierd. Fun to try something a bit more event-based. Also slow compile times, even though it is (from my perspective) not doing much. Quite a bit slower than a similar Python implementation for part 1, roughly similar for part2. |
| 3 | C#(Mono) | P1: 0.14, P2: 0.14 | Actually pretty nice, fast compiler (on Linux!), expected features (string splitting, dynamic lists, map/reduce etc) are available and seem to work as expected, except for the slightly unusual syntax and capitalised functions. |
| 4 | Go | P1: 0.00, P2: xx | Had a quite frustrating time trying to solve this in Haskell/Lisp. Turns out learning these is going to take more than half an hour during a lecture... Fell back on Go which I used very briefly little before. Turned out to be a quite pleasant experience. Special bonus points for the compiler, it provides very helpful feedback on errors (in only one line!) and also fails you for bad practice stuff (unused variables etc). Feels like a more hand-holdy version of Rust, which is both good and bad. |


## Notes
Timings will need to be redone, they are not all measured on the same machine.

Pontentially planned languages: Erlang, Clojure/LISP, Prolog, OCaml,Haskell, Scala, Ruby, Perl