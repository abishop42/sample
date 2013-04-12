
#include <stdio.h>
#include <stdlib.h>
#include <iostream>


void int_sample()
{
	int nums[] = {0,1,2,3,4,5,6,7,8,9,10};


	int size_nums = sizeof(nums);
	int size_nums_0 = sizeof(nums[0]);
	
	std::cout << "size of (nums,nums[0]): " << size_nums 
		<< " , " << size_nums_0 << std::endl
		<< "items in array: " << size_nums/size_nums_0 << std::endl;

}

void check_string_array(std::string strings[])
{
	int size_strings = sizeof(strings);
	int size_strings_0 = sizeof(strings[0]);

	std::cout << "size of (strings,strings[0]): " << size_strings 
		<< " , " << size_strings_0 << std::endl
		<< "items in array: " << size_strings/size_strings_0 << std::endl;


}

void string_sample()
{
	std::string strings[] = {"this", "is", "a test", "string"};
	
	int size_strings = sizeof(strings);
	int size_strings_0 = sizeof(strings[0]);

	std::cout << "size of (strings,strings[0]): " << size_strings 
		<< " , " << size_strings_0 << std::endl
		<< "items in array: " << size_strings/size_strings_0 
		<< std::endl;

	check_string_array(strings);

}

int main()
{
	int_sample();
	string_sample();
	
	return 0;
}
