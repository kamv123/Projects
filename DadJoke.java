import java.net.ProxySelector;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;

public class DadJoke {
	
	// A method to make a web request at a certain URL and return the server's response as a String. 
	public static String getResponseText(String url) throws Exception {
		HttpRequest request = HttpRequest.newBuilder(new URI(url)).headers("Accept","text/plain").GET().build();
		HttpResponse<String> response = HttpClient
				  .newBuilder()
				  .proxy(ProxySelector.getDefault())
				  .build()
				  .send(request, BodyHandlers.ofString());
		return response.body();
	}

	public static void main(String[] args) throws Exception {		
		
		String url;		
		// Update the url, depending on how many command line arguments there are.
		if(args.length == 0) {
			url = "https://icanhazdadjoke.com/";
		}else if(args.length == 1) {
			url = "https://icanhazdadjoke.com/search?term="+args[0]+"&limit=1";
		}else{
			System.out.println("Error");
			return;
		}

		String joke = getResponseText(url); // Make a web request and save the server's response in a String called joke.
		if (joke.equals("")){
			System.out.println("Error");
			return;
		}

		System.out.println(joke);
	}

}