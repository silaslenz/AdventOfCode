package main

import (
	"strings"
    "bufio"
    "fmt"
    "log"
    "os"
    "sort"
    "strconv"
)

func getDate(line string) string{
    return line[1:11]
}

func getMinute(line string) int{
    result, _ := strconv.Atoi(line[15:17])
    return result
}

func getAction(line string) string{
    return strings.Split(line, "] ")[1]
}


func main() {
    file, err := os.Open("input")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()


    type sleep struct{
        start int
        end int
    }

    lines := make([]string,0)
    sleep_times := make(map[int][]sleep) // Guard => [start/end]
    minutes_asleep := make(map[int]int) // Guard => minutes

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
		lines = append(lines, scanner.Text())
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
    sort.Strings(lines)

    guard := 0
    start := 0
    for _, line := range lines{
        if (strings.Contains(line,"Guard")){
            guard, _ = strconv.Atoi(strings.Split(getAction(line)," ")[1][1:])
        } else if (strings.Contains(line, "falls")){
            start = getMinute(line)
        } else {
            end := getMinute(line)
            sleep_times[guard] = append(sleep_times[guard], sleep{start,end})
            minutes_asleep[guard]+= (end-start)
        }
    }
    

    max_guard := 0
    max := 0
    for guard_id, sleep_minutes := range minutes_asleep { 
        if (sleep_minutes>max){
            max = sleep_minutes
            max_guard = guard_id
        }
    }
    hour := make([]int, 60)
    for _, sleep_time := range sleep_times[max_guard]{
        for i := sleep_time.start; i < sleep_time.end; i++{
            hour[i]++
        }
    }
    max_asleep := -1
    max = 0
    for minute, asleep_counter := range hour{
        if asleep_counter>max{
            max = asleep_counter
            max_asleep = minute
        }
    }
    fmt.Println("Guard", max_guard, "was asleep for", max, "minutes at ", sleep_times[max_guard], " with the most sleepy minute beeing " , max_asleep)
    fmt.Println("Answer part 1:", max_guard*max_asleep)
}