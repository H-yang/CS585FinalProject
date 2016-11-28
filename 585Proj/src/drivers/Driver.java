package drivers;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Driver {

	public void setUp(){
		
		String chromeService = "C:\\chromedriver_win32\\chromedriver.exe";
		String firefoxService = "C:\\geckodriver\\wires.exe";
		String ieService = "C:\\IEDriverServer_x64_2.53.1\\IEDriverServer.exe";

		System.setProperty("webdriver.chrome.driver", chromeService);
		System.setProperty("webdriver.ie.driver", ieService);
		System.setProperty("webdriver.firefox.driver", firefoxService);
	}
	

	
}
