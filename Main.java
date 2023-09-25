import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter articles: ");
        String userInput = scanner.nextLine();
        String[] articles = userInput.split(" ");

        for(int i = 0; i < articles.length; i++){
            WebScraping webScraping = new WebScraping(articles[i], i + 1);
            webScraping.start();
        }
        // for (int i = 1; i <= numberOfArticles; i++){
        //     System.out.print("Article " + i + " URL: ");
        //     String articleURL = scanner.nextLine();

        //     WebScraping webScraping = new WebScraping(articleURL, i);
        //     webScraping.start();
        // }
    }
}