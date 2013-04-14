#include "file_reader.h"
#include <iostream>
#include <fstream>

file_reader::file_reader(std::string filename)
{
	file_name = filename;
}

file_reader::~file_reader()
{

}

std::string file_reader::get_file_name()
{
	return file_name;
}

std::vector<std::string> file_reader::get_data()
{
	return data;
}

void file_reader::read_file()
{
	std::ifstream input(file_name.c_str());
	for (std::string line; getline(input, line); )
	{
		data.push_back(line);
	}
	input.close();
}

void file_reader::display()
{
	std::cout << "*** " << file_name << std::endl;

	for (std::vector<std::string>::iterator it = data.begin(); it != data.end(); ++it)
	{
		std::cout << *it << std::endl;
	}
}

int main(int argc, char* argv[])
{
	if (argc > 1)
	{
		for (int i = 1; i < argc; ++i)
		{
			file_reader fr = file_reader(std::string(argv[i]));
			fr.read_file();
			fr.display();
		}
	}
	else
	{
		std::cout << "there was nothing to do" << std::endl;
	}
	return 0;
}
