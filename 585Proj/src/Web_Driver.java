import java.io.IOException;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;

import drivers.Driver;
import img.Screenshot;

 
public class Web_Driver {
		 
	public static void main(String[] args) throws IOException, InterruptedException {
		
		Driver ini = new Driver();
		ini.setUp();
		Screenshot scr = new Screenshot();
		String url = "https://demosite-rosayang.c9users.io/index.html";
		
		
		WebDriver FF_Driver = new FirefoxDriver();
		scr.get(FF_Driver, url, "FF");
		
		WebDriver CH_Driver = new ChromeDriver();
		ChromeOptions options = new ChromeOptions();
		options.addArguments("--start-maximized");
		CH_Driver = new ChromeDriver(options);
		scr.get(CH_Driver, url, "CH");

	}
}