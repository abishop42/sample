require 'rubygems'
require 'selenium-webdriver'





class Browser_Test
	
	attr_accessor :browser
  	
  	def initialize(t)
		@browser = Selenium::WebDriver.for t
	end


	def get_next_race()
		puts "getting next race to run"

		divs = @browser.find_elements(:id, 'NEXTTORACE-tab')
		
		if divs.count == 1
			headers = divs[0].find_elements(:tag_name, 'h3')
			headers[0].find_element(:tag_name,'a').click
		else
			divs = @browser.find_elements(:id,"content-id_SBT_RacingNextHorse_SBT_RacingNextHorseContent")
			if divs.count == 1
				divs[0].find_element(:tag_name,'a').click	
			end
		end
	end

	def visit(url)
		begin
			puts "going to #{url}"
			@browser.get url
			sleep 3
		rescue Selenium::WebDriver::Error::WebDriverError => e
			puts "oh look an error"
		rescue => e
			puts "oh look another type of error"			
		end
	end

	def close()
		@browser.close
	end
end


if __FILE__ == $0
	puts "meh"
	bt = Browser_Test.new(:firefox)
	bt.visit("http://www.sportsbet.com.au")
	bt.visit("http://www.sportsbet.com.au/horse-racing/australia-nz/caulfield/race-3-707740.html?LeftNav")
	bt.get_next_race()
end