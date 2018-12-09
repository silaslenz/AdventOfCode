points = File.readlines('input').map {|line| line.strip.split(', ').map{|value| value.to_i}}
# puts points

def manhattan_distance(x,y, points)
    points.collect{|point| (x - point[0]).abs + (y - point[1]).abs}
end

max_x = points.collect {|x| x[0] }.max
max_y = points.collect {|x| x[1] }.max


# grid = Array.new(max_x+1) { Array.new(max_y+1)}
grid = {}
infinite = []
# p grid
for x in 0..max_x
    for y in 0..max_y
        distances = manhattan_distance(x,y, points)
        closest = distances.each_index.select{|i| distances[i] == distances.min}
        # puts distances
        grid[[x,y]] = closest.length == 1 ? closest[0] : nil
        if x == 0 || x==max_x || y == 0 || y == max_y
            infinite.append(closest.length == 1 ? closest[0] : nil)
        end
    end
end

# p grid
# p infinite

biggest = 0
for n in 0..points.length
    if grid.values.count(n) > biggest && (!infinite.include? n)
        biggest = grid.values.count(n)
    end
end
p biggest