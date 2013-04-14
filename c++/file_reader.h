#include <string>
#include <vector>

class file_reader
{
	public:
		file_reader(std::string file_name);
		~file_reader();
		std::string get_file_name();
		void read_file();
		std::vector<std::string> get_data();
		void display(); //can I overwrite cout or printf type?

	private:
		std::string file_name;
		std::vector<std::string> data;
};

