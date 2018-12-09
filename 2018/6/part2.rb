points = File.readlines('input').map {|line| line.strip.split(', ').map{|value| value.to_i}}
# puts points

def manhattan_distance(x,y, points)
    points.collect{|point| (x - point[0]).abs + (y - point[1]).abs}
end

max_x = points.collect {|x| x[0] }.max
max_y = points.collect {|x| x[1] }.max

size = 0
for x in 0..max_x
    for y in 0..max_y
        distances = manhattan_distance(x,y, points)
        if distances.sum <10000
            size = size +1
        end
    end
end

p size
