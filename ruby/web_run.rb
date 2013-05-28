require 'rubygems'
#require 'watir-webdriver'
require 'watir'
 
 
class UserStep
  attr_accessor :type,:value
  def initialize(type="url",value=nil)
                                @type = type
                                @value = value
                end
end
 
class WebSurfer
 
                attr_accessor :driver, :window_list
 
                def initialize()
                                @driver = Watir::IE.new                              
    @window_list = []
                end
 
                def browse(steps)
                                steps.each do|s|
                                                  puts "#{s.type} -> #{s.value}"
                case s.type
                                when "url"
                                                @driver.goto s.value   
                                when "go back"
                                                @driver.back
                                when "sleep"
                                                sleep(s.value)
                                when "add_value"
                                                @driver.text_field(:id,s.value["name"]).set s.value["value"]
                                when "click"
                                                @driver.button(:id, s.value).click
          when "nav click"
            @driver.lis(s.value["div_type"],s.value["div_value"])[0].links[0].click
                                when "clear"
                                                @driver.button(:id, s.value).click
          when "reload"
            @driver.refresh
          when "new window"
            window_list << @driver.url
            @driver = Watir::IE.new
          when "close window"
            @driver.close
            @driver = Watir::IE.attach(:url, s.value)
            window_list.remove s.value
          when "click result link"
            v = s.value
            #expect pos, result div name
            puts "click link result"
            puts v["div_type"]
            puts v["div_value"]
            @driver.divs(v["div_type"],v["div_value"])[0].lis[v["pos"]].link.click
          when "click google search suggestion"
            v = s.value
            puts v["div_type"]
            puts v["div_value"]
            @driver.tables(:class,v["div_value"])[0].spans.each do|l|
              puts "suggestion -> #{l.text}"
              if l.text == v["search term"]
                puts "using suggestion -> #{l.text}"
                l.click
                break
              end
            end           
                                else
                                puts "invalid step"
          end
      end
  end
end
 
google_url = UserStep.new("url","www.google.com")
google_search_click = UserStep.new("click","gbqfb")
google_search_box_clear = UserStep.new("clear","gbqfq")
page_reload = UserStep.new("reload")
go_back = UserStep.new("go back")
 
google_login = [google_url,UserStep.new("click", "gbi4t"),UserStep.new("sleep",5),
                UserStep.new("clear", "Email"),UserStep.new("add_value",{"name" => "Email", "value" => "abishop.test"}),
                UserStep.new("clear", "Passwd"),UserStep.new("add_value",{"name" => "Passwd", "value" => "testable"}),
                UserStep.new("click", "signIn")]
 
 
google_logout = [google_url,UserStep.new("sleep",5),UserStep.new("click", "gbg4"),
                 UserStep.new("sleep",1),UserStep.new("click", "gb_71")]
 
 
search_travel = []
search_travel << google_url
search_travel << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
search_travel << UserStep.new("sleep",1)
search_travel << google_search_click
search_travel << UserStep.new("sleep",60)
 
search_hash_and_equals = []
search_hash_and_equals << google_url
search_hash_and_equals << UserStep.new("add_value",{"name" => "gbqfq","value" => "testing the hash issue"})
search_hash_and_equals << UserStep.new("sleep",1)
search_hash_and_equals << google_search_click
search_hash_and_equals << UserStep.new("sleep",60)
search_hash_and_equals << google_url
search_hash_and_equals << UserStep.new("add_value",{"name" => "gbqfq","value" => "testing the equals sign issue"})
search_hash_and_equals << UserStep.new("sleep",1)
search_hash_and_equals << google_search_click
search_hash_and_equals << UserStep.new("sleep",60)
 
yahoo_cars_netbank_register = []
yahoo_cars_netbank_register << UserStep.new("url","au.yahoo.com")
yahoo_cars_netbank_register << UserStep.new("sleep",20)
yahoo_cars_netbank_register << UserStep.new("nav click",{"div_type" => :id,"div_value" => "nav-cars"})
yahoo_cars_netbank_register << UserStep.new("sleep",60)
yahoo_cars_netbank_register << UserStep.new("url","www.netbank.commbank.com.au")
yahoo_cars_netbank_register << UserStep.new("sleep",20)
yahoo_cars_netbank_register << UserStep.new("click","lnkRegistration")
yahoo_cars_netbank_register << UserStep.new("sleep",60)
 
 
 
#Dual Terms Test 1
#1. Type 'travel into the browser address bar and hit enter.
#2. The previous step usually takes the user to the results page for the term 'travel'. If this is the case, delete 'travel' from the search box and replace it with 'books' and hit enter.
#3. Navigate back using ALT + ← or the navigate back button.
 
dual_terms_1 = []
dual_terms_1 << google_url
dual_terms_1 << UserStep.new("sleep",60)
dual_terms_1 << google_search_box_clear
dual_terms_1 << UserStep.new("add_value",{"name" => "gbqfq","value" => "books"})
dual_terms_1 << google_search_click
dual_terms_1 << UserStep.new("sleep",60)
dual_terms_1 << go_back
dual_terms_1 << UserStep.new("sleep",60)
 
#Dual Terms Test 2
#1. Go to www.google.com, type in 'travel' and hit enter.
#2. Go to www.google.com, type in 'travel' and hit enter. While on the results page delete 'travel' from the search box and replace it with 'books. Then hit enter.
#3. Navigate back using ALT + ← or the navigate back button.
 
dual_terms_2 = []
dual_terms_2 << google_url
dual_terms_2 << UserStep.new("sleep",10)
dual_terms_2 << google_search_box_clear
dual_terms_2 << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
dual_terms_2 << google_search_click
dual_terms_2 << UserStep.new("sleep",60)
dual_terms_2 << google_search_box_clear
dual_terms_2 << UserStep.new("add_value",{"name" => "gbqfq","value" => "books"})
dual_terms_2 << google_search_click
dual_terms_2 << UserStep.new("sleep",60)
dual_terms_2 << go_back
dual_terms_2 << UserStep.new("sleep",60)
 
#Dual Terms Test 3
#1. Open a new tab in your browser. In the address bar, type 'travel' and hit enter.
#2. Open a new tab in your browser. In the address bar, type 'books' and hit enter. While on the results page, delete 'books' from the search box and replace it with 'cake'. Then hit enter.
#3. Navigate back using ALT + ← or the navigate back button.
 
dual_terms_3 = []
dual_terms_3 << UserStep.new("url","travel")
dual_terms_3 << UserStep.new("sleep",60)
dual_terms_3 << UserStep.new("new window")
dual_terms_3 << UserStep.new("url","books")

 
google_url = UserStep.new("url","www.google.com")
google_search_click = UserStep.new("click","gbqfb")
google_search_box_clear = UserStep.new("clear","gbqfq")
page_reload = UserStep.new("reload")
go_back = UserStep.new("go back")
 
google_login = [google_url,UserStep.new("click", "gbi4t"),UserStep.new("sleep",5),
                UserStep.new("clear", "Email"),UserStep.new("add_value",{"name" => "Email", "value" => "abishop.test"}),
                UserStep.new("clear", "Passwd"),UserStep.new("add_value",{"name" => "Passwd", "value" => "SOMEPASSWORD"}),
                UserStep.new("click", "signIn")]
 
 
google_logout = [google_url,UserStep.new("sleep",5),UserStep.new("click", "gbg4"),
                 UserStep.new("sleep",1),UserStep.new("click", "gb_71")]
 
 
search_travel = []
search_travel << google_url
search_travel << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
search_travel << UserStep.new("sleep",1)
search_travel << google_search_click
search_travel << UserStep.new("sleep",60)
 
search_hash_and_equals = []
search_hash_and_equals << google_url
search_hash_and_equals << UserStep.new("add_value",{"name" => "gbqfq","value" => "testing the hash issue"})
search_hash_and_equals << UserStep.new("sleep",1)
search_hash_and_equals << google_search_click
search_hash_and_equals << UserStep.new("sleep",60)
search_hash_and_equals << google_url
search_hash_and_equals << UserStep.new("add_value",{"name" => "gbqfq","value" => "testing the equals sign issue"})
search_hash_and_equals << UserStep.new("sleep",1)
search_hash_and_equals << google_search_click
search_hash_and_equals << UserStep.new("sleep",60)
 
yahoo_cars_netbank_register = []
yahoo_cars_netbank_register << UserStep.new("url","au.yahoo.com")
yahoo_cars_netbank_register << UserStep.new("sleep",20)
yahoo_cars_netbank_register << UserStep.new("nav click",{"div_type" => :id,"div_value" => "nav-cars"})
yahoo_cars_netbank_register << UserStep.new("sleep",60)
yahoo_cars_netbank_register << UserStep.new("url","www.netbank.commbank.com.au")
yahoo_cars_netbank_register << UserStep.new("sleep",20)
yahoo_cars_netbank_register << UserStep.new("click","lnkRegistration")
yahoo_cars_netbank_register << UserStep.new("sleep",60)
 
 
 
#Dual Terms Test 1
#1. Type 'travel into the browser address bar and hit enter.
#2. The previous step usually takes the user to the results page for the term 'travel'. If this is the case, delete 'travel' from the search box and replace it with 'books' and hit enter.
#3. Navigate back using ALT + ← or the navigate back button.
 
dual_terms_1 = []
dual_terms_1 << google_url
dual_terms_1 << UserStep.new("sleep",60)
dual_terms_1 << google_search_box_clear
dual_terms_1 << UserStep.new("add_value",{"name" => "gbqfq","value" => "books"})
dual_terms_1 << google_search_click
dual_terms_1 << UserStep.new("sleep",60)
dual_terms_1 << go_back
dual_terms_1 << UserStep.new("sleep",60)
 
#Dual Terms Test 2
#1. Go to www.google.com, type in 'travel' and hit enter.
#2. Go to www.google.com, type in 'travel' and hit enter. While on the results page delete 'travel' from the search box and replace it with 'books. Then hit enter.
#3. Navigate back using ALT + ← or the navigate back button.
 
dual_terms_2 = []
dual_terms_2 << google_url
dual_terms_2 << UserStep.new("sleep",10)
dual_terms_2 << google_search_box_clear
dual_terms_2 << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
dual_terms_2 << google_search_click
dual_terms_2 << UserStep.new("sleep",60)
dual_terms_2 << google_search_box_clear
dual_terms_2 << UserStep.new("add_value",{"name" => "gbqfq","value" => "books"})
dual_terms_2 << google_search_click
dual_terms_2 << UserStep.new("sleep",60)
dual_terms_2 << go_back
dual_terms_2 << UserStep.new("sleep",60)
 
#Dual Terms Test 3
#1. Open a new tab in your browser. In the address bar, type 'travel' and hit enter.
#2. Open a new tab in your browser. In the address bar, type 'books' and hit enter. While on the results page, delete 'books' from the search box and replace it with 'cake'. Then hit enter.
#3. Navigate back using ALT + ← or the navigate back button.
 
dual_terms_3 = []
dual_terms_3 << UserStep.new("url","travel")
dual_terms_3 << UserStep.new("sleep",60)
dual_terms_3 << UserStep.new("new window")
dual_terms_3 << UserStep.new("url","books")
dual_terms_3 << UserStep.new("sleep",60)
dual_terms_3 << UserStep.new("add_value",{"name" => "gbqfq","value" => "cake"})
dual_terms_3 << google_search_click
dual_terms_3 << UserStep.new("sleep",60)
dual_terms_3 << go_back
dual_terms_3 << UserStep.new("sleep",60)
dual_terms_3 << UserStep.new("close window","www.google.com")
 
 
 
#1. Go to www.google.com, type in 'travel' and hit enter immediately.
google_instant = []
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
#2. Go to www.google.com, type in 'travel' and hit enter immediately. Once the results have loaded, hit CTRL + R or the reload button.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
google_instant << page_reload
google_instant << UserStep.new("sleep",60)
#3. Go to www.google.com, type in 'travel' and hit enter immediately. Click on the first organic search result. Once the page has loaded, navigate back to the search results page using ALT + ← or the navigate back button.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
google_instant << UserStep.new("click result link",{"div_type" => :id,"div_value" => "ires", "pos" => 0})
google_instant << UserStep.new("sleep",60)
google_instant << go_back
google_instant << UserStep.new("sleep",60)
#4. Go to www.google.com, paste in 'travel' and hit enter immediately.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
#5. Go to www.google.com, type in 'travel' and hit enter right after results appear.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << UserStep.new("sleep",2)
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
#6. Go to www.google.com, paste in 'travel'  and hit enter right after results appear.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << UserStep.new("sleep",2)
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
#7. Go to www.google.com, type in 'travel' and hit enter after waiting three seconds.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << UserStep.new("sleep",4)
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
#8. Go to www.google.com, paste  in 'travel' and hit enter after waiting three seconds.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << UserStep.new("sleep",4)
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
#. Go to www.google.com, type in "trav" and select 'travel' from list (results for "travelocity" already being displayed).
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "trav"})
google_instant << UserStep.new("click google search suggestion",{"div_type" => :class,"div_value" => "gssb_m", "search term" => "travel"})
google_instant << UserStep.new("sleep",60)
#10. Go to www.google.com, type in 'tec' and select "techbargains" from list immediately.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "tec"})
google_instant << UserStep.new("click google search suggestion",{"div_type" => :class,"div_value" => "gssb_m", "search term" => "techbargains"})
google_instant << UserStep.new("sleep",60)
#11. Go to www.google.com, type in 'tec' and select "techbargains" from list after waiting three seconds.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "tec"})
google_instant << UserStep.new("sleep",3)
google_instant << UserStep.new("click google search suggestion",{"div_type" => :class,"div_value" => "gssb_m", "search term" => "techbargains"})
google_instant << UserStep.new("sleep",60)
#12. Go to www.google.com, type in 'travel' and wait three seconds.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << UserStep.new("sleep",3)
#3. Go to www.google.com, paste in 'travel' and wait three seconds.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "trav"})
google_instant << UserStep.new("sleep",3)
#4. Go to www.google.com, type in 'trav' and wait three seconds.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "trav"})
google_instant << UserStep.new("sleep",3)
#15. Go to www.google.com, type in 'trsvel', correct it to "travel", and wait three seconds.
google_instant << google_url
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "trsvel"})
google_instant << UserStep.new("sleep",1)
google_instant << google_search_box_clear
google_instant << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
google_instant << google_search_click
google_instant << UserStep.new("sleep",60)
 
test = []
test << google_url
test << UserStep.new("add_value",{"name" => "gbqfq","value" => "travel"})
test << google_search_click
test << UserStep.new("sleep",5)
test << UserStep.new("click result link",{"div_type" => :id,"div_value" => "ires", "pos" => 0})
#test << UserStep.new("click google search suggestion",{"div_type" => :class,"div_value" => "gssb_m", "search term" => "travel"})
test << UserStep.new("sleep",60) 
 
 
browser = WebSurfer.new
todo = [
  #google_login,
  search_travel,
  search_hash_and_equals,
  yahoo_cars_netbank_register,
  dual_terms_1, 
  dual_terms_2,
  #dual_terms_3,
  google_instant,
  google_logout,
  #search_travel,
  #search_hash_and_equals,
  #yahoo_cars_netbank_register,
  #dual_terms_1, 
  #dual_terms_2,
  #dual_terms_3,
  #google_instant
]
counter = 10
while counter > 0
  todo.each do |t|
    browser.browse t
  end
  counter = counter - 1
end


