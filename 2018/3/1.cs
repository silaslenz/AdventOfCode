using System;
using System.Linq;
using System.Collections.Generic;
 
public class HelloWorld
{
    static public void Main ()
    {
    
        string read_line;
        // int max_size = 0;
        int[,] fabric_usage = new int[1001,1001];

        List<string> lines = new List<string>();
        System.IO.StreamReader file =   
            new System.IO.StreamReader(@"input");  
        while((read_line = file.ReadLine()) != null)  
        {  
            lines.Add(read_line);
        }  
        file.Close();

        foreach (string line in lines){
            string[] words = line.Split(' ');
            string id = words[0];
            Int32[] start_coordinates = words[2].Trim(':').Split(',').Select(s => Int32.Parse(s)).ToArray();
            Int32[] size = words[3].Split('x').Select(s => Int32.Parse(s)).ToArray();;

            // max_size = Math.Max(max_size, start_coordinates[0]+size[0]);
            // max_size = Math.Max(max_size, start_coordinates[1]+size[1]);

            for(int x = start_coordinates[0]; x <start_coordinates[0]+size[0]; x++){
                for (int y = start_coordinates[1]; y < start_coordinates[1]+size[1]; y++){
                    fabric_usage[x,y]++;
                }
            }
        }
        
        int counter = 0;
        for(int x = 0; x <1001; x++){
            for (int y = 0; y < 1001; y++){
                if (fabric_usage[x,y]>1)
                    counter++;
            }
        }

        System.Console.WriteLine(counter);

        foreach(string line in lines){  
            string[] words = line.Split(' ');
            string id = words[0];
            Int32[] start_coordinates = words[2].Trim(':').Split(',').Select(s => Int32.Parse(s)).ToArray();
            Int32[] size = words[3].Split('x').Select(s => Int32.Parse(s)).ToArray();;

            bool is_unique = true;

            for(int x = start_coordinates[0]; x <start_coordinates[0]+size[0]; x++){
                for (int y = start_coordinates[1]; y < start_coordinates[1]+size[1]; y++){
                    if (fabric_usage[x,y] != 1){
                        is_unique = false;
                    }
                }
            }
            if (is_unique){
                System.Console.WriteLine(id);
                break;
            }
        }
    }
}
