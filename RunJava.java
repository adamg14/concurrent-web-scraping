import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class RunJava{
    public static void main(String[] args){
        try{
            String script = "hello.py";
            // create a new process to run the python file
            ProcessBuilder processBuilder = new ProcessBuilder("python", "hello.py", "adam");

            processBuilder.redirectErrorStream(true);


            // start the created process
            Process process = processBuilder.start();

            // the input stream is the output of the process
            InputStream inputStream = process.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            String line;
            List<String> output = new ArrayList<String>();
            while((line = reader.readLine()) != null){
                System.out.println(line);
                output.add(line);
            }

            for(int i = 0; i < output.size(); i++){
                System.out.print(output.get(i));
            }
            // wait for the script to complete
            int exit = process.waitFor();
        }catch(IOException | InterruptedException e){
            e.printStackTrace();
        }
    }
}