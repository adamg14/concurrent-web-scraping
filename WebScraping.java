import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class WebScraping extends Thread{

    private int threadNumber;
    private String articleURL;
    public WebScraping(String _articleURL, int _threadNumber){
        this.threadNumber = _threadNumber;
        this.articleURL = _articleURL;
    }

    public void run(){
        try{
            String script = "web_scraping.py";
            // create a new process to run the python file
            ProcessBuilder processBuilder = new ProcessBuilder("python", "/Users/adam/Documents/multithreading-projects/concurrent-web-scraping/web_scraping.py", articleURL);

            processBuilder.redirectErrorStream(true);


            // start the created process
            Process process = processBuilder.start();

            // the input stream is the output of the process
            InputStream inputStream = process.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            String line;
            List<String> output = new ArrayList<String>();
            while((line = reader.readLine()) != null){
                output.add(line);
            }
            for(int i = 0; i < output.size(); i++){
                System.out.println("Article " + threadNumber + " result: " + output.get(i));
            }

            // wait for the script to complete
            int exit = process.waitFor();
        }catch(IOException | InterruptedException e){
            e.printStackTrace();
        }
    }
}