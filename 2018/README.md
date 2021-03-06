# AdventOfCode
2018 edition of http://adventofcode.com/

Doing one previously unfamiliar language each day:

| Day | Language | Timings (s) | Comments |
| --- | -------- | ----------- | -------- |
| 1 | Rust | P1: 0.01, P2: 0.17 | A bit verbose, but some cool modern features (interresting error handling, nice data structures, map/filter etc). Seems a bit like a mixture between Kotlin and C++. Slow compile times. Turning on compiler optimizations makes an order of magnitude difference in runtime (timings are with -O), slightly faster than an equivalent Python implementation. |
| 2 | Typescript(Node) | P1: 0.14, P2: 0.11 | Not as terrible to program in as expected, but still a bit wierd. Fun to try something a bit more event-based. Also slow compile times, even though it is (from my perspective) not doing much. Quite a bit slower than a similar Python implementation for part 1, roughly similar for part2. |
| 3 | C#(Mono) | P1: 0.14, P2: 0.14 | Actually pretty nice, fast compiler (on Linux!), expected features (string splitting, dynamic lists, map/reduce etc) are available and seem to work as expected, except for the slightly unusual syntax and capitalised functions. |
| 4 | Go | P1: 0.00, P2: 0.00 | Had a quite frustrating time trying to solve this in Haskell/Lisp. Turns out learning these is going to take more than half an hour during a lecture... Fell back on Go which I used very briefly before. Turned out to be a quite pleasant experience. Special bonus points for the compiler, it provides very helpful feedback on errors (in only one line!) and also fails you for bad practice stuff (unused variables etc). Feels like a more hand-holdy version of Rust, which is both good and bad. Seems fast, but I don't have anything to compare to this time. |
| 5 | Perl | P1: 0.58, P2: 11.71 | Got stuck for a while due to perl appearantly including the newline char when reading line by line. Compiler errors are sometimes terrible (missing a ';' will give totally unrelated errors for some of the following rows), sometimes pretty useful (did you miss 'my'?). Manages to be over twice as slow compared to the same approach in Python for part 1, five times as slow in part 2. While it wasn't necessarily bad to program in I couldn't find a reason to use this instead of Python. Installing stuff using cpan only worked in root mode for some reason, installing the library through the package manager didn't work either. |
| 6 | Ruby | P1: 2.98, P2: 1.27 | I wanted something easy to quickly catch up a bit and selected Ruby. Turns out it was a nice choise: flexible, quite compact code, great standard library. Could see using this instead of Python sometimes, it was quite fun to program in! Error messages where okay, though nothing special. |


## Notes
Timings will need to be redone, they are not all measured on the same machine.

Pontentially planned languages: Erlang, Clojure/LISP, Prolog, OCaml, Haskell, Scala.