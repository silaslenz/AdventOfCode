let lines = System.IO.File.ReadAllLines("input")
let counter = ref 0
let counterTwo = ref 0

for line in lines do
    let split = line.Split(',')
    let a = split[ 0 ].Split('-') |> Array.map int
    let b = split[ 1 ].Split('-') |> Array.map int

    let idsInAButNotB =
        Set.ofSeq (seq { a[0] .. a[1] }) - Set.ofSeq (seq { b[0] .. b[1] })

    let idsInBButNotA =
        (Set.ofSeq (seq { b[0] .. b[1] }) - Set.ofSeq (seq { a[0] .. a[1] }))

    if idsInAButNotB.Count = 0 || idsInBButNotA.Count = 0 then
        counter.Value <- counter.Value + 1

    if idsInAButNotB.Count < a[1] - a[0] + 1 || idsInBButNotA.Count < b[1] - b[0] + 1 then
        counterTwo.Value <- counterTwo.Value + 1


printfn $"Part 1: {counter.Value}"
printfn $"Part 2: {counterTwo.Value}"
