require 'rubygems'
require 'selenium-webdriver'


def get_next_race(browser, values)
	puts "get next race to run"
	div = browser.find_element(:id, 'NEXTTORACE-tab')
	headers = div.find_elements(:tag_name, 'h3')
	headers[0].find_element(:tag_name,'a').click
end



class Browser_Test
	
	attr_accessor :browser, :methods
  	
  	def initialize(t)
		@browser = Selenium::WebDriver.for t
		@methods = {}
	end


	def add_method(name, function)
		@methods[name] = function
	end

	def call_method(name, values)
		@methods[name].call(@browser, values)
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
	bt.add_method('get_next_race', method(:get_next_race))
	bt.visit("http://www.sportsbet.com.au")
	bt.call_method('get_next_race', "some_value")
end