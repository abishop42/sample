#include <stdio.h>
#include <stdlib.h>
#include <iostream>


enum {
	MAX_BUFFER = 128
};

struct run_result 
{
	std::string output;
	int return_code;
};

run_result run_command(std::string  command)
{

	command += " 2>&1";

	FILE *output = popen((char *)command.c_str(), "r");
	char buffer[MAX_BUFFER];

	run_result result;

	while(fgets(buffer, sizeof(buffer), output)!=NULL)
	{
		result.output += buffer;
	}

	result.return_code = pclose(output);

	return result;

}

int main()
{
	std::string commands[5] = {"ls","df","du","find .", "ifconfig"};
	for (int i = 0; i < 5; i++)
	{
		run_result result = run_command(commands[i]);
		std::cout << "------" << std::endl 
			<< commands[i] << std::endl 
			<< result.output << std::endl 
			<< "return code: " << result.return_code << std::endl;
	}
	return 0;
}
