using System;
using System.Linq;
 
public class HelloWorld
{
    static public void Main ()
    {
        string line;  
        // int max_size = 0;
        int[,] fabric_usage = new int[1001,1001];

        // Read the file and display it line by line.  
        System.IO.StreamReader file =   
            new System.IO.StreamReader(@"input");  
        while((line = file.ReadLine()) != null)  
        {  
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
        // System.Console.WriteLine(max_size);
        file.Close();  
    }
}
