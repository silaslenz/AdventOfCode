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
	max_guard := 0
	max_among_all := 0
	max_asleep_minute_of_max_guard := 0
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
	for guard_id, _ := range sleep_times { 
		hour := make([]int, 60)
		for _, sleep_time := range sleep_times[guard_id]{
			for i := sleep_time.start; i < sleep_time.end; i++{
				hour[i]++
			}
		}
		max := 0
		max_asleep := -1
		for minute, asleep_counter := range hour{
			if asleep_counter>max{
				max = asleep_counter
				max_asleep = minute
			}
		}
        if (max>max_among_all){
            max_among_all = max
			max_guard = guard_id
			max_asleep_minute_of_max_guard = max_asleep
        }
    }

   fmt.Println(max_guard, max_among_all, max_asleep_minute_of_max_guard, max_asleep_minute_of_max_guard*max_guard)
}