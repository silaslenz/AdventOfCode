let lines = System.IO.File.ReadAllLines("input")
let counter = ref 0

for line in lines do
    let split = line.Split(',')
    let a = split[ 0 ].Split('-') |> Array.map int
    let b = split[ 1 ].Split('-') |> Array.map int

    if
        (Set.ofSeq (seq { a[0] .. a[1] }) - Set.ofSeq (seq { b[0] .. b[1] })).Count = 0
        || (Set.ofSeq (seq { b[0] .. b[1] }) - Set.ofSeq (seq { a[0] .. a[1] })).Count = 0
    then
        counter.Value <- counter.Value + 1

printfn $"{counter.Value}"
